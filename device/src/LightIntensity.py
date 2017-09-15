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
import smbus
import time

# Define some constants from the datasheet

DEVICE     = 0x5c # Default device I2C address

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

#bus = smbus.SMBus(0) # Rev 1 Pi uses 0
bus = smbus.SMBus(1)  # Rev 2 Pi uses 1

def convertToNumber(data):
  # Simple function to convert 2 bytes of data
  # into a decimal number
  return ((data[1] + (256 * data[0])) / 1.2)

def readLight(addr=DEVICE):
#  data = bus.read_i2c_block_data(addr,ONE_TIME_HIGH_RES_MODE_1)
  data = bus.read_i2c_block_data(addr,CONTINUOUS_HIGH_RES_MODE_1)
  print data
  print data[1]
  print data[2]
