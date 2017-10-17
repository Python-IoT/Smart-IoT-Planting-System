#!/usr/bin/env python
#receive signal from infrared sensor
#Sensor: HC-SR501
#VCC 
#Signal <--> GPIO(IN) Y8
#GND
import pyb
from pyb import Pin
motion_detect = Pin('Y8',Pin.IN,Pin.PULL_UP)
#if motion sensor value is 1, otherwise 0.
def detectMotion():
  print('in security module')
  return motion_detect.value()

