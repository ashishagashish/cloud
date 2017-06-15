#!usr/bin/python

import os,time,socket,getpass


s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s_ip="192.168.122.182"
s_port=8888

print "1 : For fullscreenshot \n2 : For selected Part"
y = raw_input("")

if y == "1":
	os.system('sshpass -p "q" ssh -X a@'+s_ip+' gnome-screenshot + ' &>/dev/null'')
	print "Sreenschot has been saved in pictures"

elif y == "2":
	os.system('sshpass -p "q" ssh -X a@'+s_ip+' gnome-screenshot -a + ' &>/dev/null'')
	print "Sreenschot has been saved in pictures"

else:
	print "Invalid Selection"

execfile('saas.py')
