import serial
import time
import spidev
from mq import MQ
from Adafruit_IO import Client, Feed, RequestError
import threading
import sys

# Adafruit IO configuration
ADAFRUIT_IO_USERNAME = 'username'
ADAFRUIT_IO_KEY = 'io_key'

# Initialize Adafruit IO client
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

# Define the PMReader class
class PMReader:
    def __init__(self):
        self.aio = aio

    def read_pm(self):
        ser = serial.Serial('/dev/ttyUSB0')

        while True:
            data = []
            for index in range(0, 10):
                datum = ser.read()
                data.append(datum)

            pmtwofive = int.from_bytes(b''.join(data[2:4]), byteorder='little') / 10
            pmten = int.from_bytes(b''.join(data[4:6]), byteorder='little') / 10

            print("PM2.5:", pmtwofive)
            print("PM10:", pmten)

            aio.send('pm25', pmtwofive)
            aio.send('pm10', pmten)

            time.sleep(30)

# Define the MQ7Reader class
class MQ7Reader:
    def __init__(self):
        self.mq7 = MQ(analogPin=2)  # MQ7 connected to pin 2 of MCP3008
        self.molecular_weight_co = 28.01  # Molecular weight of CO in g/mol
        self.aio = aio
        self.feed_name = 'co-concentration'  # Name of Adafruit IO feed

        try:
            self.co_feed = self.aio.feeds(self.feed_name)
        except RequestError:
            self.co_feed = Feed(name=self.feed_name)
            self.co_feed = self.aio.create_feed(self.co_feed)

    def ppm_to_mg_per_m3(self, ppm):
        return (ppm * self.molecular_weight_co / 24.45) / 10 + 2

    def send_to_adafruit(self, value):
        self.aio.send_data(self.co_feed.key, value)

    def read_co(self):
        while True:
            perc = self.mq7.MQPercentage()
            co_ppm = perc["CO"]
            co_mg_per_m3 = self.ppm_to_mg_per_m3(co_ppm)
            self.send_to_adafruit(co_mg_per_m3)  
            sys.stdout.write("\r")
            sys.stdout.write("\033[K")
            sys.stdout.write("CO: %.2f mg/m3" % co_mg_per_m3)
            sys.stdout.flush()
            time.sleep(30)

# Define the MQ135Reader class
class MQ135Reader:
    def __init__(self, spi_bus=0, spi_device=0):
        self.spi = spidev.SpiDev()
        self.spi.open(spi_bus, spi_device)
        self.spi.max_speed_hz = 1000000
        self.aio = aio
        self.feed_name = 'nh3-concentration'

        try:
            self.nh3_feed = self.aio.feeds(self.feed_name)
        except RequestError:
            self.nh3_feed = Feed(name=self.feed_name)
            self.nh3_feed = self.aio.create_feed(self.nh3_feed)

    def read_analog(self, channel):
        command = [1, 8 + channel << 4, 0]
        adc_data = self.spi.xfer2(command)
        adc_value = ((adc_data[1] & 3) << 8) + adc_data[2] 
        return adc_value

    def send_to_adafruit(self, value):
        self.aio.send_data(self.nh3_feed.key, value)

if __name__ == "__main__":
    # Start reading PM sensor in a thread
    pm_reader = PMReader()
    pm_thread = threading.Thread(target=pm_reader.read_pm)
    pm_thread.start()

    # Read CO concentration
    mq7_reader = MQ7Reader()
    mq7_reader.read_co()

    # Read NH3 concentration
    mq135_reader = MQ135Reader()
    channel = 0
    while True:
        adc_value = mq135_reader.read_analog(channel)
        print("NH3 Concentration : {} ug/m3".format(adc_value))
        mq135_reader.send_to_adafruit(adc_value)  
        time.sleep(30)
