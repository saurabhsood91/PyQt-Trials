# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'txtedit.ui'
#
# Created by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.buttonOpen = QtGui.QPushButton(self.centralwidget)
        self.buttonOpen.setGeometry(QtCore.QRect(20, 10, 90, 23))
        self.buttonOpen.setText(QtGui.QApplication.translate("MainWindow", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonOpen.setObjectName(_fromUtf8("buttonOpen"))
        self.buttonClose = QtGui.QPushButton(self.centralwidget)
        self.buttonClose.setGeometry(QtCore.QRect(260, 10, 90, 23))
        self.buttonClose.setText(QtGui.QApplication.translate("MainWindow", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonClose.setObjectName(_fromUtf8("buttonClose"))
        self.textWindow = QtGui.QTextEdit(self.centralwidget)
        self.textWindow.setGeometry(QtCore.QRect(10, 50, 681, 481))
        self.textWindow.setObjectName(_fromUtf8("textWindow"))
        self.buttonSave = QtGui.QPushButton(self.centralwidget)
        self.buttonSave.setGeometry(QtCore.QRect(140, 10, 90, 23))
        self.buttonSave.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonSave.setObjectName(_fromUtf8("buttonSave"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.buttonClose, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        pass

