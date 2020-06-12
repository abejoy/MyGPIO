import RPi.GPIO as GPIO
import time
import tkinter as tk

ledPin = 11
lightstatus = False
root = tk.Tk()
btn_text = tk.StringVar()


def setup():
    GPIO.setmode(GPIO.BOARD)       # use PHYSICAL GPIO Numbering
    GPIO.setup(ledPin, GPIO.OUT)   # set the ledPin to OUTPUT mode
    GPIO.output(ledPin, GPIO.LOW)  # make ledPin output LOW level 
    print ('using pin%d'%ledPin)

def show_button():
	print("clicked")
	global lightstatus
	lightstatus = not lightstatus
	GPIO.output(ledPin, lightstatus)
	btn_text.set(get_text())
	
	
def quit_program():
    GPIO.cleanup() 
    quit()
	
def get_text():
    return "Turn Off" if lightstatus else "Turn On"
	
setup()
print('i get herer')

frame = tk.Frame(root)
frame.pack()
button = tk.Button(frame, text=btn_text, command=show_button)
button.pack()

quitButton = tk.Button(frame, text="Quit", fg="red", command=quit_program)
quitButton.pack()

root.mainloop()


	
