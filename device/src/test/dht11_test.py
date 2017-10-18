
import pyb
from pyb import Pin
from pyb import Timer  
import micropython
import time
from DHT11 import DHT11

micropython.alloc_emergency_exception_buf(100)

#LED shining regularly(using timer) to indicate the program is running correctly
tim1 = Timer(1, freq=1)
tim1.callback(lambda t: pyb.LED(1).toggle())

if __name__=='__main__':
  S=DHT11('X8')
  while True:
    print('------------------------------------')
	
    print('Temperature & Humidity:')
#    S=DHT11('X8')
    temp,hum = S.read_temp_hum()
    print('Temperature:')
    print(temp)
    print('Humidity:')
    print(hum)	
    print('')
    time.sleep(3)
	
	
