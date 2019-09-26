#!/usr/bin/python3

import requests

from requests.auth import HTTPBasicAuth
#this is for supplying http basic authentication
cred=HTTPBasicAuth('lalit','cisco')

h={'Accept':'application/json'}
#headers={'Accept','text/html'}
#defining data from the api in json format
url="http://192.168.234.131/level/15/exec/-/sh/ip/int/bri/CR"

#now connection to restconf or --http protocol
output=requests.get(url,headers=h,auth=cred)
print(output)
#above output only giving HTTP response code
print(output.text)
#above output giving HTML based response
