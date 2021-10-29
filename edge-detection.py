import RPi.GPIO as GPIO
import time
import datetime
import csv
import sys
from time import sleep 


start_time = time.time()
run_time = int(sys.argv[1])
sleep_interval= int(sys.argv[2])
stop_time = start_time + run_time
current_time = time.time()
Detector_File= sys.argv[3]
DelayTime = int(sys.argv[4])

DetectorFile= open( Detector_File, "w",newline="")
header=['Time','Counts_Per_Minute']

DetectorWriter= csv.writer(DetectorFile)
DetectorWriter.writerow(header)
Time = []
Counts = []

time.sleep(DelayTime)

Data=0
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.IN, pull_up_down=GPIO.PUD_UP)

#GPIO.setup(17,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
def my_callback(channel):
		global Data
		Data= Data+1 
		print ("detected")
GPIO.add_event_detect(17, GPIO.FALLING, callback=my_callback)
while current_time < stop_time:
	current_time = time.time()
	Counts= Data
	data_list= [current_time, Counts]
	DetectorWriter.writerow(data_list)
	time.sleep(sleep_interval)
	
	
		

#GPIO.wait_for_edge(17, GPIO.FALLING)
GPIO.cleanup
print("Collected counts=", Data,"Counts")
DetectorFile.close()


