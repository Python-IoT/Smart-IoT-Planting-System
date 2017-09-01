#Sqlite database init sql.
sqlite3 test.db

create table smart_agri(device_id interger primary key, sensor_interval text,light_status text,alarm_swith text);

insert into smart_agri values(1, '1000', 'ON', 'CLOSE');

.headers on #open the title of table
.mode column #display contents of table in column format
