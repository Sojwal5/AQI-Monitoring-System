import serial
import time
from Adafruit_IO import Client

# Adafruit IO setup
ADAFRUIT_IO_USERNAME = 'xxxxxxxx'  # Enter your Adafruit IO username
ADAFRUIT_IO_KEY = 'xxxxxxxxxxxxxxxxxxx'  # Enter your Adafruit IO key
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

# Serial setup
ser = serial.Serial('/dev/ttyUSB0')

def calculate_overall_aqi(pm25_concentration, pm10_concentration,nhthree_concentration, co_concentration):
    # AQI calculation for PM2.5
    if 0 <= pm25_concentration <= 12:
        aqi_pm25 = (50 / 12) * pm25_concentration
    elif 12 < pm25_concentration <= 35.4:
        aqi_pm25 = ((100 - 51) / (35.4 - 12)) * (pm25_concentration - 12) + 51
    else: aqi_pm25 = ((100 - 51) / (500 - 35.4)) * (pm25_concentration - 35.4) + 51
    # Add more AQI calculation ranges for PM2.5 here...

    # AQI calculation for PM10
    if 0 <= pm10_concentration <= 54:
        aqi_pm10 = (50 / 54) * pm10_concentration
    elif 55 <= pm10_concentration <= 154:
        aqi_pm10 = ((100 - 51) / (154 - 55)) * (pm10_concentration - 55) + 51
    else: aqi_pm10 = ((100 - 51) / (500 - 154)) * (pm10_concentration - 154) + 51
    # Add more AQI calculation ranges for PM10 here...

    # Calculate overall AQI
    return max(aqi_pm25, aqi_pm10)

while True:
    data = []
    for index in range(0, 10):
        datum = ser.read()
        data.append(datum)

    # Convert data to concentrations (adjust these calculations based on your sensor)
    pmtwofive = int.from_bytes(b''.join(data[2:4]), byteorder='little') / 10
    pmten = int.from_bytes(b''.join(data[4:6]), byteorder='little') / 10
    nhthree = int.from_bytes(b''.join(data[6:8]), byteorder='little') / 10
    co = int.from_bytes(b''.join(data[8:10]), byteorder='little') / 10
    
    # Calculate overall AQI
    overall_aqi = calculate_overall_aqi(pmtwofive, pmten,nhthree,co)
    print("Overall AQI:", overall_aqi)

    # Optionally, you can send the overall AQI to Adafruit IO
    aio.send('aqi', overall_aqi)

    time.sleep(5)
