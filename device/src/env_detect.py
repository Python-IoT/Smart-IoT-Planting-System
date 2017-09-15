#--------------------------------------
#    ___ _      ____
#   / __(_)__  / __/
#  _\ \/ / _ \_\ \
# /___/_/ .__/___/
#      /_/
#
#           dev_detect.py
#  Environment detection.
#
# Author : Arvin
# Date   : 15/09/2017
#--------------------------------------

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
#SCL <--> X9
#VCC
#GND
#ADO(ADDR/address) <--> None
#Command list:
#0x00 power off
#0x01	power on
#0x07	reset
#0x10	Continuously H-Resolution Mode, 1lx resolution, measurement time is typically 120ms
#0x11	0.5lx, 120ms
#0x13	4lx, 16ms

from pyb import I2C

i2c = I2C(1, I2C.MASTER)             # create and init as a master

i2c.send(0x10, 0x23)        # send 3 bytes to slave with address 0x23

i2c.is_ready(0x23)           # check if slave 0x23 is ready
i2c.scan()                   # scan for slaves on the bus, returning

i2c.mem_read(3, 0x23, 2)     # read 3 bytes from memory of slave 0x23,
                             #   starting at address 2 in the slave

