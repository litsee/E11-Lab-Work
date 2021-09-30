import RPi.GPIO as GPIO
import time
import datetime
from time import sleep 


Data=0
GPIO.setmode(GPIO.BCM)
def my_callback(channel):
	global Data
	Data= Data+1
	print(Data)
		
GPIO.setup(17,GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.setup(17,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(17, GPIO.FALLING, callback=my_callback)
#GPIO.wait_for_edge(17, GPIO.FALLING)
sleep(30)
GPIO.cleanup
print("Collected counts=", Data,"Counts")



