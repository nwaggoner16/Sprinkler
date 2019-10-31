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
GPIO.setmode(GPIO.BOARD)

#Assign pin numbers to variables
phr = int(config.get('pinout','photoresistor'))
dht = int(config.get('pinout','dht11'))
ms = int(config.get('pinout','moisture_sensor'))


hw.rc_time(phr);
hw.cleanup();
