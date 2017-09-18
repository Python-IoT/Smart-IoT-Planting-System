#    LoRa.py
#Communication module: LoRa.
#Communication method with gateway via LoRa.
#Uart port drive LoRa module.
#Parse JSON between device and gateway via LoRa channel.
#LoRa module: E32-TTL-100
#Pin specification:
#M0    <--> GPIO(OUT)     #mode setting
#M1    <--> GPIO(OUT)     #mode setting
#RXD   <--> X1(TX)        #UART4
#TXD   <--> X2(RX)        #UART4
#AUX   <--> GPIO/INT(IN)  #module status detecting
#VCC
#GND

from pyb import UART  
u4 = UART(4,115200)  
u4.init(115200, bits=8, parity=None, stop=1)  
def Send(data):
  u4.write(data)



