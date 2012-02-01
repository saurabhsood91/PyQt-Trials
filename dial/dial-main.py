'''
Created on Jan 31, 2012

@author: saurabh
'''

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

class dialForm(QDialog):
    def __init__(self,parent=None):
        super(dialForm,self).__init__(parent)
        self.layout=QHBoxLayout()
        self.dial=QDial()
        self.dial.setNotchesVisible(True)
        self.spin=QSpinBox()
        self.dial.setRange(0,50)
        self.spin.setRange(0,50)
        self.layout.addWidget(self.dial)
        self.layout.addWidget(self.spin)
        self.setLayout(self.layout)
        self.connect(self.dial, SIGNAL("valueChanged(int)"),self.changeSpinVal)
        self.connect(self.spin, SIGNAL("valueChanged(int)"),self.changeDialVal)
        self.show()
    def changeSpinVal(self,val):
        self.spin.setValue(val)
    def changeDialVal(self,val):
        self.dial.setValue(val)
        
app=QApplication(sys.argv)
df=dialForm()
app.exec_()        