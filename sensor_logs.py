#!/usr/bin/python
import mysql.connector as mariadb
import serial
from time import sleep
from datetime import datetime as dt

mysql = mariadb.connect(user='root', password='P3r$3ph0n3', database='Plant_logger')
cursor = mysql.cursor()

ser = serial.Serial('/dev/ttyACM0',9600)
serial_list = []
temperature = 0
humidity = 0
light = 0
soil_temperature = 0
soil_moisture = 0
moisture_sum = 0
avg_daily_moisture = 0
water_if_below = 55
current_time = dt.now()
water_time = 20
while('start' not in serial_list and 'end' not in serial_list):
	read_serial=ser.readline()
	read_serial = str(read_serial)
	serial_list = read_serial.split(',');
		

temperature = float(serial_list[1]) * 9/5 +32
humidity = serial_list[2]
light = serial_list[3]
soil_temperature = serial_list[4]
soil_moisture = serial_list[5]
cursor.execute('insert into sensor_data (log_time, temperature, humidity, light, soil_temperature, soil_moisture) values (now(), {},{},{},{},{})'.format(temperature, humidity, light, soil_temperature, soil_moisture));

cursor.execute("select soil_moisture from Plant_logger.sensor_data order by log_time desc limit 24;")
for soil_moisture in cursor:
	moisture_sum += soil_moisture[0]

avg_daily_moisture = moisture_sum/24


if avg_daily_moisture < water_if_below and current_time.hour == water_time:
        ser.write('1') # Sending data to the Arduino
        sleep(5)
        avg_daily_moisture = 100
        
if avg_daily_moisture == 100:
        ser.write('0')
	
mysql.commit()
print(avg_daily_moisture)

