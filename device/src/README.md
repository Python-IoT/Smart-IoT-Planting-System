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
 ------------ | ------------- | ------------ | -------------  
 1 | ONLINE | N | N          


第一表头 | 第二表头
------------ | -------------
第一单元格内容 | 第二单元格内容
第一列内容 | 第二列内容





