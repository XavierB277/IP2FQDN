# -*- encoding: utf-8 -*-
from dns import resolver, reversename
import time

list = []
for line in open('ip_addresses.txt', 'r'):
	list.append(line.strip())

print("\nResolving IP addresses...\n")
time.sleep(2)
x = 0
for ip in list:
	try:
		addr = reversename.from_address(list[x])
		result=str(resolver.query(addr,"PTR")[0])
		print(list[x] + "\t" + result)
		x += 1
	except:
		print(list[x] + "\t" + "Not Found")
		x += 1

time.sleep(2)
print("\nTask Complete!")
