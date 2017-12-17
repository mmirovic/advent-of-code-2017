#!/usr/bin/python

str = open('input', 'r').read().strip()
#str = '91212129'
#str = '1111'
#str = '1234'
#str = '91212129'

c1 = c2 = 0
s = len(str)

for i in range(s):
	if str[i] == str[(i+1)%s]:
		c1 += int(str[i])
	if str[i] == str[(i+s/2)%s]:
		c2 += int(str[i])
	
print c1, c2
