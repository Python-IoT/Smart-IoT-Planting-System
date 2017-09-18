#!/usr/bin/env python
#    LoRa.py
#Communication module: LoRa.
#Communication method with device via LoRa.
#Uart port drive LoRa module.
#Parse JSON between device and gateway via LoRa channel.
#LoRa module: E32-TTL-100
#Pin specification:
#M0    <--> GPIO(OUT)     #mode setting
#M1    <--> GPIO(OUT)     #mode setting
#RXD   <--> 8(TXD)        #ttyS0
#TXD   <--> 10(RXD)       #ttyS0
#AUX   <--> GPIO/INT(IN)  #module status detecting
#VCC
#GND

#Install pyserial:
#pip install pyserial    #Python2
#pip3 install pyserial   #Python3

#Config UART port in raspberryPi:
#$ raspi-config
#Would you like a login shell to be accessible over serial? Choose No.
#Would you like the serial port hardware to be enabled?     Choose Yes.
#ttyS0 appear in /dev

import serial  
import time  
pyserial_test = serial.Serial("/dev/ttyS0", 115200)  
def main():  
    while True:  
        count = pyserial_test.inWaiting()  
        if count != 0:  
            recv = "pi return: "+pyserial_test.read(count)+"\n"  
            pyserial_test.write(recv)  
        pyserial_test.flushInput()  
        time.sleep(0.1)  
  
if __name__ == '__main__':  
    try:  
        main()  
    except KeyboardInterrupt:  
        if pyserial_test != None:  
            pyserial_test.close()  
