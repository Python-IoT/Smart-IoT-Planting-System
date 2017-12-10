#!/usr/bin/env python
import threading, time
import queue
q = queue.Queue()

def Producer():
  n = 0
  while n < 5:
    n += 1
    q.put(n)
    print('Producer has created %s' % n)
    time.sleep(0.1)
def Consumer():
  count = 0
  while count < 5:
    count += 1
    data = q.get()
    print('Consumer has used %s' % data)
    time.sleep(0.2)

p = threading.Thread(target = Producer, name='')
c = threading.Thread(target = Consumer, name='')
