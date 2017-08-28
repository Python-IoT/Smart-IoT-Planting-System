#soil moisture sensor.
#VCC, GND, AO, DO
#DO <--> GPIO
#AO <--> ADC Port
#if value is low than defined data, DO value is 0, 
#if value is high than defined data, DO value is 1.
#AO is the specific value.
from pyb import Pin
p_in = Pin('Y12', Pin.IN, Pin.PULL_UP)
p_in.value


adc = pyb.ADC(Pin('Y11'))       # create an analog object from a pin
adc = pyb.ADC(pyb.Pin.board.Y11)
val = adc.read()                # read an analog value
