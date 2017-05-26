#!/usr/bin/env python
#

import i2c_driver
import time

from sklearn import linear_model
from lcd_driver import *


def cool():
	setRGB(50, 205, 50)
	#setText("")
	for i in range (0,100,99):
	    print(i)
	    m.MotorSpeedSetAB(i,i)
	    time.sleep(30)#
	    setText("Cooling")




try:
	# You can initialize with a different address too: grove_i2c_motor_driver.motor_driver(address=0x0a)
	m= i2c_driver.motor_driver()

	#Increase speed
	for i in range(10):
		print("Loop count",i)
		n = repr(i)
		setText("loop count: "+ n)
		cool()


	setText("Clear")
	m.MotorSpeedSetAB(0,0)
	setRGB(255, 255, 255)

except IOError:
	print("Unable to find the motor driver, check the addrees and press reset on the motor driver and try again")
