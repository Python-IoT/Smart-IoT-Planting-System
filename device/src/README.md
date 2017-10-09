Source code repository for end node device.  
## Function list:  
- **irrigation actuator**   
When the soil moisture is lower than the standard value, steering engine(simulate the tap) will open to water the plant.

- **environment detection**     
Collect the environment information which consists of light Intensity, raining volume, air temperature&humility, water level.

- **security system**    
If motion detection sensor detect the intrusion， it will send the message to gateway and cloud platform, gateway will call the security guard's phone.

- **light controlling**    
Simulate the bulb with led on TPYBoard, user can control the light via the browser on smartphone.

- **device management**    
Device will report it's status(battery, online status) to gateway and cloud platform, if there is something wrong, engineer will repair the device.

## Command list:
- **Online**   
When the device powers on, it need to send 'Online' command to gateway to obtain its data(light/led status[on/off], irrigation status[on/off], environment report rate, etc).
Json string format:    

ID | CMD | TYPE | VALUE
------------ | ------------- | ------------- | -------------
1 | Online | N | N

- **Heartbeat**   
Device need to send heartbeat message to gatewat to show it is alive, and send the battery volume to gateway.
Json string format:    

ID | CMD | TYPE | VALUE
------------ | ------------- | ------------- | -------------
1 | Heartbeat | Battery | 80

- **Envionment**   
Device will conllect sensor data and send them to gateway regularly.
Json string format:    

ID | CMD | TYPE | VALUE
------------ | ------------- | ------------- | -------------
1 | Env | light | 2000
1 | Env | tempurature | 28
1 | Env | humility | 61
1 | Env | water | 20
1 | Env | raning | 72

- **Alarm**   
Device will send alarm message to gateway if motion detection sensor detect people.
Json string format:    

ID | CMD | TYPE | VALUE
------------ | ------------- | ------------- | -------------
1 | Alarm | N | N






