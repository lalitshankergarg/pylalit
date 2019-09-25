#1/usr/bin/python3

import netmiko,time

#multi vendor library
from getpass import getpass

sec=getpass("please enter password for device : ")
#accept password without showing in screen

device1={
	'username' : 'lalit',
	'password' : sec,
	'device_type' : 'cisco_ios',
	'host' : '192.168.234.13'
}
device2={
        'username' : 'lalit',
        'password' : sec,
        'device_type' : 'cisco_ios',
        'host' : '192.168.234.131'
}
device3={
        'username' : 'lalit',
        'password' : 'cisc',
        'device_type' : 'cisco_ios',
        'host' : '192.168.234.131'
}
device4={
        'username' : 'lalit',
        'password' : 'cisco',
        'device_type' : 'cisco_ios1',
        'host' : '192.168.234.131'
}
device5={
        'username' : 'lalit',
        'password' : 'cisco',
        'device_type' : 'cisco_ios',
        'host' : '192.168.234.131'
}


for i in [device1,device2,device3,device4] :
	try:
		print("                                         ")
		print("                                         ")
		print("connecting with Device_type :--->",i['device_type'],"Having IP",i['host'])
		print("                                         ")
		device_connect=netmiko.ConnectHandler(**i)
		#sending command
		output=device_connect.send_command("sh ip int bri")
		print(output)

	except netmiko.ssh_exception.NetMikoTimeoutException :
		print("Please check your IP or Network connectivity : ", i['host'])
	except netmiko.ssh_exception.AuthenticationException :
		print(" wrong credentials used : ", i['host'])
	except :
		print("Unknown errors occurred : ", i['host'])



