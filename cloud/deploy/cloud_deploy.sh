#!/bin/sh
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

