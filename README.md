# (SIPS)Smart-IoT-Planting-System
[![MIT Licence](https://badges.frapsoft.com/os/mit/mit.svg?v=103)](https://opensource.org/licenses/mit-license.php)   
SIPS is an intelligence/smart/automatic planting system in the agricultural greenhouse which is base on IoT technology.   
It consists of sensors, terminal device(STM32 MCU), gateway(RPi), Web server.   
This system adopted LoRa, MQTT, GSM module, Django web framework, echarts, bootstrap and ajax.   
Most of the source codes are implemented by Python.  

## Features:
- **Environmental Monitoring**    
  Show environment information, such as air temperature, humility, light intensity, soil moisture, water level, raining volume.
- **Irrigating Remotely**   
  Control pump to irrigate by 3 methods, auto, manual or regularly.
- **Security System**   
  Trigger alarm while detecting signal from IR sensor.
- **Light Controlling**   
  Control light by 3 methods, auto, manual or regularly.
- **Devices Tracking**   
  Show the online status, battery of all the hardware devices.
- **File Mangement**    
  Mange database file of gateway.

## Project Diagram:
![Alt text](https://github.com/Python-IoT/Smart-IoT-Planting-System/blob/master/arch/arch-diagram.png)

## Hardware Lists:
![Alt text](https://github.com/Python-IoT/Smart-IoT-Planting-System/blob/master/arch/Hardware-kit-2.jpg)

## Obtain Hardware:   
Contact me by mail, wechat or twitter.   
Mail: mikepetermessidona@hotmail.com    
Wechat: Arvin-Messi    
Twitter: Messi_Arvin

## Deployment Steps:
- download source code
- obtain hardware kits
- TYPBoard wiring and firmware download
- gateway(raspberryPi) wiring and software deployment and application running
- deploy source code of cloud on server and execute it
- test the system via browser

## Cloud UI:
![Alt text](https://github.com/Python-IoT/Smart-IoT-Planting-System/blob/master/arch/environment.png)




