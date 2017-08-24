#!/usr/bin/env python
#Light control module.
#Use led on board simulate the bulb.
#Usr can turn on & turn off the led, besides, they can control lightness of led.  
#Because succulent need to be shined regularly.
def Turn_On(num):
  light=LED(num)
  light.On()

def Turn_Off(num):
  light=LED(num)
  light.Off()
 
#Adjust lightness of led.
def Lightness(par):
  pwm_control
