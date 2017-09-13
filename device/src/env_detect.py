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
#SCL <--> X9
#VCC
#GND
#ADO(ADDR/address ?)

from pyb import I2C

i2c = I2C(1)                         # create on bus 1
i2c = I2C(1, I2C.MASTER)             # create and init as a master
i2c.init(I2C.MASTER, baudrate=20000) # init as a master
i2c.init(I2C.SLAVE, addr=0x23)       # init as a slave with given address(GY-30 address is 0x23)
i2c.deinit()                         # turn off the peripheral

i2c.init(I2C.MASTER)
i2c.send('123', 0x23)        # send 3 bytes to slave with address 0x23
i2c.send(b'456', addr=0x23)  # keyword for address

i2c.is_ready(0x23)           # check if slave 0x23 is ready
i2c.scan()                   # scan for slaves on the bus, returning

i2c.mem_read(3, 0x23, 2)     # read 3 bytes from memory of slave 0x23,
                             #   starting at address 2 in the slave
i2c.mem_write('abc', 0x23, 2, timeout=1000) # write 'abc' (3 bytes) to memory of slave 0x23
                                            # starting at address 2 in the slave, timeout after 1 second
#Test log:
>>> from pyb import I2C
>>> i2c=I2C(1)
>>> i2c=I2C(1,I2C.MASTER)
>>> i2c.i2c.init(I2C.MASTER, baudrate=20000)
>>> i2c.init(I2C.MASTER, baudrate=20000)
>>> i2c.init(I2C.SLAVE,addr=0x23)
>>> i2c.is_ready(0x23)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: I2C must be a master
>>> i2c.scan()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: I2C must be a master
>>> i2c.init(I2C.MASTER)
>>> i2c.scan()
[35]
>>> i2c.is_ready(0x35)
False
>>> i2c.is_ready(0x23)
True
>>> i2c.mem_read(3,0x23,2)
b'\x00\x00\xff'
