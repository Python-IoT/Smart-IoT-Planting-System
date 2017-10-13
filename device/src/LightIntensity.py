#--------------------------------------
#    ___ _      ____
#   / __(_)__  / __/
#  _\ \/ / _ \_\ \
# /___/_/ .__/___/
#      /_/
#
#           LightIntensity.py
#  Get light intensity data from GY-30 module which is base on bh1750 sensor.
#
# Author : Arvin
# Date   : 15/09/2017
#--------------------------------------

#Wiring method between TPYBoard and GY-30 module.
#Light intensity sensor(GY-30) <--> I2C(1)
#SDA <--> X10
#SCL <--> X9
#VCC
#GND
#ADO(ADDR/address) <--> GND

from pyb import I2C
import time

# Define some constants from the datasheet

DEVICE     = 0x23 # The value is 0x23 if GY-30's ADO(ADDR) pin is connected to GND, value is 0x5c while VCC.

POWER_DOWN = 0x00 # No active state
POWER_ON   = 0x01 # Power on
RESET      = 0x07 # Reset data register value

# Start measurement at 4lx resolution. Time typically 16ms.
CONTINUOUS_LOW_RES_MODE = 0x13
# Start measurement at 1lx resolution. Time typically 120ms
CONTINUOUS_HIGH_RES_MODE_1 = 0x10
# Start measurement at 0.5lx resolution. Time typically 120ms
CONTINUOUS_HIGH_RES_MODE_2 = 0x11
# Start measurement at 1lx resolution. Time typically 120ms
# Device is automatically set to Power Down after measurement.
ONE_TIME_HIGH_RES_MODE_1 = 0x20
# Start measurement at 0.5lx resolution. Time typically 120ms
# Device is automatically set to Power Down after measurement.
ONE_TIME_HIGH_RES_MODE_2 = 0x21
# Start measurement at 1lx resolution. Time typically 120ms
# Device is automatically set to Power Down after measurement.
ONE_TIME_LOW_RES_MODE = 0x23


i2c = I2C(1, I2C.MASTER)             # create and init as a master

#i2c.is_ready(0x23)           # check if slave 0x23 is ready
#i2c.scan()                   # scan for slaves on the bus, returning

def convertToNumber(data):
  # Simple function to convert 2 bytes of data
  # into a decimal number
  #return ((data[1] + (256 * data[0])) / 1.2)
  #convert float to int
  return int(((data[1] + (256 * data[0])) / 1.2))

def readLight(addr=DEVICE):
#  data = bus.read_i2c_block_data(addr,ONE_TIME_HIGH_RES_MODE_1)
  i2c.send(CONTINUOUS_HIGH_RES_MODE_1, DEVICE) 
  time.sleep(0.2)  #Waiting for the sensor data
  data = i2c.mem_read(8, DEVICE, 2) # read 3 bytes from memory of slave 0x23, tarting at address 2 in the slave
  #print(data)
  #print(data[1])
  #print(data[2])
  return convertToNumber(data)
