#!/usr/bin/python

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys				#to access the command line arguments
import time				#to access the sleep function

app=QApplication(sys.argv)		#create a QApplication object
currentTime=QTime.currentTime()
try:
	if len(sys.argv)<2:				#by default, there is one argument. if <2, there is no arguments given. Thus, no time provided. Raise Error
		raise ValueError			#Raise Value Error
	hours,mins=sys.argv[1].split(":")		#split the string argument. Time provided like 3:13. Hours-> 3, Mins -> 13
	due=QTime(int(hours),int(mins))			#construct the QTime object with the obtained Hours and Mins
	if not due.isValid():				#check if the constructed time is valid or not
		raise ValueError			#if time is not valid, raise value error
	if len(sys.argv)>2:				#if more than two arguments are provided, then there is an optional message given. Use that in message also
		message=" ".join(sys.argv[2:])
except ValueError:					#Handle the exception
	message="Usage: HH:MM [optional message]"	#24 hr clock


while QTime.currentTime()<due:				#while the current time is less than the due time
	time.sleep(20)					#put the process to sleep till the specified number of seconds

label=QLabel("<font color='red'><h1><b>"+message+"</b></h1></font>")		#construct the label to be displayed
label.setWindowFlags(Qt.SplashScreen)						#set the label as a Splash Screen
label.show()									#show the label
QTimer.singleShot(60000,app.quit)						#single shot timer. Time out after the specified ms, and which function will be called after timeout
app.exec_()									#enter event loop
