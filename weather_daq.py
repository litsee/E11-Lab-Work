# Measures Temperature, Humidity, Pressure
# BME280 - Adafruit 
#Write the data to a file - a time column, temperature, humidity, pressure
# look up Adafruit CircuitPython BME280 module
# update code to use that module 

import time
import board
from adafruit_bme280 import basic as adafruit_bme280
i2c = board.I2C()  # uses board.SCL and board.SDA
sensor= adafruit_bme280.Adafruit_BME280_I2C(i2c)
times = []
temperatures = []

start_time = time.time()
run_time = 10
stop_time = start_time + run_time
current_time = time.time()
while current_time < stop_time:
	current_time = time.time()
	temp = sensor.temperature
	print(temp)
	times.append(current_time)
	temperature.append(temp)
	time.sleep(1)
	
print(temperatures)
