#!/bin/sh
#Script for deploy & preparation for gateway software.
#install requests lib
pipenv install requests

#install pip3
#install virtualenv
#install hbmqtt
pip install hbmqtt

#install sqlite
sudo apt-get install sqlite sqlite3
