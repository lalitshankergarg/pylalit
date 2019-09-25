#1/usr/bin/python3

import netmiko,time

#multi vendor library


device1={
	'username' : 'lalit',
	'password' : 'cisco',
	'device_type' : 'cisco_ios',
	'host' : '192.168.234.131'
}

device_connect=netmiko.ConnectHandler(**device1)
output=device_connect.send_command("sh ip int bri")
print(output)
output1=device_connect.send_command("sh ip int bri",use_textfsm = True)
for i in output1:
	print("my interface name is ",i['intf'],"with IP ",i['ipaddr'], "having status ",i['status'])
	time.sleep(1)
#print(output1)


