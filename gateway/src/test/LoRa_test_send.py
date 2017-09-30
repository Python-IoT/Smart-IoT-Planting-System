#!/usr/bin/env python
# LoRa_test_send.py
#Communication module: LoRa.
#Communication method with device via LoRa.
#Uart port drive LoRa module.
#Parse JSON between device and gateway via LoRa channel.
#LoRa module: E32-TTL-100
#Pin specification:
#M0    <--> GPIO(OUT)     #mode setting  connct to GND is OK!(Low)
#M1    <--> GPIO(OUT)     #mode setting  connct to GND is OK!(Low)
#RXD   <--> 8(TXD)        #ttyS0
#TXD   <--> 10(RXD)       #ttyS0
#AUX   <--> GPIO/INT(IN)  #module status detecting
#VCC
#GND

#Install pyserial:
#pip install pyserial

import serial
import time
pyserial_test = serial.Serial("/dev/ttyS0", 9600)
def main():
    while True:
        pyserial_test.write('{ID:12,CMD:Notify,DATA:Gateway,SEQUENCE:123}')
        pyserial_test.flushInput()
        time.sleep(3)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        if pyserial_test != None:
            pyserial_test.close()
