#1/usr/bin/python3

import netmiko,time
#multi vendor library

device1={
	'username' : 'lalit',
	'password' : 'cisco',
	'device_type' : 'cisco_ios',
	'host' : '192.168.234.131'
}


# to connect target device
#by checking couple of things connecthandler will allow you to connect
'''
	. device_type

'''
device_connect=netmiko.ConnectHandler(**device1)
#print([i for i in dir(device_connect) if 'send' in i])
# now sending command
cmd=["show ip int bri","show ippp"]
for i in cmd:
	print("sending command",i)
	print("____________________________")
	output=device_connect.send_command(i)
	print(output)



