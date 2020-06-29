import RPi.GPIO as GPIO

pins = [11, 12, 13] 

def setup():
    GPIO.setmode(GPIO.BOARD)       # use PHYSICAL GPIO Numbering
    GPIO.setup(pins, GPIO.OUT)     # set RGBLED pins to OUTPUT mode
    GPIO.output(pins, GPIO.LOW)   # make RGBLED pins output HIGH level


def loop():
	try:
		while(True):
			request = input("RGB -->")
			if(len(request) == 3):
				GPIO.output(pins[0], int(request[0]))
				GPIO.output(pins[1], int(request[1]))
				GPIO.output(pins[2], int(request[2]))
	except KeyboardInterrupt:
		GPIO.cleanup()


setup()

loop()
