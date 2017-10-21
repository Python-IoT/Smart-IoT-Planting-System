#!/usr/bin/env python
#0:0:07 everyday upload gateway.db to server to backup
import time
from datetime import datetime, timedelta
from time import sleep
import requests
SECONDS_PER_DAY = 24 * 60 * 60

def doFunc():
  import requests
 
  url = 'http://www.sips/gateway/123456/upload'
  files = {'file': open('/home/sips/123456/gateway.db', 'rb')}
  #files = {'file': ('report.jpg', open('/home/lyb/sjzl.mpg', 'rb'))}      
  r = requests.post(url, files=files)
  print(r.text)  
  print('upload gateway.db to server...')

def doFirst():
  curTime = datetime.now()
  print(curTime)
  desTime = curTime.replace(hour=0, minute=0, second=7, microsecond=0) #0:0:07
  print(desTime)
  delta = desTime-curTime
  sleeptime = delta.total_seconds()
  print("Now day must sleep %d seconds" % sleeptime)
  sleep(sleeptime)
  doFunc()

if __name__ == "__main__":
  doFirst()
