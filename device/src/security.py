#!/usr/bin/env python
#receive signal from infrared sensor
#Sensor: HC-SR501
#VCC, Signal <--> GPIO Y12, GND
from pyb import Pin
motion_detect = Pin('Y12',Pin.IN,Pin,PULL_UP)
if(motion_detect.value() == 1):
  print('alarm')
