#This scripyt is used to test module LightIntensity.
#Obtain light intensity data from sensor GY-30 and display it.
import py

#Import light intensity needed module 
import LightIntensity
import time

print('light intensity module test')
if __name__=='__main__':
  while True:
    print(LightIntensity.readLight())
    time.sleep(2)
