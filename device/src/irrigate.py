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

from pyb import Servo
servo=Servo(1) # X1

def irrigate_start():
  servo.angle(90)
  
def irrigate_stop():
  servo.angle(0)

def irrigate_rotate(angle):
  servo.angle(angle)
  

  
