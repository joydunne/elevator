
from gpiozero import Button
import time
from motorU import *
elevatorMotor = motorU()
pos = "down"
buttonOne= Button(2)
buttonTwo= Button(3)
while True:
    time.sleep (0.5)
    if buttonOne.is_pressed:
        print("Button One is pressed")
        if pos == "down":
            pos = "up"
            for i in range (4):
        	       elevatorMotor.rotate()
    if buttonTwo.is_pressed:
        print("Button Two is pressed")
        if pos == "up":
            pos = "down"
            for i in range (4):
        	       elevatorMotor.rotate(direction = "counterClockwise")
