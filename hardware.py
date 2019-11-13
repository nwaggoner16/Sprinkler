import RPi.GPIO as GPIO
import time
import Adafruit_DHT

class Valve:
	# pin is a variable used to define output pin on rpi
	pin = 'x'
	# measured in seconds
	water_len = 10

	def water(self):
		# startup in board mode
		GPIO.setmode(GPIO.BOARD)

		# set pin[7] to output a signal
		GPIO.setup(self.pin, GPIO.OUT)

		# start sending trigger to relay
		GPIO.output(self.pin,1)

		# wait however long its set
		time.sleep(self.water_len)

		# stop
		GPIO.output(self.pin, 0)
        GPIO.cleanup()


class moisture_sensor:
	# pin is a variable used to define output pin on rpi
	pin = 'x'

	def moisture_check(self):

		# start up in board mode
		GPIO.setmode(GPIO.BOARD)

		# set pin[19] to input a signal
		GPIO.setup(self.pin, GPIO.IN)

		# listening for a signal from moisture sensor
		if GPIO.input(self.pin):
			return 1 # on
		else:
			return 0 # off
        GPIO.cleanup();

class DHT11:
	humidity, temperature = Adafruit_DHT.read_retry(11, 27)  # GPIO27 (BCM notation)
	temperature = temperature * 9/5 + 32

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
	ena_pin = 'x'
	in1_pin = 'x'
	in2_pin = 'x'
	speed = 'x'
	run_time = 5
	def run_pump(self):
		GPIO.setup(self.ena_pin, GPIO.OUT)
		GPIO.setup(self.in1_pin, GPIO.OUT)
		GPIO.setup(self.in2_pin, GPIO.OUT)
		GPIO.output(self.in1_pin, GPIO.LOW)
		GPIO.output(self.in2_pin, GPIO.LOW)
		pump = GPIO.PWM(ena_pin, 1000)
		pump.start(speed)
		GPIO.output(self.in1_pin, GPIO.HIGH)
		time.sleep(run_time)
		GPIO.output(self.in1_pin, GPIO.LOW)
		break
