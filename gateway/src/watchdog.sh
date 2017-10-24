#!/usr/bin/env bash
 
echo "[+] Activating Temperature Sensor"
modprobe bcm2708_wdog
echo "bcm2708_wdog" >> /etc/modules
 
echo "[+]Installing Watchdog"
apt-get -y install watchdog chkconfig
 
echo "[+]Setting Up Watchdog"
chkconfig watchdog on
sed -i 's/#max-load-1[^5]/max-load-1\ /g' /etc/watchdog.conf
sed -i 's/#\(watchdog-device\t[\ ]*\)\=/\1\t\=/g' /etc/watchdog.conf
sed -i 's/#\(temperature-device[\ ]*\)\=/\1\ \= \/sys\/class\/thermal\/thermal\_zone0\/temp/g' /etc/watchdog.conf
sed -i 's/#\(max-temperature[\ ]*\)\=\ 120/\1\ \=\ 75000/g' /etc/watchdog.conf
sed -i 's/#\(interval[\ ]*\)\=\ 1/\1\ \=\ 10 /g' /etc/watchdog.conf
/etc/init.d/watchdog start
