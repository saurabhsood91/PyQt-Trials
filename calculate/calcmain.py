'''
Created on Jan 28, 2012

@author: saurabh
'''

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from math import *

class Form(QDialog):
    def __init__(self,parent=None):
        super(Form,self).__init__(parent)
        self.browser=QTextBrowser()
        self.lineEdit=QLineEdit("Enter Expression and Press Enter: ")
        self.lineEdit.selectAll()
        self.layout=QVBoxLayout()
        self.layout.addWidget(self.browser)
        self.layout.addWidget(self.lineEdit)
        self.setLayout(self.layout)
        self.lineEdit.setFocus()
        self.connect(self.lineEdit, SIGNAL("returnPressed()"),self.updateUi)
        self.setWindowTitle("Calculate")
        self.show()
    def updateUi(self):
        try:
            text=unicode(self.lineEdit.text())
            self.browser.append("%s = <b>%s</b>" % (text,eval(text)))
            self.lineEdit.clear()
        except:
            self.browser.append("<font color=red>Invalid Expression</font> - %s" % (text))

if __name__!="main":
    app=QApplication(sys.argv)
    formObj=Form()
    formObj.show()
    app.exec_()
