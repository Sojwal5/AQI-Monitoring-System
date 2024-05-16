import spidev
import time
from Adafruit_IO import Client, Feed, RequestError

class MQ135Reader:
    def __init__(self, spi_bus=0, spi_device=0):
        self.spi = spidev.SpiDev()
        self.spi.open(spi_bus, spi_device)
        self.spi.max_speed_hz = 1000000  # Set SPI speed to 1MHz (you may need to adjust this)
        self.aio = Client('xxxxxxxxxxxxxxxxxxxxxx', 'xxxxxxxxxxxxxxxxxxxxxx')  # Enter your Adafruit IO username and key
        self.feed_name = 'nh3-concentration'  # Name of your Adafruit IO feed

        try:
            self.nh3_feed = self.aio.feeds(self.feed_name)
        except RequestError:  # Create a new feed if it doesn't exist
            self.nh3_feed = Feed(name=self.feed_name)
            self.nh3_feed = self.aio.create_feed(self.nh3_feed)

    def read_analog(self, channel):
        # MCP3008 command format: [1, 8 + channel << 4, 0]
        command = [1, 8 + channel << 4, 0]
        adc_data = self.spi.xfer2(command)
        adc_value = ((adc_data[1] & 3) << 8) + adc_data[2]  # Combine 2 bytes of data
        return adc_value

    def send_to_adafruit(self, value):
        self.aio.send_data(self.nh3_feed.key, value)

if __name__ == "__main__":
    mq135_reader = MQ135Reader()
    channel = 0  # Assuming MQ135 is connected to channel 0 of ADC3008

    try:
        while True:
            adc_value = mq135_reader.read_analog(channel)
            print("NH3 Concentration : {} ug/m3".format(adc_value))
            mq135_reader.send_to_adafruit(adc_value)  # Send NH3 concentration to Adafruit feed
            time.sleep(30)  # Read every 10 seconds

    except KeyboardInterrupt:
        print("Program terminated by user")
