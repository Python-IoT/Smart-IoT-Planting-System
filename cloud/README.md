Using Python Django framework to develop the cloud platform.    
## Features include:
- connection management(support plenty of clients)
- message transmission(user browser <--> server <--> gateway <--> device)
- device monitoring(consist of gateway<cpu temperature, on-line status> and device(battery volume, on-line status))
- data visualization(echars python, environment data from sensor, plant grow status, alarm record)
- data storage(store data in MySQL)
- user interface(web browser for PC, tablets, phone based on bootstrap)


MQTT(hbmqtt) is responsible for command between server and gateway.   
Django is responsible for interaction between server and user.   

Message from gateway received by MQTT will insert into MySQL database in server.    
Django read data from MySQL and show it on the top of highcharts.    


## Web UI:   
- environment display: use highcharts to show env info
- light: control light remotely, show its status(on/off)
- irrigation: manual/auto(set time or siol moisture threshold value)
- security: hack record, alarm method(text message, call the phone, web message)
- device management: online/offline, battery volume, hardware topology
- user: profile, password, figure



Gateway online will send message to cloud, sync the data from cloud to local.   
Gateway online method of communication with cloud base on HTTP(requests).   
Gateway need to send gw.db to cloud regularly.  
Gateway send and download gw.db from cloud via requests framework.

Gateway heartbeat and command with cloud base on MQTT(hbmqtt).

could web base on Django and bootstrap, user command send to gateway via MQTT.  

hbmqtt and Django interact base on  MySQL database.
