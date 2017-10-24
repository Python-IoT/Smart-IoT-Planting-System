#!/bin/sh
#start watchdog.sh
./watchdog.sh

#start python program
./main.py

#start backup_db.py
./backup_db.py
