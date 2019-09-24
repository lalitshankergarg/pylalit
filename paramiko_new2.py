#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3

import paramiko,time,sys

#using as ssh client 
client=paramiko.SSHClient()

#auto adjust host key verification with yes or no
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#time for connecting to remote Cisco IOS
addr= sys.argv[1]#First argument as ip address
u=sys.argv[2] #username as second argument
p=sys.argv[3] #password as third argument
#connect with ssh session
client.connect(addr,username=u,password=p,allow_agent=False, look_for_keys=False)
#we have to ask for shell
device_access=client.invoke_shell()
# now sending command
device_access.send("term len 0 \n")
device_access.send("show run \n")
device_access.send("show ip int bri \n")
device_access.send("show int gig1 \n")
time.sleep(1)
# assume command got executed so lets recv data
output=device_access.recv(10000000)
#decoding byte-like string in to string

print(output.decode("ascii"))

#saving output in a file
with open("csrv1000v_1.txt","w") as f:
        f.write(output.decode('ascii'))
