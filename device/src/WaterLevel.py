#Water level sensor.
#VCC 
#GND
#AO <--> ADC Port(A7) Analog data

#AO is the specific value.

import pyb
from pyb import Pin

adc = pyb.ADC(Pin('A7'))       # create an analog object from a pin
adc = pyb.ADC(pyb.Pin.board.A7)
# read an analog value
def getWaterLevel():               
  print('WaterLevel Ao')
  return adc.read()
