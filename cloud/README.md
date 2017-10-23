Using Python Django framework to develop the cloud platform.    
Features include:
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
