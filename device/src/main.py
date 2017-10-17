#This is the file executing while STM32 MCU bootup, and in this file,  
#it will call other functions to fullfill the project.
#Communication module: LoRa.
#Communication method with gateway via LoRa.
#Uart port drive LoRa module.
#Parse JSON between device and gateway via LoRa channel.
#LoRa module: E32-TTL-100
#Pin specification:
#Module         MCU
#M0(IN)    <--> GPIO(Y3)(OUT)     #mode setting, can not hang
#M1(IN)    <--> GPIO(Y4)(OUT)     #mode setting, can not hang
#RXD(IN)   <--> Y1(TX)(OUT)   #UART6
#TXD(OUT)  <--> Y2(RX)(IN)    #UART6
#AUX(OUT)  <--> GPIO/INT(IN)  #module status detecting
#VCC
#GND
#Communication mode is 0, need to set M0 and M1 to 0.

import pyb
from pyb import Pin
from pyb import Timer
from pyb import UART  
import micropython
import irrigate
#Import light intensity needed module 
import LightIntensity
import moisture
import rainfall
import WaterLevel
import security
import time
import json

micropython.alloc_emergency_exception_buf(100)

Pin('Y11',Pin.OUT_PP).low() #GND
Pin('Y9',Pin.OUT_PP).high() #VCC

#Set LoRa module with mode-0.
M0 = Pin('Y3', Pin.OUT_PP)
M1 = Pin('Y4', Pin.OUT_PP)
M0.low()
M1.low()
#Init uart4 for LoRa module.
lora_uart = UART(6,9600)  
lora_uart.init(9600, bits=8, parity=None, stop=1)  
#Send Online command to gateway while it power on to obtain its status data from gateway's database.
#lora_uart.write('{"ID":"1", "CMD":"Online", "TYPE":"N", "VALUE":"N"}\n')
#time.sleep(1)
#lora_uart.write('{"ID":"1", "CMD":"ENV", "TYPE":"moisture", "VALUE":"1800"}\n')	
#LED shining regularly(using timer) to indicate the program is running correctly
tim1 = Timer(1, freq=1)
tim1.callback(lambda t: pyb.LED(1).toggle())

 
#Read the light intensity value from sensor regularly.

lightVlaue = 0
#time2 callback function, obtain value from light intensity sensor and send it to gateway via LoRa module.
#Warning: interruput function can not execute complex task suck print(), otherwise it will execute only one time and die.
def getLightInten():
  global lightValue
#  lightValue = LightIntensity.readLight()
#  #print(lightValue)
#  lora_uart.write('{"ID":"1", "CMD":"ENV", "TYPE":"light", "VALUE":"+lightValue+"}\n')
#  lora_uart.write('{"ID":"1", "CMD":"ENV", "TYPE":"moisture", "VALUE":"1800"}\n')
	
'''
#Get soil moisture and send it to gateway, if the current value is lower than standard, gateway
#will send 'irrigate' command to device, device will control steering engine to open the tap and water the plants.
def moisture():
  global moisture
  moisture = moisture.readMoisture()
  lora_uart.write('{"ID":"1", "CMD":"ENV", "TYPE":"moisture", "VALUE":"+moisture+"}\n')
'''	

#tim2 = Timer(2, freq=1)
#tim2.callback(getLightInten())

if __name__=='__main__':
  while True:
    print('------------------------------------')
	
    print('1. Light Intensity:')
    lightValue = LightIntensity.readLight()
    print(lightValue)
    print('')
	
    if lightValue > 1000:
      irrigate.irrigate_start() 
    else:
      irrigate.irrigate_stop()
    
    print('2. Soil Moisture:')
    #Python func call need to (), otherwise : function getMoisAo at 0x20003d20
    print(moisture.getMoisAo())	
    print('')
	
    print('3. Security Status:')
    print(security.detectMotion())	
    print('')
	
    print('4. Rainfall:')
    print(rainfall.getRainAo())	
    print('')

    print('5. WaterLevel:')
    print(WaterLevel.getWaterLevel())	
    print('')
	
    time.sleep(3)
	
	
'''
    #Waiting for the message from UART4 to obtain LoRa data.
    len = lora_uart.any()
    if(len > 0): 
      recv = lora_uart.read()
      print(recv)
      json_lora = json.loads(recv)
      #Parse JSON from gateway.
      if (json_lora.get("CMD") == 'Online' and json_lora.get("TYPE") == 'Light2' ): #Control the light(led on TPYBoard)
        print('light2')
        if json_lora.get("VALUE") == 'On':
          pyb.LED(2).on()
 #         lora_uart.write('{"ID":"1", "CMD":"ENV", "TYPE":"moisture", "VALUE":"1800"}\n')		  
        else:
          pyb.LED(2).off()
      elif json_lora.get("CMD") == 'irrigate': # irrigate the plants
        if json_lora.get("VALUE") == 'Open':
          irrigate.irrigate_start()
        else:
          irrigate.irrigate_stop()
'''	
