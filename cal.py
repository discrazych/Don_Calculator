# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cal.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(424, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.outputlabel = QtWidgets.QLabel(self.centralwidget)
        self.outputlabel.setGeometry(QtCore.QRect(20, 30, 381, 71))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.outputlabel.setFont(font)
        self.outputlabel.setFrameShape(QtWidgets.QFrame.Box)
        self.outputlabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.outputlabel.setLineWidth(4)
        self.outputlabel.setMidLineWidth(2)
        self.outputlabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.outputlabel.setObjectName("outputlabel")
        self.ceButton = QtWidgets.QPushButton(self.centralwidget)
        self.ceButton.setGeometry(QtCore.QRect(230, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.ceButton.setFont(font)
        self.ceButton.setObjectName("ceButton")
        self.cButton = QtWidgets.QPushButton(self.centralwidget)
        self.cButton.setGeometry(QtCore.QRect(120, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.cButton.setFont(font)
        self.cButton.setObjectName("cButton")
        self.sevenButton = QtWidgets.QPushButton(self.centralwidget)
        self.sevenButton.setGeometry(QtCore.QRect(20, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.sevenButton.setFont(font)
        self.sevenButton.setObjectName("sevenButton")
        self.eightButton = QtWidgets.QPushButton(self.centralwidget)
        self.eightButton.setGeometry(QtCore.QRect(120, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.eightButton.setFont(font)
        self.eightButton.setObjectName("eightButton")
        self.nineButton = QtWidgets.QPushButton(self.centralwidget)
        self.nineButton.setGeometry(QtCore.QRect(230, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.nineButton.setFont(font)
        self.nineButton.setObjectName("nineButton")
        self.divideButton = QtWidgets.QPushButton(self.centralwidget)
        self.divideButton.setGeometry(QtCore.QRect(330, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.divideButton.setFont(font)
        self.divideButton.setObjectName("divideButton")
        self.fourButton = QtWidgets.QPushButton(self.centralwidget)
        self.fourButton.setGeometry(QtCore.QRect(20, 290, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.fourButton.setFont(font)
        self.fourButton.setObjectName("fourButton")
        self.fiveButton = QtWidgets.QPushButton(self.centralwidget)
        self.fiveButton.setGeometry(QtCore.QRect(120, 290, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.fiveButton.setFont(font)
        self.fiveButton.setObjectName("fiveButton")
        self.sixButton = QtWidgets.QPushButton(self.centralwidget)
        self.sixButton.setGeometry(QtCore.QRect(230, 290, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.sixButton.setFont(font)
        self.sixButton.setObjectName("sixButton")
        self.multiplyButton = QtWidgets.QPushButton(self.centralwidget)
        self.multiplyButton.setGeometry(QtCore.QRect(330, 290, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.multiplyButton.setFont(font)
        self.multiplyButton.setObjectName("multiplyButton")
        self.oneButton = QtWidgets.QPushButton(self.centralwidget)
        self.oneButton.setGeometry(QtCore.QRect(20, 380, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.oneButton.setFont(font)
        self.oneButton.setObjectName("oneButton")
        self.twoButton = QtWidgets.QPushButton(self.centralwidget)
        self.twoButton.setGeometry(QtCore.QRect(120, 380, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.twoButton.setFont(font)
        self.twoButton.setObjectName("twoButton")
        self.threeButton = QtWidgets.QPushButton(self.centralwidget)
        self.threeButton.setGeometry(QtCore.QRect(230, 380, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.threeButton.setFont(font)
        self.threeButton.setObjectName("threeButton")
        self.plusButton = QtWidgets.QPushButton(self.centralwidget)
        self.plusButton.setGeometry(QtCore.QRect(330, 380, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.plusButton.setFont(font)
        self.plusButton.setObjectName("plusButton")
        self.decimal = QtWidgets.QPushButton(self.centralwidget)
        self.decimal.setGeometry(QtCore.QRect(20, 470, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.decimal.setFont(font)
        self.decimal.setObjectName("decimal")
        self.equalButton = QtWidgets.QPushButton(self.centralwidget)
        self.equalButton.setGeometry(QtCore.QRect(230, 470, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.equalButton.setFont(font)
        self.equalButton.setObjectName("equalButton")
        self.minusButton = QtWidgets.QPushButton(self.centralwidget)
        self.minusButton.setGeometry(QtCore.QRect(330, 470, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.minusButton.setFont(font)
        self.minusButton.setObjectName("minusButton")
        self.zeroButton = QtWidgets.QPushButton(self.centralwidget)
        self.zeroButton.setGeometry(QtCore.QRect(120, 470, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.zeroButton.setFont(font)
        self.zeroButton.setObjectName("zeroButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 424, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.outputlabel.setText(_translate("MainWindow", "0"))
        self.ceButton.setText(_translate("MainWindow", "CE"))
        self.cButton.setText(_translate("MainWindow", "C"))
        self.sevenButton.setText(_translate("MainWindow", "7"))
        self.eightButton.setText(_translate("MainWindow", "8"))
        self.nineButton.setText(_translate("MainWindow", "9"))
        self.divideButton.setText(_translate("MainWindow", "/"))
        self.fourButton.setText(_translate("MainWindow", "4"))
        self.fiveButton.setText(_translate("MainWindow", "5"))
        self.sixButton.setText(_translate("MainWindow", "6"))
        self.multiplyButton.setText(_translate("MainWindow", "x"))
        self.oneButton.setText(_translate("MainWindow", "1"))
        self.twoButton.setText(_translate("MainWindow", "2"))
        self.threeButton.setText(_translate("MainWindow", "3"))
        self.plusButton.setText(_translate("MainWindow", "+"))
        self.decimal.setText(_translate("MainWindow", "."))
        self.equalButton.setText(_translate("MainWindow", "="))
        self.minusButton.setText(_translate("MainWindow", "-"))
        self.zeroButton.setText(_translate("MainWindow", "0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
