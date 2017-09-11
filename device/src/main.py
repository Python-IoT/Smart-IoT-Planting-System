#This is the file executing while STM32 MCU bootup, and in this file,  
#it will call other functions to fullfill the project.
import pyb
from pyb import Pin
from ds18x20 import DS18X20
from pyb import Timer
import micropython

micropython.alloc_emergency_exception_buf(100)
tempValue = 0
print('pin init')
Pin('Y11',Pin.OUT_PP).low() #GND
Pin('Y9',Pin.OUT_PP).high() #VCC

def displayTemp(t):
 print('Current Temperature:')
 print(tempValue)
 
tim1 = Timer(1)
tim1.callback(displayTemp)
tim1.init(freq=1/5)
 
if __name__=='__main__':
 print('Smart IoT Plant System')
 DQ=DS18X20(Pin('Y10')) #DQ
 while True:
  tempValue = DQ.read_temp()
  
  
###reference###
import pyb
from pyb import Pin
from ds18x20 import DS18X20
from pyb import Timer
import micropython

micropython.alloc_emergency_exception_buf(100)
tempValue = 0
print('pin init')
Pin('Y11',Pin.OUT_PP).low() #GND
Pin('Y9',Pin.OUT_PP).high() #VCC

def displayTemp(t):
 print('Current Temperature:')
 print(tempValue)
 
tim1 = Timer(1)
tim1.callback(displayTemp)
tim1.init(freq=1/5)
 
if __name__=='__main__':
 print('Smart IoT Plant System')
 DQ=DS18X20(Pin('Y10')) #DQ
 while True:
  tempValue = DQ.read_temp()
 ### 
