#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3

import paramiko,time,sys

#using as ssh client 
client=paramiko.SSHClient()

#auto adjust host key verification with yes or no
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#create list of devices
device_ip=["192.168.234.131","192.168.234.131","192.168.234.131"]
u='lalit'
p='cisco'
#apply FOR loop
for i in device_ip :
	print("connecting with device : ",i)
	client.connect(i,username=u,password=p,allow_agent=False, look_for_keys=False)
#we have to ask for shell
	device_access=client.invoke_shell()
# now sending command
	device_access.send("term len 0 \n")
	device_access.send("show run \n")
	time.sleep(1)
# assume command got executed so lets recv data
	output=device_access.recv(10000000)
#decoding byte-like string in to string

	print(output.decode("ascii"))
	print("__________________________")
	print("__________________________")
	with open(i+time.ctime(), "w+") as f:
		f.write(output.decode('ascii'))
		time.sleep(1)
