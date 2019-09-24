#!/usr/bin/python3

from time import ctime,sleep
#only importing desired functions
from subprocess import getstatusoutput,getoutput
from os import mkdir


options='''
press 1 to check current date and time : 
press 2 to run any command in your current os :
press 3 to create a directory :
press 4 to start a train :
press 5 ping any website :
'''
print(options)
#to capture input from user
choice=input()
print("you have choosen ",choice)
#conditional statement with if
if choice == '1' : 
    print(ctime())

elif choice == '2' :
    cmd=input("please enter any command : ")
    output=getoutput(cmd)
    print(output)

elif int(choice) == 3 :
    d_name=input("enter directory name to create : ")
    mkdir(d_name)
    print(d_name," successfully created " )

elif choice == '5' :
    web=input("enter website name to ping :  ")
    print(getoutput("ping -c 5 "+web))

else:
    print("wrong option ")

