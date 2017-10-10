#This is the file executing while STM32 MCU bootup, and in this file,  
#it will call other functions to fullfill the project.
import pyb
from pyb import Pin
from pyb import Timer
import micropython

#Import light intensity needed module 
import LightIntensity
import time

micropython.alloc_emergency_exception_buf(100)

print('pin init')
Pin('Y11',Pin.OUT_PP).low() #GND
Pin('Y9',Pin.OUT_PP).high() #VCC

#LED shining regularly(using timer) to indicate the program is running correctly
tim1 = Timer(1, freq=1)
tim1.callback(lambda t: pyb.LED(1).toggle())
 
if __name__=='__main__':
  while True:
    print('Smart IoT Plant System-Device')
    print(LightIntensity.readLight())
    time.sleep(2)

 
 #send on-line message to gateway to notifiy and obtain own data from gateway's database

  
###reference begin###
"""
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
 ###reference end###
 """
"""
Waiting for LoRa message from gateway.
from pyb import UART
u4 = UART(4,9600)  
u4.init(9600, bits=8, parity=None, stop=1)  
while True:
    if(u4.any() > 0):
        print('reading....')
        receive = u4.read()
        print(receive)
        u4.write(receive)	
  
"""
