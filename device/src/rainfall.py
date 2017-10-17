#rainfall sensor.
#VCC 
#GND
#DO <--> GPIO(X12)  Digital data
#AO <--> ADC Port(X11) Analog data
#if value is low than defined data, DO value is 0, 
#if value is high than defined data, DO value is 1.
#AO is the specific value.
import pyb
from pyb import Pin
p_in = Pin('X12', Pin.IN, Pin.PULL_UP)
p_in.value


adc = pyb.ADC(Pin('X11'))       # create an analog object from a pin
adc = pyb.ADC(pyb.Pin.board.X11)
# read an analog value
def getRainAo():               
  print('rainfall Ao')
  return adc.read()

# read an digital value
def getRainDo():             
  print('rainfall Do')
  return p_in.value
