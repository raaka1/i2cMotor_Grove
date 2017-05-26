#!/usr/bin/env python
#

import i2c_driver
import time

from sklearn import linear_model
from lcd_driver import *

setRGB(0, 255, 255)




try:
	# You can initialize with a different address too: grove_i2c_motor_driver.motor_driver(address=0x0a)
	m= i2c_driver.motor_driver()

	#FORWARD
	print("Forward")
	setText("System Cooling")
	m.MotorSpeedSetAB(100,100)	#defines the speed of motor 1 and motor 2;
	m.MotorDirectionSet(0b1010)	#"0b1010" defines the output polarity, "10" means the M+ is "positive" while the M- is "negtive"
	ltime = 340
	time.sleep(ltime)



	#STOP
	print("Stop")
	setText("Stop")
	m.MotorSpeedSetAB(0,0)
	time.sleep(1)

	#Increase speed
	for i in range (100):
		print("Speed:",i)
		m.MotorSpeedSetAB(i,i)
		time.sleep(.02)

	print("Stop")
	m.MotorSpeedSetAB(0,0)
	setRGB(255, 255, 255)

except IOError:
	print("Unable to find the motor driver, check the addrees and press reset on the motor driver and try again")
