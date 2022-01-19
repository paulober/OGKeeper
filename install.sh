#!/bin/bash

if [ "$(id -u)" == 0]
    then echo "Please run this installer as root"
    exit
fi

cp ogkeeper.py /usr/local/bin/ogkeeper
cp ogkeeper.service /etc/systemd/system/
mkdir /etc/ogkeeper
cp config.json /etc/ogkeeper/

nano /etc/ogkeeper/config.json
