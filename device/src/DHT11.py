import pyb
from pyb import UART
from pyb import Pin
import time
class DHT11:
    def __init__(self,pin_):
        self.PinName=pin_
        time.sleep(1)
        self.gpio_pin = Pin(pin_, Pin.OUT_PP)
#        pyb.delay(10)
    def read_temp_hum(self):
        data=[]
        j=0
        gpio_pin=self.gpio_pin
        gpio_pin = Pin(self.PinName, Pin.OUT_PP) # can not ignore
        gpio_pin.low()
        time.sleep(0.018)
        gpio_pin.high()
        #wait to response
        gpio_pin = Pin(self.PinName,Pin.IN)
        while gpio_pin.value()==1:
            continue
        while gpio_pin.value()==0:
            continue
        while gpio_pin.value()==1:
                continue
        #get data
        while j<40:
            k=0
            while gpio_pin.value()==0:
                continue
            while gpio_pin.value()==1:
                k+=1
                if k>100:break
            if k<3:
                data.append(0)
            else:
                data.append(1)
            j=j+1
        j=0
		
        humidity_bit=data[0:8]
        humidity_point_bit=data[8:16]
        temperature_bit=data[16:24]
        temperature_point_bit=data[24:32]
        check_bit=data[32:40]
        humidity=0
        humidity_point=0
        temperature=0
        temperature_point=0
        check=0
        temp_negative=0

#        data[24] = 1
#        print(data[24:32])

#means temperature value is negative,set data[24] with 0 to ignore it.
        if data[24] == 1:  
            data[24] = 0
#            print(data[24:32])
            temp_negative = 1
        for i in range(8):
            humidity+=humidity_bit[i]*2**(7-i)
            humidity_point+=humidity_point_bit[i]*2**(7-i)
            temperature+=temperature_bit[i]*2**(7-i)
            temperature_point+=temperature_point_bit[i]*2**(7-i)
            check+=check_bit[i]*2**(7-i)
        tmp=humidity+humidity_point+temperature+temperature_point
        if check==tmp:
            if temp_negative == 1:
              return -(temperature+temperature_point/10),humidity+humidity_point/10
              temp_negative = 0
            else:
              return temperature+temperature_point/10,humidity+humidity_point/10
        else:
            print('checksum ERROR')
            return 0,0
