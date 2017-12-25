Gateway code and documents.   
Devices need to send a notice message to gateway while it boot up every time.   
Gateway will respond to device with device's relevant data(light on/off, watering status, etc) in database(sqlite).  

Gateway(Raspberry Pi) communicate with Server via MQTT and HTTP(request).  
MQTT python module is hbmqtt.   
Gateway is MQTT client, Server is MQTT broker and client.     

##Messages between End-device and Gateway:   

Message Type | ori_ID | des_ID | CMD | VALUE | Message Direction   
------------ | ------------- | ------------- | ------------- | ------------- | -------------    
Online Message | 1 | 123456 | Online | None | End-device -> Gateway    
Heartbeat Message | 1 |	123456 |	Heart |	[{"battery":"80"}] |	End-device -> Gateway    
Environmental Information |	1 |	123456 |	Env	| [{"temp":"28"},{"hum":"65"},...] | End-device -> Gateway     
Alarm Message | 1 | 123456 | ALarm | None | End-device -> Gateway     
Controlling Command |	123456 |	1 |	Control	| [{"light":"On"},{"pump":"Stop"},...] | Gateway -> End-device




