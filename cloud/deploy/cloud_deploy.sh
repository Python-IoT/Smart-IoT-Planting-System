#!/bin/sh
#PC ubuntu simulate server.
cd /usr/bin
#because MQTT run best with Python 3.4.3, so we need to use Python3.4
ln -s python3.4 python
apt-get install python3-pip
pip3 install hbmqtt





#------------------------------------------
#install pip
#universal method：
curl -O https://raw.github.com/pypa/pip/master/contrib/get-pip.py
python get-pip.py
#different platform:
#ubuntu:
sudo apt-get install python-pip
#CentOS:
sudo yum install python-pip
#install hbmqtt
pip install hbmqtt
#install virtualenv
pip install virtualenv

#install MySQL in CentOS:
yum install -y mysql-server mysql mysql-devel 

