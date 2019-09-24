#!/usr/bin/env python3

from time import sleep
from subprocess import getoutput 
import sys
data=sys.argv[1:]

for i in data :
    print("PING request for server : "+i)
    print(getoutput("ping -c 3 "+i))    
    print("-----------------------------")
    print("-----------------------------")


