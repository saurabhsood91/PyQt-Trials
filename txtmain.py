from PyQt4 import QtCore,QtGui		#import required PyQt libraries
from txtedit import Ui_MainWindow	#import the UI file compiled with pyuic4
import sys				#for command line args that QApplication constructor needs
import codecs				#adds unicode support
class textedit(QtGui.QMainWindow):				#create a class that inherits from QMainWindow or Top Level Container

	#def readFile(self):
	#	dialog=QtGui.QFileDialog(self)			#create a File Dialog
	#	self.fileName=dialog.getOpenFileName()		#Open the File Dialog, and get the filename, or get None
	#	if(self.fileName<>None and self.fileName<>""):	#if the filename is not null, then open and read its contents
	#		fileData=codecs.open(self.fileName,'r','utf-8').read()
	#		self.ui.textWindow.setText(fileData)
	#	else:
	#		print 'Error\n'				#if no file is selected, print error
	
	def saveFile(self):
		dialog=saveFileName=QtGui.QFileDialog(self)
		self.saveName=dialog.getSaveFileName()
		if(self.saveName<>None and self.saveName<>""):
			file=codecs.open(self.saveName,'w','utf-8')			#opens the file in read mode, but with unicode support
			file.write(unicode((self.ui.textWindow.toPlainText())))		#converts the text to unicode, and then writes to the file
			self.ui.buttonSave.setEnabled(False)				#after saving, disable the save button
	
	def textChanged(self):
		self.ui.buttonSave.setEnabled(True)		#Enable Save Button
	
	def openFile(self):
		if self.ui.buttonSave.isEnabled()==True:					#if save button enabled, means changes are there
			message=QtGui.QMessageBox(self)						
			message.setText("Unsaved Changes")	
			message.setWindowTitle("Notepad")
			message.addButton("Save",QtGui.QMessageBox.AcceptRole)			#add Save Button to Message Box
			message.addButton("Discard",QtGui.QMessageBox.DestructiveRole)		#add Discard button to message box
			message.addButton("Cancel",QtGui.QMessageBox.RejectRole)		#added cancel button to message box
			message.exec_()								#message loop
			response=message.clickedButton().text()					#getting the response, and checking which button was clicked

			if response=="Save":							#if save was clicked, call the save slot
				self.saveFile()
			elif response=="Discard":						#if discard was called, show the dialog, and open the file accordingly
				dialog=QtGui.QFileDialog(self)	
				self.fileName=dialog.getOpenFileName()
				if(self.fileName<>None and self.fileName<>""):
					fileData=codecs.open(self.fileName,"r","utf-8").read()
					self.ui.textWindow.setText(fileData)
					self.ui.buttonSave.setEnabled(False)
			
	def __init__(self,parent=None):				#constructor. It has no parent by default, as it is a top level window
		QtGui.QWidget.__init__(self,parent)		
		self.ui=Ui_MainWindow()				#call constructor for the Ui_MainWindow, which is pyuic4 compiled class
		self.ui.setupUi(self)				#setup the ui
		self.ui.buttonSave.setEnabled(False)		#By Default, Save Button is Disabled
		QtCore.QObject.connect(self.ui.buttonOpen,QtCore.SIGNAL('clicked()'),self.openFile)
		QtCore.QObject.connect(self.ui.buttonSave,QtCore.SIGNAL('clicked()'),self.saveFile)
		QtCore.QObject.connect(self.ui.textWindow,QtCore.SIGNAL('textChanged()'),self.textChanged)	#connects textchanged to slot to Enable save button

if __name__=="__main__":
	app=QtGui.QApplication(sys.argv)
	text=textedit()
	text.show()
	sys.exit(app.exec_())

