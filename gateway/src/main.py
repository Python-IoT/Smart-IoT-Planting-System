#!/usr/bin/env python

#Communicate with end devices via LoRa.
#Communicate with server via MQTT(hbmqtt) and HTTP POST.
#Save data in the sqlite database.
#Parse JSON from MQTT and LoRa protocol.

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

#You need to install pyserial manually, install command is below:
#pip install pyserial

import serial
import time
pyserial_test = serial.Serial("/dev/ttyS0", 9600)
def main():
    while True:
        #Waiting for LoRa module message from uart port.
        count = pyserial_test.inWaiting()
        #print('after inWaiting')
        if count != 0:
            recv = pyserial_test.read(count)
            #recv = pyserial_test.readline()
            print('[LoRa]recv:')
            print(recv)
            #Parse JSON
            response = '{"ID":1, "CMD":Online, "TYPE":"Light", "VALUE":"On"}'
            pyserial_test.write(response)
            pyserial_test.flushInput()
        time.sleep(0.1)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        if pyserial_test != None:
            pyserial_test.close()

