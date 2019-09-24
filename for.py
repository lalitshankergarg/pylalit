#!/usr/bin/env python3

from time import sleep
import sys
data=sys.argv[1:]

sum=0
for i in data :
    sum=sum+int(i)

print(sum)


