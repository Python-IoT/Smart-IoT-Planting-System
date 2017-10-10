#This is the file executing while STM32 MCU bootup, and in this file,  
#it will call other functions to fullfill the project.
#Communication module: LoRa.
#Communication method with gateway via LoRa.
#Uart port drive LoRa module.
#Parse JSON between device and gateway via LoRa channel.
#LoRa module: E32-TTL-100
#Pin specification:
#Module         MCU
#M0(IN)    <--> GPIO(X3)(OUT)     #mode setting, can not hang
#M1(IN)    <--> GPIO(X4)(OUT)     #mode setting, can not hang
#RXD(IN)   <--> X1(TX)(OUT)   #UART4
#TXD(OUT)  <--> X2(RX)(IN)    #UART4
#AUX(OUT)  <--> GPIO/INT(IN)  #module status detecting
#VCC
#GND
#Communication mode is 0, need to set M0 and M1 to 0.

import pyb
from pyb import Pin
from pyb import Timer
from pyb import UART  
import micropython

#Import light intensity needed module 
import LightIntensity
import time

micropython.alloc_emergency_exception_buf(100)

print('pin init')
Pin('Y11',Pin.OUT_PP).low() #GND
Pin('Y9',Pin.OUT_PP).high() #VCC

#Set LoRa module with mode-0.
M0 = Pin('X3', Pin.OUT_PP)
M1 = Pin('X4', Pin.OUT_PP)
M0.low()
M1.low()
#Init uart4 for LoRa module.
u4 = UART(4,9600)  
u4.init(9600, bits=8, parity=None, stop=1)  
cmd_online = '{"ID":1, "CMD":Online, "TYPE":"N", "VALUE":"N"}'
u4.write(cmd_online)



#LED shining regularly(using timer) to indicate the program is running correctly
tim1 = Timer(1, freq=1)
tim1.callback(lambda t: pyb.LED(1).toggle())
 
if __name__=='__main__':
  while True:
    #Waiting for the message from UART4 to obtain LoRa data.
    len = u4.any()
    if(len > 0): 
      print(u4.read())

 
