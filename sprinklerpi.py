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
pump = hw.l298n()
pump.ena_pin = 22
pump.in1_pin = 18
pump.in2_pin = 16
pump.speed = 25
pump.run_time = 5
run_pump()

#Run
#moisture = hw.moisture_check(ms);

#if (moisture == 0):
