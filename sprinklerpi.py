import os
import sys
sys.path.append("home/pi/gardensystem")
import hardware as hw
import RPi.GPIO as GPIO



import ConfigParser
#import MySQLdb as mysql
import io
import json

#Import and parse pinout.ini for sensor pins
pinout = "pinout.ini"
with open(pinout) as f:
    pin_config = f.read()
config = ConfigParser.RawConfigParser(allow_no_value=True)
config.readfp(io.BytesIO(pin_config))

#Assign pin numbers to variables
phr = int(config.get('pinout','photoresistor'))
dht = int(config.get('pinout','dht11'))
ms = int(config.get('pinout','moisture_sensor'))
#Create pump object using L298n class from hardware
ena=int(config.get('L298n','ena'))
in1=int(config.get('L298n','in1'))
in2=int(config.get('L298n','in2'))
speed=int(config.get('L298n','speed'))
run_time=int(config.get('L298n','run_time'))
pump = hw.L298n(ena, in1, in2, speed, run_time)

pump.run_pump()

#Run
#moisture = hw.moisture_check(ms);

#if (moisture == 0):
