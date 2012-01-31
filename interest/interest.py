'''
Created on Jan 31, 2012

@author: saurabh
'''

#Q/usr/bin/python
# A GUI app to calculate Compound Interest

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

class CalcInterest(QDialog):
    def __init__(self,parent=None):
        super(CalcInterest,self).__init__(parent)
        self.years=5.00
        self.row1=QHBoxLayout()
        self.row2=QHBoxLayout()
        self.row3=QHBoxLayout()
        self.row4=QHBoxLayout()
        self.mainLayout=QVBoxLayout()
        self.lblPricipal=QLabel("<b>Principal: </b>")
        self.lblRate=QLabel("<b>Rate: </b>")
        self.lblYears=QLabel("<b>Years: </b>")
        self.lblResult=QLabel("<b>Amount is: ")
        self.lblFinal=QLabel()
        self.spinP=QDoubleSpinBox()
        self.spinI=QDoubleSpinBox()
        self.comboYears=QComboBox()
        self.spinP.setRange(1000.00,1000000.00)
        self.spinP.setPrefix("$ ")
        self.spinI.setRange(1.25,20.00)
        self.spinI.setSuffix(" % ")
        list=QStringList()
        list.append(QString("1 year"))
        for x in range(2,20):
            list.append(QString("%1 years").arg(x))
        self.comboYears.addItems(list)
        self.row1.addWidget(self.lblPricipal)
        self.row1.addWidget(self.spinP)
        self.row2.addWidget(self.lblRate)
        self.row2.addWidget(self.spinI)
        self.row3.addWidget(self.lblYears)
        self.row3.addWidget(self.comboYears)
        self.row4.addWidget(self.lblResult)
        self.row4.addWidget(self.lblFinal)
        self.mainLayout.addLayout(self.row1)
        self.mainLayout.addLayout(self.row2)
        self.mainLayout.addLayout(self.row3)
        self.mainLayout.addLayout(self.row4)
        self.setLayout(self.mainLayout)
        self.setWindowTitle("Compound Interest")
        self.connect(self.spinI, SIGNAL("valueChanged(double)"),self.updateUi)
        self.connect(self.spinP, SIGNAL("valueChanged(double)"),self.updateUi)
        self.connect(self.comboYears,SIGNAL("activated(QString)"),self.setTime)
        self.show()
        
    def updateUi(self):                                         #called each time either spinbox is changed
        principal=self.spinP.value()
        print principal
        interest=self.spinI.value()
        print interest
        result=(((interest/100)+1)**self.years)*principal       #calculate the final amount
        self.lblFinal.setText(QString("%1").arg(result))        #display amount in the result field
    
    def setTime(self,val):
        stlist=QStringList(QString(val).split(" "))
        self.years=int(stlist.first())
        self.updateUi()
        print self.years
app=QApplication(sys.argv)
i=CalcInterest()
i.updateUi()
app.exec_()