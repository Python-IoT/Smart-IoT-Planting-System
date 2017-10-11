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
import json
#ser  = serial.Serial("/dev/ttyS0", 9600)
ser  = serial.Serial("/dev/ttyS0", 9600, timeout=0.2)
def main():
    while True:
        #Waiting for LoRa module message from uart port.
        count = ser.inWaiting()
        if count != 0:
            recv = pyserial_test.readline() #readline() need to set timeout, otherwise results block
            print(recv)
            json_lora = json.loads(recv)
            #Parse JSON
            if json_lora.get("ID") == 1 : #Device ID-1 existed in gateway database
              response = '{"ID":1, "CMD":Online, "TYPE":"Light", "VALUE":"On"}'
              ser.write(response)
            else:
              #init_device()  #Create sqlite table for device 1.
        ser.flushInput()
        time.sleep(0.1)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        if pyserial_test != None:
            pyserial_test.close()

