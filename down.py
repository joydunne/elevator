from motorU import *
windowMotor = motorU()
for i in range (4):
	windowMotor.rotate(direction = "counterClockwise")
windowMotor.cleanup()
