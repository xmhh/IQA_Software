# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'start_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 500)
        Form.setMinimumSize(QtCore.QSize(800, 500))
        Form.setMaximumSize(QtCore.QSize(800, 500))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Main_Exp/images/app_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("QWidget#Form{\n"
"    border-image: url(:/start/images/start_bg_2.jpg);\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(0, 0, 500, 125))
        self.lineEdit.setMinimumSize(QtCore.QSize(500, 125))
        self.lineEdit.setMaximumSize(QtCore.QSize(500, 125))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: transparent;\n"
"font: 28pt \"微软雅黑\" ;\n"
"color: rgb(255, 255, 255);\n"
"border: none;\n"
"\n"
"")
        self.lineEdit.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.layoutWidget = QtWidgets.QWidget(self.widget)
        self.layoutWidget.setGeometry(QtCore.QRect(710, 0, 89, 42))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_4.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_4.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setToolTipDuration(700)
        self.pushButton_4.setStyleSheet("QPushButton {\n"
"    font: 20px;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: transparent;\n"
"    border-radius: 20px;\n"
"    border: 2px;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(68, 68, 66);\n"
"    border: 2px double;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(141, 141, 151);\n"
"}\n"
"")
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_3.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_3.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setToolTipDuration(700)
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"    font: 20px;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: transparent;\n"
"    border-radius: 20px;\n"
"    border: 2px;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(68, 68, 66);\n"
"    border: 2px double;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(141, 141, 151);\n"
"}\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(30, 120, 461, 31))
        self.lineEdit_2.setStyleSheet("background-color: transparent;\n"
"color:rgb(255, 255, 255);\n"
"font: 17px \"Sitka Display\";\n"
"border: none;")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setStyleSheet("background-color: transparent;")
        self.widget_2.setObjectName("widget_2")
        self.pushButton = QtWidgets.QPushButton(self.widget_2)
        self.pushButton.setGeometry(QtCore.QRect(20, 150, 150, 40))
        self.pushButton.setMinimumSize(QtCore.QSize(150, 40))
        self.pushButton.setMaximumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton {\n"
"    font: 18px;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(147, 151, 158);\n"
"    border-radius: 20px;\n"
"    border: 2px;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(68, 68, 66);\n"
"    border: 2px double;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(141, 141, 151);\n"
"}")
        self.pushButton.setCheckable(True)
        self.pushButton.setChecked(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_2.setGeometry(QtCore.QRect(680, 150, 100, 40))
        self.pushButton_2.setMinimumSize(QtCore.QSize(100, 40))
        self.pushButton_2.setMaximumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    font: 18px;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(147, 151, 158);\n"
"    border-radius: 20px;\n"
"    border: 2px;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(68, 68, 66);\n"
"    border: 2px double;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(141, 141, 151);\n"
"}")
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setChecked(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.widget_2)
        self.verticalLayout.setStretch(0, 3)
        self.verticalLayout.setStretch(1, 2)

        self.retranslateUi(Form)
        self.pushButton_2.clicked.connect(Form.start_show_more_info)
        self.pushButton.clicked.connect(Form.jumpfrom_start_to_getinfo)
        self.pushButton_4.clicked.connect(Form.start_pane_min)
        self.pushButton_3.clicked.connect(Form.start_pane_close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lineEdit.setText(_translate("Form", "图像质量评价实验平台"))
        self.pushButton_4.setToolTip(_translate("Form", "<html><head/><body><p>最小化</p></body></html>"))
        self.pushButton_4.setText(_translate("Form", "—"))
        self.pushButton_3.setToolTip(_translate("Form", "关闭"))
        self.pushButton_3.setText(_translate("Form", "X"))
        self.lineEdit_2.setText(_translate("Form", "Image Subjective Quality Evaluation Experimental Platform"))
        self.pushButton.setText(_translate("Form", "开始测试准备"))
        self.pushButton_2.setText(_translate("Form", "了解更多"))
import images_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
