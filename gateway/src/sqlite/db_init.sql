PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
 
CREATE TABLE temps(
    name TEXT DEFAULT 'RPi.CPU',
    tdatetime DATETIME DEFAULT (datetime('now', 'localtime')),
    temperature NUMERIC NOT NULL
);
     
INSERT INTO temps
VALUES('RPi.CPU', datetime('now', 'localtime', '-3 hours'), 40.1);
 
INSERT INTO temps(name, tdatetime, temperature)
VALUES('RPi.CPU', datetime('now', 'localtime', '-2 hours'), 40.2);
 
INSERT INTO temps(tdatetime, temperature)
VALUES(datetime('now', 'localtime', '-1 hours'), 40.3);
 
INSERT INTO temps(temperature)
VALUES(40.4);
 
COMMIT;
