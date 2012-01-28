'''
Created on Jan 28, 2012

@author: saurabh
'''

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from math import *

class Form(QDialog):
    def __init__(self,parent=None):             #constructor with parent as none by default, signifying top level window
        super(Form,self).__init__(parent)       #constructing the base class, which is QDialog
        self.browser=QTextBrowser()             #creating a text browser
        self.lineEdit=QLineEdit("Enter Expression and Press Enter: ")       #creating a line edit for entering expression
        self.lineEdit.selectAll()                                           #selecting the whole text by default
        self.layout=QVBoxLayout()                                           #using VBoxLayout
        self.layout.addWidget(self.browser)                                 #adding browser to layout
        self.layout.addWidget(self.lineEdit)                                #adding lineedit to layout
        self.setLayout(self.layout)                                         #setting the main layout to the defined layout
        self.lineEdit.setFocus()                                            #setting focus to lineedit
        self.connect(self.lineEdit, SIGNAL("returnPressed()"),self.updateUi)    #connecting return pressed to updateUI slot
        self.setWindowTitle("Calculate")                                        #setting window title to calculate
        self.show()                                                             #showing the UI
    def updateUi(self):
        try:
            text=unicode(self.lineEdit.text())                                  #extracting the text in the lineedit
            self.browser.append("%s = <b>%s</b>" % (text,eval(text)))           #evaluating the expression and showing in browser
            self.lineEdit.clear()                                               #clearing the expression lineedit
        except:
            self.browser.append("<font color=red>Invalid Expression</font> - %s" % (text))  #if invalid expression, show msg

if __name__!="main":
    app=QApplication(sys.argv)
    formObj=Form()
    formObj.show()
    app.exec_()
