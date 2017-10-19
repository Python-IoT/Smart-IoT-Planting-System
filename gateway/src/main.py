#!/usr/bin/env python
import threading
import time
 
def my_thread():
  for i in range(0, 4):
    print("\nThis is a sub thread!")
    time.sleep(1)
 
thread1 = threading.Thread(target = my_thread, args = ())
thread2 = threading.Thread(target = my_thread, args = ())
thread1.start()
thread2.start()
thread1.join()
thread2.join()
 
print("\nThis is the main thread!")
