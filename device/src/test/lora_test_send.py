#    lora_test_send.py
#Communication module: LoRa.
#Communication method with gateway via LoRa.
#Uart port drive LoRa module.
#Parse JSON between device and gateway via LoRa channel.
#LoRa module: E32-TTL-100
#Pin specification:
#Module         MCU
#M0(IN)    <--> GPIO(X3)(OUT)     #mode setting, can not hang
#M1(IN)    <--> GPIO(X4)(OUT)     #mode setting, can not hang
#RXD(IN)   <--> X1(TX)(OUT)   #UART4
#TXD(OUT)  <--> X2(RX)(IN)    #UART4
#AUX(OUT)  <--> GPIO/INT(IN)  #module status detecting
#VCC
#GND

#Communication mode is 0, need to set M0 and M1 to 0.

#JSON data format:
#{ID:123,CMD:heartbeat,DATA:hello,SEQUENCE:123}

from pyb import Pin
from pyb import UART  
from pyb import Timer
import time

#LED shining regularly(using timer) to indicate the program is running correctly
tim1 = Timer(1, freq=1)
tim1.callback(lambda t: pyb.LED(1).toggle())

M0 = Pin('X3', Pin.OUT_PP)
M1 = Pin('X4', Pin.OUT_PP)
M0.low()
M1.low()

u4 = UART(4,9600)  
u4.init(9600, bits=8, parity=None, stop=1)  
u4.write('{ID:1,CMD:OnLine,DATA:TYPBoard1,SEQ:0}')

if __name__=='__main__':
  while True:
    u4.write('{ID:1,CMD:HEARTBEAT,DATA:TPYBoard1,SEQ:1}')
    time.sleep(1)
    print(u4.read())
    time.sleep(2)

#GPIO input demo
#p_in = Pin('X2', Pin.IN, Pin.PULL_UP)
#p_in.value() # get value, 0 or 1
#M0.high()
#u4.read()
#u4.any() #check the data in UART buffer

