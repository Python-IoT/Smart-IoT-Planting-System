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
#Function of Thread Lora, waiting for the data(json) from device via LoRa-module.
def Lora(func):
  global recv
  while True:
    #Waiting for LoRa module message from uart port.
    count = ser.inWaiting()
    if count != 0:
      recv = ser.readline() #readline() need to set timeout, otherwise results block
      #put recv in quene, Thread Lora_json will deal with recv command one by one while it is free
      #hbmqtt_send(recv)  #send recv to server via MQTT
      ser.flushInput()
      print(recv)
    sleep(0.1)  
   
#Function of Thread Lora_json, parse the json from device.  
def Lora_json(func):
  global recv
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
      recv = ''
    print("This is %s. %s" % (func,ctime()))
    sleep(1)

#Function of Thread gateway_mqtt, waiting for the data(json) from server via MQTT.
#Use hbmqtt
def gateway_mqtt(func):
  while True:
    #Waiting for json from server via MQTT.    
    print('Waiting for MQTT data from server.....')
 
def mqtt_parse(func):
  while True:
    #check MQTT message appear or not
    #parse_mqtt()
    #send command to device
    #LoRa_send()
    #insert the setting data into sqlite database
    #db_operate()
    
    
def gateway_init():
  print('gateway init')
  print('check gateway database existed or not')
  print('dateway database do not exist')
  print('read gateway ID from gateway.inf')
  print('send ID to server to check gateway database backup on server or not')
  #requests.post('http://www.sips.com/gateway', data=json.dumps({'ID': '123456'}))
  print('if ID backup on server, download it, otherwise init it')
  #url = 'http://www.sips.com/gateway/123456/sips.db'
  #r = requests.get(url) 
  #with open("sips.db", "wb") as code:
  # code.write(r.content)
  print('init database......')
  
threads = []
t1 = threading.Thread(target=Lora,args=('Lora Thread',))
threads.append(t1)
t2 = threading.Thread(target=Lora_json,args=('Lora_json_parse Thread',))
threads.append(t2)
t3 = threading.Thread(target=gateway_mqtt,args=('MQTT listen Thread',))
threads.append(t3)
t4 = threading.Thread(target=mqtt_parse,args=('MQTT Parse Thread',))
threads.append(t4)
if __name__ == '__main__':
  #gateway_init()
  for t in threads:
#        t.setDaemon(True)
    t.start()
  while True:
   print("\nThis is the main thread!")
   sleep(2)
