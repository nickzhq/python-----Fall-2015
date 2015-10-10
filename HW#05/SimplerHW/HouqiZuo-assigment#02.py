import urllib.request
import re
import json
from pprint import pprint

url = "https://restcountries.eu/rest/v1/alpha/co"
page=urllib.request.urlopen(url)
content=page.read()
content_string=content.decode('utf-8')

json_data = json.loads(content_string)

#print(json_data)
#print("\n\n\n")
#pprint(json_data)

code_input = input("Please enter the country code: ")

flag = False
for k,v in json_data.items():
	if ( code_input == v ):
		print("Found it")
		print("nativeName: ", json_data['nativeName'])
		print("capital: ", json_data['capital'])
		flag = True
		break
if( not flag ):
	print("Didn't find it")
	print("nativeName: ", json_data['nativeName'])
	print("capital: ", json_data['capital'])

print("Bye Bye")
