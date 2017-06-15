#!usr/bin/python

import os,time,socket,getpass


s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s_ip="192.168.122.182"
s_port=8888

print "Enter your Authentication Details"
time.sleep(2)
s_user=raw_input("User Name : ")
s_passwd=getpass.getpass("Password : ")


s.sendto(s_user,(s_ip,s_port))
s.sendto(s_passwd,(s_ip,s_port))

z=s.recvfrom(2)

if z[0]=="ok":
	print"Connected"
	execfile('saas.py')
else:
	print "Not Connected" 
	exit()

