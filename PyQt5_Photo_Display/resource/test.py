# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(784, 510)
        self.dial = QtWidgets.QDial(Form)
        self.dial.setGeometry(QtCore.QRect(120, 90, 121, 101))
        self.dial.setObjectName("dial")
        self.lcdNumber = QtWidgets.QLCDNumber(Form)
        self.lcdNumber.setGeometry(QtCore.QRect(120, 220, 121, 51))
        self.lcdNumber.setObjectName("lcdNumber")
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(150, 40, 118, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(140, 330, 93, 28))
        self.pushButton.setStyleSheet("QPushButton:hover {\n"
"    background-color: rgb(255, 184, 155);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    \n"
"    background-color: rgb(225, 160, 58);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    \n"
"    background-color: rgb(235, 235, 235);\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(255, 115, 102);\n"
"    color: rgb(242, 222, 89);\n"
"    font: 75 10pt \"微软雅黑\";\n"
"    border-radius: 20px;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 50, 61, 81))
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 410, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(320, 120, 381, 231))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        self.dial.valueChanged['int'].connect(Form.get_dial_value)
        self.pushButton.clicked.connect(Form.change_pic)
        self.pushButton_2.clicked.connect(Form.show_pic)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "PushButton"))
        self.label.setText(_translate("Form", "TextLabel"))
        self.pushButton_2.setText(_translate("Form", "给爷显示"))
        self.label_2.setText(_translate("Form", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
