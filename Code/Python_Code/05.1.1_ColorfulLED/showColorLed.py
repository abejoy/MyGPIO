#!/usr/bin/env python3
########################################################################
# Filename    : ColorfulLED.py
# Description : Random color change ColorfulLED
# Author      : www.freenove.com
# modification: 2019/12/27
########################################################################
import RPi.GPIO as GPIO
import time
import random
from matplotlib import colors





pins = [11, 12, 13]         # define the pins for R:11,G:12,B:13 

def setup():
    global pwmRed,pwmGreen,pwmBlue
    GPIO.setmode(GPIO.BOARD)       # use PHYSICAL GPIO Numbering
    GPIO.setup(pins, GPIO.OUT)     # set RGBLED pins to OUTPUT mode
    GPIO.output(pins, GPIO.HIGH)   # make RGBLED pins output HIGH level
    pwmRed = GPIO.PWM(pins[0], 2000)      # set PWM Frequence to 2kHz
    pwmGreen = GPIO.PWM(pins[1], 2000)  # set PWM Frequence to 2kHz
    pwmBlue = GPIO.PWM(pins[2], 2000)    # set PWM Frequence to 2kHz
    pwmRed.start(0)      # set initial Duty Cycle to 0
    pwmGreen.start(0)
    pwmBlue.start(0)

def setColor(rgb_array=[], r_val=0, g_val=0, b_val=0): # change duty cycle for three pins to r_val,g_val,b_val
    if len(rgb_array) != 3:
        pwmRed.ChangeDutyCycle(r_val)     # change pwmRed duty cycle to r_val
        pwmGreen.ChangeDutyCycle(g_val)
        pwmBlue.ChangeDutyCycle(b_val)
    else:
        pwmRed.ChangeDutyCycle(rgb_array[0])     # change pwmRed duty cycle to r_val
        pwmGreen.ChangeDutyCycle(rgb_array[1])
        pwmBlue.ChangeDutyCycle(rgb_array[2])

def set_col_name(name):
    col_name = name
    
def invert_rgb(r, g, b):
    return [100-r, 100-g, 100-b]



def loop():
    while True :
        color_val = input("enter color: ")

        color_info = colors.to_rgba(color_val)
        red_col = int(round(color_info[0]*100))
        green_col = int(round(color_info[1]*100))
        blue_col = int(round(color_info[2]*100))

        setColor(invert_rgb(red_col, green_col, blue_col))          #set random as a duty cycle value 
        print ('r=%d, g=%d, b=%d ' %(red_col, green_col, blue_col))


def destroy():
    pwmRed.stop()
    pwmGreen.stop()
    pwmBlue.stop()
    GPIO.cleanup()

def mainstuff():
    if __name__ == '__main__':     # Program entrance
        print('Program is starting ... ')
        setup()
        try:
            loop()
        except ValueError:  # if unknown color inpout
            print('Unknown Color, Try again')
            print()
            destroy()
            mainstuff()
        except KeyboardInterrupt:
            destroy()


mainstuff()

