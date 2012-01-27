from PyQt4 import QtCore,QtGui		#import required PyQt libraries
from txtedit import Ui_MainWindow	#import the UI file compiled with pyuic4
import sys				#for command line args that QApplication constructor needs
import codecs
class textedit(QtGui.QMainWindow):				#create a class that inherits from QMainWindow or Top Level Container

	def readFile(self):
		dialog=QtGui.QFileDialog(self)			#create a File Dialog
		self.fileName=dialog.getOpenFileName()		#Open the File Dialog, and get the filename, or get None
		if(self.fileName<>None and self.fileName<>""):	#if the filename is not null, then open and read its contents
			fileData=codecs.open(self.fileName,'r','utf-8').read()
			self.ui.textWindow.setText(fileData)
		else:
			print 'Error\n'				#if no file is selected, print error
	
	def saveFile(self):
		dialog=saveFileName=QtGui.QFileDialog(self)
		self.saveName=dialog.getSaveFileName()
		if(self.saveName<>None and self.saveName<>""):
			file=codecs.open(self.saveName,'w','utf-8')
			file.write(unicode((self.ui.textWindow.toPlainText())))

	def __init__(self,parent=None):				#constructor. It has no parent by default, as it is a top level window
		QtGui.QWidget.__init__(self,parent)		
		self.ui=Ui_MainWindow()				#call constructor for the Ui_MainWindow, which is pyuic4 compiled class
		self.ui.setupUi(self)				#setup the ui
		QtCore.QObject.connect(self.ui.buttonOpen,QtCore.SIGNAL('clicked()'),self.readFile)
		QtCore.QObject.connect(self.ui.buttonSave,QtCore.SIGNAL('clicked()'),self.saveFile)

if __name__=="__main__":
	app=QtGui.QApplication(sys.argv)
	text=textedit()
	text.show()
	sys.exit(app.exec_())

