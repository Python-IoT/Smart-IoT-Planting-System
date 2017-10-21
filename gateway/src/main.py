#!/usr/bin/env python
#### /usr/bin/python3.4
#Communicate with end devices via LoRa.
#Communicate with server via MQTT(hbmqtt) and HTTP POST.
#Save data in the sqlite database.
#Parse JSON from MQTT and LoRa protocol.

#Communication module: LoRa.
#Communication method with device via LoRa.
#Uart port drive LoRa module.
#Parse JSON between device and gateway via LoRa channel.
#LoRa module: E32-TTL-100
#Pin specification:
#M0    <--> GPIO(OUT)     #mode setting  connct to GND is OK!(Low)
#M1    <--> GPIO(OUT)     #mode setting  connct to GND is OK!(Low)
#RXD   <--> 8(TXD)        #ttyS0
#TXD   <--> 10(RXD)       #ttyS0
#AUX   <--> GPIO/INT(IN)  #module status detecting
#VCC
#GND

#You need to install pyserial manually, install command is below:
#pip install pyserial(Python2)
#pip3 install pyserial(Python3)

import serial
import time
import json
#ser  = serial.Serial("/dev/ttyS0", 9600)
ser  = serial.Serial("/dev/ttyS0", 9600, timeout=0.2)
import threading
from time import ctime,sleep
recv = ''
def Lora(func):
  while True:
    #Waiting for LoRa module message from uart port.
    count = ser.inWaiting()
    if count != 0:
      recv = ser.readline() #readline() need to set timeout, otherwise results block
      ser.flushInput()
      print(recv)
    sleep(0.1)  
        
def Lora_json(func):
  while True:
    if recv.strip()=='':
      print('recv is empty')
    else:
      json_lora = json.loads(bytes.decode(recv))
      #Parse JSON
      #print(json_lora.get("ID"))
      #print(json_lora["ID"])
      #if json_lora.get("ID") == '1' : #Device ID-1 existed in gateway database
      if int(json_lora.get("ID")) == 1 : #Device ID-1 existed in gateway database
        if json_lora.get("CMD") == 'Online':
          response = '{"ID":"1", "CMD":"Online", "TYPE":"Light2", "VALUE":"On"}'
          print(response)
        elif json_lora.get("CMD") == 'Env':
          if json_lora.get("TYPE") == 'moisture':
            if int(json_lora.get("VALUE")) < 2000: # soil moisture is lower than standard
              response = '{"ID":"1", "CMD":"irrigate", "TYPE":"Open", "VALUE":"100"}'
        ser.write(str.encode(response))
      else:
        print('init_device')
        #init_device()  #Create sqlite table for device 1.
      
    print("This is %s. %s" % (func,ctime()))
    sleep(1)

threads = []
t1 = threading.Thread(target=Lora,args=('Lora Thread',))
threads.append(t1)
t2 = threading.Thread(target=Lora_json,args=('Lora_json_parse Thread',))
threads.append(t2)

if __name__ == '__main__':
  for t in threads:
#        t.setDaemon(True)
    t.start()
  while True:
   print("\nThis is the main thread!")
   sleep(2)
