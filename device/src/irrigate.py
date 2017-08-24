#!/usr/bin/env python
#In this project, I use a servo to simulate the water tap.
#Roating to 90 angle suggest that the water tap is open, and 0 angle means close.
from pyb import Servo
servo=Servo(1) # X1
def irrigate_start():
  servo.angle(90)
  
def irrigate_stop():
  servo.angle(0)
  
