#!/usr/bin/env python
#In this project, I use a RS360 micro water pump which is drived by relay,
#the realy's open/close status define start/stop water. 
#Use steering enging to rotate the waterpipe so as to extend the irrigation field.

#Steering engine pin connection:
#deep red <--> GND
#red      <--> VCC
#yellow   <--> signal(X1)


#Water pump(RS360) is powered by 5V power.
#Realy connect to GPIO(X2).
import pyb
from pyb import Servo
from pyb import Pin
servo=Servo(1) # X1
pin_out = Pin('X2', Pin.OUT_PP)

def irrigate_start():
  pin_out.high()
  
def irrigate_stop():
  pin_out.low()

def irrigate_rotate(angle):
  servo.angle(angle)
  

  
