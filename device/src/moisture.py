#soil moisture sensor.
#VCC 
#GND
#DO <--> GPIO(Y12)  Digital data
#AO <--> ADC Port(Y11) Analog data
#if value is low than defined data, DO value is 0, 
#if value is high than defined data, DO value is 1.
#AO is the specific value.
#Sensor value reference:
#0 ~300 : dry soil
#300~700 : wet soil 
#700~950 : in water
import pyb
from pyb import Pin
p_in = Pin('Y12', Pin.IN, Pin.PULL_UP)
p_in.value


adc = pyb.ADC(Pin('Y11'))       # create an analog object from a pin
adc = pyb.ADC(pyb.Pin.board.Y11)
# read an analog value
def getMoisAo():               
  print('moisture Ao')
  return adc.read()

# read an digital value
def getMoisDo():             
  print('moisture Do')
  return p_in.value
