import RPi.GPIO as GPIO
import time

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
        GPIO.cleanup()

def rc_time(self):
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
	
def cleanup():
	GPIO.cleanup()
