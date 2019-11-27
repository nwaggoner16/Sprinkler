import RPi.GPIO as GPIO

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
