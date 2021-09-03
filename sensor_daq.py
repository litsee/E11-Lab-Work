# Measures Temperature, Humidity, Pressure
# BME280 - Adafruit 
#Write the data to a file - a time column, temperature, humidity, pressure
# look up Adafruit CircuitPython BME280 module
# update code to use that module 

import time
import board
from adafruit_bme280 import basic as adafruit_bme280
import csv 
import serial
import sys

port = serial.Serial("/dev/serial0", baudrate=9600, timeout=1.5)
start_time = time.time()
run_time = int(sys.argv[1])
sleep_interval= int(sys.argv[2])
stop_time = start_time + run_time
current_time = time.time()
FileName= sys.argv[3]
DelayTime = int(sys.argv[4])

SensorFile= open( FileName, "w",newline="")
header=['Time','Temperature', 'Humidity', 'Pressure', 'Altitude', ' PM1','PM2', 'PM3']


SensorWriter= csv.writer(SensorFile)
SensorWriter.writerow(header)
i2c = board.I2C()  # uses board.SCL and board.SDA
bme280= adafruit_bme280.Adafruit_BME280_I2C(i2c)
times = []
temperatures = []
relative_humidity=[]
pressure=[]
Altitude= []



time.sleep(DelayTime)


while current_time < stop_time:
	current_time = time.time()
	Temperature= bme280.temperature
	Humidity= bme280.relative_humidity
	Pressure= bme280.pressure
	Altitude = bme280.altitude
	text = port.read(32)
	PM1=int.from_bytes(text[4:6],byteorder='big')
	PM2=int.from_bytes(text[6:8],byteorder='big')
	PM3=int.from_bytes(text[8:10],byteorder='big')
	data_list= [current_time, Temperature, Humidity, Pressure, Altitude,PM1,PM2,PM3] 
	SensorWriter.writerow(data_list)
	time.sleep(sleep_interval)
	
	

print(data_list) 
