import RPi.GPIO as GPIO
import time

ledPin = 11
buttonPin = 12

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def blink(x:int):
    print("blinking")
    for i in range(x):
        GPIO.output(ledPin, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(ledPin, GPIO.LOW)
        time.sleep(0.5)

def loop():
    while True:
        if GPIO.input(buttonPin) == GPIO.HIGH :
            blink(5)

def destroy():
    GPIO.output(ledPin, GPIO.LOW)     # turn off led
    GPIO.cleanup()


print("Program is starting")
setup()
try:
    loop()
except KeyboardInterrupt:
    destroy()
