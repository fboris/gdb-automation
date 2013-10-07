#!/usr/bin/python
check_str= 'This is a simple sentence'

fd = open('./serial.out','r')
read_str = fd.read()
for idx, val in enumerate(check_str):
	if val == read_str[idx]:
		print idx
		print "find {}".format(val)

	else:
             	print "error!"

