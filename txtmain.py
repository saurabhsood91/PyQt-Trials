from PyQt4 import QtCore,QtGui		#import required PyQt libraries
from txtedit import Ui_MainWindow	#import the UI file compiled with pyuic4
import sys				#for command line args that QApplication constructor needs

class textedit(QtGui.QMainWindow):				#create a class that inherits from QMainWindow or Top Level Container
	def __init__(self,parent=None):				#constructor. It has no parent by default, as it is a top level window
		QtGui.QWidget.__init__(self,parent)		
		self.ui=Ui_MainWindow()				#call constructor for the Ui_MainWindow, which is pyuic4 compiled class
		self.ui.setupUi(self)				#setup the ui

if __name__=="__main__":
	app=QtGui.QApplication(sys.argv)
	text=textedit()
	text.show()
	sys.exit(app.exec_())

