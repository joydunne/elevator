
from gpiozero import Button
import time

buttonOne= Button(2)
buttonTwo= Button(3)
while True:
    if buttonOne.is_pressed:
        print("Button One is pressed")
    if buttonTwo.is_pressed:
        print("Button Two is pressed")
