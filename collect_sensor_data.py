from mcp3008 import cap_moisture_sensor

moisture_sensor1 = cap_moisture_sensor(0)

print(moisture_sensor1.cap_moisture_level())
