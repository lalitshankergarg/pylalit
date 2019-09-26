#!/usr/bin/python3

import time
from ncclient import manager
#this code will act as netconf client

#using connect function with manager to connect Netconf enabled devices
device=manager.connect(host='192.168.234.131',port=22,username='lalit',password='cisco')
print(device)
print("___________________")
print("___________________")
time.sleep(2)
print(dir(device))
print("@@@@@@@@@@@")
time.sleep(1)
print(device.get_config('running').data_xml)
