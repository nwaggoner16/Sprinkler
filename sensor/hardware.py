#import RPi.GPIO as GPIO
import time
#import Adafruit_DHT

class Valve:
	def __init__(self, solenoid_pin, water_len = 10):
		self.solenoid_pin = solenoid_pin
		self.water_len = water_len
	# pin is a variable used to define output pin on rpi
	# measured in seconds
	def water(self):
		# startup in board mode
		GPIO.setmode(GPIO.BOARD)

		# set pin[7] to output a signal
		GPIO.setup(self.solenoid_pin, GPIO.OUT)

		# start sending trigger to relay
		GPIO.output(self.solenoid_pin,1)

		# wait however long its set
		time.sleep(self.water_len)

		# stop
		GPIO.output(self.solenoid_pin, 0)
		GPIO.cleanup()


class moisture_sensor:
	def __init__(self, moisture_pin):
		self.moisture_pin = moisture_pin
	# pin is a variable used to define output pin on rpi

	def moisture_check(self):

		# start up in board mode
		GPIO.setmode(GPIO.BOARD)

		# set pin[19] to input a signal
		GPIO.setup(self.moisture_pin, GPIO.IN)

		# listening for a signal from moisture sensor
		if GPIO.input(self.moisture_pin):
			return 1 # on
		else:
			return 0 # off
		GPIO.cleanup()

class DHT11:
	def read_dht(self):
		humidity, temperature = Adafruit_DHT.read_retry(11, 4)  # GPIO27 (BCM notation)
		#temperature = temperature * 9/5 + 32
		return humidity, temperature

#Creating class for photoresistor
class Photoresistor:
	pin = 'x'
	#Creating function to return light level from photoresistor, taking gpio pin number as input.
	def return_light_level(self):
	    count = 0

	    #Output on the pin for
	    GPIO.setup(self.pin, GPIO.OUT)
	    GPIO.output(self.pin, GPIO.LOW)
	    time.sleep(0.1)

	    #Change the pin back to input
	    GPIO.setup(self.pin, GPIO.IN)

	    #Count until the pin goes high
	    while (GPIO.input(self.pin) == GPIO.LOW):
	        count += 1

	    return count

def cleanup():
	GPIO.cleanup()

class L298n:
	def __init__(self, ena_pin, in1_pin, in2_pin, speed, run_time):
		self.ena_pin = ena_pin
		self.in1_pin = in1_pin
		self.in2_pin = in2_pin
		self.speed = speed
		self.run_time = run_time
	def run_pump(self):
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(self.ena_pin, GPIO.OUT)
		GPIO.setup(self.in1_pin, GPIO.OUT)
		GPIO.setup(self.in2_pin, GPIO.OUT)
		GPIO.output(self.in1_pin, GPIO.LOW)
		GPIO.output(self.in2_pin, GPIO.LOW)
		pump = GPIO.PWM(self.ena_pin, 1000)
		pump.start(self.speed)
		GPIO.output(self.in1_pin, GPIO.HIGH)
		time.sleep(self.run_time)
		GPIO.output(self.in1_pin, GPIO.LOW)
		GPIO.cleanup()
