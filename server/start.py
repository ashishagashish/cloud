#!/usr/bin/python

import os,time,socket,getpass

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.bind(("",8888))
s_data=s.recvfrom(100)
s_data1=s.recvfrom(100)

if s_data[0]=="test" and s_data1[0]=="1234":
	s.sendto("ok",s_data[1])
else:
	s.sendto("not ok",s_data[1])
	exit()
execfile('start.py')
