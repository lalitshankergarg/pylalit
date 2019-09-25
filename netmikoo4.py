#1/usr/bin/python3

import netmiko,time

#multi vendor library


device1={
	'username' : 'lalit',
	'password' : 'cisco',
	'device_type' : 'cisco_ios',
	'host' : '192.168.234.131'
}
#to connect to target device
#by checking couple of things connect handler will allow you to connect

device_connect=netmiko.ConnectHandler(**device1)
#print([i for i in dir(device_connect) if 'send' in i])
#now sending configuration for device
conf=["hostname pyrouter1","username hello privi 10 password cisco","end"]
#output=device_connect.send_config_set(conf)
#print(output)
#sending configuration from file
output1=device_connect.send_config_from_file('myrouter.txt')
print(output1)

