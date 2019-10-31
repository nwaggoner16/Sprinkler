import sys
sys.path.append("home/pi/gardensystem")
import hardware as hw
import RPi.GPIO as GPIO
import Adafruit_DHT
import time
import os
import ConfigParser
#import MySQLdb as mysql
import io
import json

#Import and parse pinout.ini for sensor pins
configfile_name = "pinout.ini"
with open("pinout.ini") as f:
    sample_config = f.read()
config = ConfigParser.RawConfigParser(allow_no_value=True)
config.readfp(io.BytesIO(sample_config))

#Assign pin numbers to variables
phr = int(config.get('pinout','photoresistor'))
dht = int(config.get('pinout','dht11'))
ms = int(config.get('pinout','moisture_sensor'))

def rc_time(phr):
    count = 0

    #Output on the pin for
    GPIO.setup(phr, GPIO.OUT)
    GPIO.output(phr, GPIO.LOW)
    time.sleep(0.1)

    #Change the pin back to input
    GPIO.setup(phr, GPIO.IN)

    #Count until the pin goes high
    while (GPIO.input(phr) == GPIO.LOW):
        count += 1

    return count
