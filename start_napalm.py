#!/usr/bin/python3

from napalm import get_network_driver

device1 = get_network_driver('ios')
#connecting to device
device=device1('192.168.234.131','lalit','cisco')
print([i for i in dir(device) if 'load' in i])
#open session with device
device.open()
#merging configuration
print(device.load_merge_candidate(filename='myrouter.txt'))
#check the difference
print(device.compare_config())
#now commit the config applid by file on router
c=input("confirm with y|n to apply configuration : ")
if c == 'y' or c == 'Y' :

	print("commiting the configuration")
	device.commit_config()
	res = input("Do you want to rollback changes : y|n")
	if res == 'y' or res == 'Y':
		device.rollback()
	else:
		print("no rollbacks applied")
elif c == 'n' or c == 'N' :
	print("discarding configuration ")
	device.discard_config()
else:
	print("please type only y|Y or n|N")

#close connection
device.close()
