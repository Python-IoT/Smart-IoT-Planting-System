#!/usr/bin/env python
import threading, time
import queue
q = queue.Queue()

def Producer():
  n = 0
  while n < 1000:
    n += 1
    q.put(n)
#    print('Producer has created %s' % n)
#    time.sleep(0.1)
def Consumer():
  count = 0
  while count < 1000:
    count += 1
    data = q.get()
#    print('Consumer has used %s' % data)
#    time.sleep(0.2)

p = threading.Thread(target = Producer, name='')
c = threading.Thread(target = Consumer, name='')

import serial
import time
import json
import threading
from time import ctime,sleep
import queue
q = queue.Queue()
#ser  = serial.Serial("/dev/ttyS0", 9600)
ser  = serial.Serial("/dev/ttyS0", 9600, timeout=0.2)
recv = ''
def Lora(func):
  global recv
  while True:
    #Waiting for LoRa module message from uart port.
    count = ser.inWaiting()
    if count != 0:
      recv = ser.readline() #readline() need to set timeout, otherwise results block
      ser.flushInput()
      q.put(recv.decode())
      print(recv.decode())
    sleep(0.1)

def Lora_json(func):
  global recv
  while True:
    if q.empty():
      pass
    else:
      print(q.qsize())
      data = q.get()
#      json_lora = json.loads(bytes.decode(recv))
      json_lora = json.loads(data)
      #Parse JSON
      #print(json_lora.get("ID"))
      #print(json_lora["ID"])
      #if json_lora.get("ID") == '1' : #Device ID-1 existed in gateway database
      if int(json_lora.get("ID")) == 1 : #Device ID-1 existed in gateway database
        if json_lora.get("CMD") == 'Online':
          response = '{"ID":"1", "CMD":"Online", "TYPE":"Light2", "VALUE":"On"}'
          print(response.encode())
        elif json_lora.get("CMD") == 'Env':
          if json_lora.get("TYPE") == 'moisture':
            if int(json_lora.get("VALUE")) < 2000: # soil moisture is lower than standard
              response = '{"ID":"1", "CMD":"irrigate", "TYPE":"Open", "VALUE":"100"}'
        ser.write(str.encode(response))
      else:
        print('init_device')
        #init_device()  #Create sqlite table for device 1.
      recv = ''
    #print("This is %s. %s" % (func,ctime()))
    sleep(1)

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

if __name__ == '__main__':
  gateway_init()
  for t in threads:
#        t.setDaemon(True)
    t.start()
  while True:
   #print("\nThis is the main thread!")
   sleep(2)
