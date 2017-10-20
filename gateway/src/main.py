#!/usr/bin/env python
import threading
from time import ctime,sleep

def Lora(func):
  while True:
    print("This is %s. %s" % (func,ctime()))
    sleep(1)

def Lora_json(func):
  while True:
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
