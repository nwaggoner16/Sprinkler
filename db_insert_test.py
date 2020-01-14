#!/usr/bin/python
import mysql.connector as mariadb

mysql = mariadb.connect(user='root', password='P3r$3ph0n3', database='Plant_logger')
cursor = mysql.cursor()
cursor.execute('insert into sensor_data values (now(), 1,2,1,1,1)');
mysql.commit()
data = cursor.execute('Select * from sensor_data;')
print(data)
