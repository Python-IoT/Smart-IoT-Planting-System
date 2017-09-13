#!/usr/bin/env python
#Weather station.
#detect environment information from several sensors:
#water leverl, air humity, raining, air temperature, light sensitivity.
#Air temperature&humity sensor: DHT11.
#Add dht.py in micropython/stmhal/modules， refer to esp8266
#Compile the DHT in firmware, then use DHT lib in application.
#Raining, same to soil moisture.
#Raining ? DO value: 0 
from pyb import Pin
p_in = Pin('Y12', Pin.IN, Pin.PULL_UP)
p_in.value


adc = pyb.ADC(Pin('Y11'))       # create an analog object from a pin
adc = pyb.ADC(pyb.Pin.board.Y11)
val = adc.read()                # read an analog value

#-----------------------------------------#
#Light intensity sensor(GY-30) <--> I2C(1)
#SDA <--> X10
