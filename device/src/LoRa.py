#    LoRa.py
#Communication module: LoRa.
#Communication method with gateway via LoRa.
#Uart port drive LoRa module.
#Parse JSON between device and gateway via LoRa channel.
#LoRa module: E32-TTL-100
#Pin specification:
#Module         MCU
#M0(IN)    <--> GPIO(OUT)     #mode setting, can not hang
#M1(IN)    <--> GPIO(OUT)     #mode setting, can not hang
#RXD(IN)   <--> X1(TX)(OUT)   #UART4
#TXD(OUT)  <--> X2(RX)(IN)    #UART4
#AUX(OUT)  <--> GPIO/INT(IN)  #module status detecting
#VCC
#GND

#Communication mode is 0, need to set M0 and M1 to 0.

#JSON data format:
#{ID:123,CMD:heartbeat,DATA:hello,SEQUENCE:123}
from pyb import UART  
u4 = UART(4,115200)  
u4.init(115200, bits=8, parity=None, stop=1)  
def Send(data):
  u4.write(data)

