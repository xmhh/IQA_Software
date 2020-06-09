# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main_Experiment.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1115, 741)
        Form.setStyleSheet("border: 2px double;")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout.setSpacing(7)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.display_widget = QtWidgets.QWidget(Form)
        self.display_widget.setStyleSheet("border-color: rgb(238, 238, 238);")
        self.display_widget.setObjectName("display_widget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.display_widget)
        self.gridLayout_4.setContentsMargins(20, 20, 20, 20)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_4 = QtWidgets.QLabel(self.display_widget)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.display_widget)
        self.tool_widget = QtWidgets.QVBoxLayout()
        self.tool_widget.setSpacing(0)
        self.tool_widget.setObjectName("tool_widget")
        self.thumbnail_widget = QtWidgets.QWidget(Form)
        self.thumbnail_widget.setMaximumSize(QtCore.QSize(500, 16777215))
        self.thumbnail_widget.setStyleSheet("")
        self.thumbnail_widget.setObjectName("thumbnail_widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.thumbnail_widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Thumbnail_pic_lb = QtWidgets.QLabel(self.thumbnail_widget)
        self.Thumbnail_pic_lb.setMinimumSize(QtCore.QSize(290, 0))
        self.Thumbnail_pic_lb.setMaximumSize(QtCore.QSize(600, 16777215))
        self.Thumbnail_pic_lb.setObjectName("Thumbnail_pic_lb")
        self.verticalLayout.addWidget(self.Thumbnail_pic_lb)
        self.Thumbnail_info_lb = QtWidgets.QLabel(self.thumbnail_widget)
        self.Thumbnail_info_lb.setMinimumSize(QtCore.QSize(291, 25))
        self.Thumbnail_info_lb.setMaximumSize(QtCore.QSize(600, 40))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.Thumbnail_info_lb.setFont(font)
        self.Thumbnail_info_lb.setStyleSheet("border:none;")
        self.Thumbnail_info_lb.setObjectName("Thumbnail_info_lb")
        self.verticalLayout.addWidget(self.Thumbnail_info_lb)
        self.progressBar = QtWidgets.QProgressBar(self.thumbnail_widget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(11)
        self.progressBar.setFont(font)
        self.progressBar.setProperty("value", 20)
        self.progressBar.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.tool_widget.addWidget(self.thumbnail_widget)
        self.get_score_and_goback_widget = QtWidgets.QWidget(Form)
        self.get_score_and_goback_widget.setMinimumSize(QtCore.QSize(290, 0))
        self.get_score_and_goback_widget.setMaximumSize(QtCore.QSize(600, 16777215))
        self.get_score_and_goback_widget.setStyleSheet("")
        self.get_score_and_goback_widget.setObjectName("get_score_and_goback_widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.get_score_and_goback_widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_3 = QtWidgets.QLabel(self.get_score_and_goback_widget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: transparent;\n"
"\n"
"")
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.show_score_dial = QtWidgets.QDial(self.get_score_and_goback_widget)
        self.show_score_dial.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.show_score_dial.setStyleSheet("")
        self.show_score_dial.setObjectName("show_score_dial")
        self.gridLayout_2.addWidget(self.show_score_dial, 0, 1, 2, 1)
        self.show_score_lcd = QtWidgets.QLCDNumber(self.get_score_and_goback_widget)
        self.show_score_lcd.setStyleSheet("border: none;")
        self.show_score_lcd.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.show_score_lcd.setObjectName("show_score_lcd")
        self.gridLayout_2.addWidget(self.show_score_lcd, 1, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.label = QtWidgets.QLabel(self.get_score_and_goback_widget)
        self.label.setMinimumSize(QtCore.QSize(0, 25))
        self.label.setMaximumSize(QtCore.QSize(600, 40))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.get_score_of_this_picture = QtWidgets.QPushButton(self.get_score_and_goback_widget)
        self.get_score_of_this_picture.setMinimumSize(QtCore.QSize(0, 60))
        self.get_score_of_this_picture.setMaximumSize(QtCore.QSize(600, 16777215))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.get_score_of_this_picture.setFont(font)
        self.get_score_of_this_picture.setStyleSheet("QPushButton {\n"
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
        self.get_score_of_this_picture.setObjectName("get_score_of_this_picture")
        self.verticalLayout_2.addWidget(self.get_score_of_this_picture)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setContentsMargins(0, 0, -1, -1)
        self.horizontalLayout_2.setSpacing(7)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.get_score_and_goback_widget)
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton {\n"
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
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.get_score_and_goback_widget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
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
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.setStretch(0, 4)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 2)
        self.verticalLayout_2.setStretch(3, 2)
        self.tool_widget.addWidget(self.get_score_and_goback_widget)
        self.tool_widget.setStretch(0, 1)
        self.tool_widget.setStretch(1, 1)
        self.horizontalLayout.addLayout(self.tool_widget)
        self.horizontalLayout.setStretch(0, 28)
        self.horizontalLayout.setStretch(1, 10)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_4.setText(_translate("Form", "主展示界面"))
        self.Thumbnail_pic_lb.setText(_translate("Form", "同组其他照片缩略图"))
        self.Thumbnail_info_lb.setText(_translate("Form", "当前测试进度为："))
        self.label_3.setText(_translate("Form", "主观评分为："))
        self.label.setText(_translate("Form", "当前照片为："))
        self.get_score_of_this_picture.setText(_translate("Form", "确认评分"))
        self.pushButton_3.setText(_translate("Form", "上一张"))
        self.pushButton_2.setText(_translate("Form", "下一张"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
