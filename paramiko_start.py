#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3

import paramiko,time

#using as ssh client 
client=paramiko.SSHClient()

#auto adjust host key verification with yes or no
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#time for connecting to remote Cisco IOS
addr=input("enter your router ip : ")
u='lalit'
p='cisco'
client.connect(addr,username=u,password=p,allow_agent=False, look_for_keys=False)
#we have to ask for shell
device_access=client.invoke_shell()
# now sending command
device_access.send("show ip int bri \n")
time.sleep(1)
# assume command got executed so lets recv data
output=device_access.recv(100000)
#decoding byte-like string in to string

print(output.decode("ascii"))
