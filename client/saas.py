#!usr/bin/python

import os

x="""
	Menu

Press 1 to Get Firefox :
Press 2 to Get vlc :
Press 3 to Get calculator :
Press 4 to Get Web Camera:
press 5 to Get Screenshot:
Press 6 to Get office :
Press 7 to Get Gedit :
Press 9 to EXIT : 
"""

print x

ch=raw_input()

if ch=='1':
	print"Now wait for a minute"
	execfile("firefox.py")
elif ch=='2':
	print"Now wait for a minute"
	execfile("vlc.py")
elif ch=='3':
	print"Now wait for a minute"
	execfile("cal.py")
elif ch=='4':
	print"Now wait for a minute"
	execfile("webcam.py")
elif ch=='5':
	print"Now wait for a minute"
	execfile("screenshot.py")
elif ch=='6':
	print"Now wait for a minute"
	execfile("office.py")
elif ch=='7':
	print"Now wait for a minute"
	execfile("gedit.py")
elif ch=='9':
	print "BYE BYE"
	exit()
else:
	print "Wrong Option"
	execfile('saas.py')
