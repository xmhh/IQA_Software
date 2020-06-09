# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Warmup_Exp.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1034, 734)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Main_Exp/images/app_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("QWidget#Form{\n"
"    border-image: url(:/Warm_up/images/warm_up_bg.jpg);\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 5, 0, 0)
        self.verticalLayout.setSpacing(7)
        self.verticalLayout.setObjectName("verticalLayout")
        self.warmup_wincontrol_widget = QtWidgets.QWidget(Form)
        self.warmup_wincontrol_widget.setObjectName("warmup_wincontrol_widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.warmup_wincontrol_widget)
        self.horizontalLayout.setSpacing(16)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.warmup_wincontrol_widget)
        self.lineEdit.setStyleSheet("border:none;\n"
"background-color: transparent;")
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton_7 = QtWidgets.QPushButton(self.warmup_wincontrol_widget)
        self.pushButton_7.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_7.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_7.setToolTipDuration(700)
        self.pushButton_7.setStyleSheet("QPushButton {\n"
"    font: 20px;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(85, 170, 255);\n"
"    border-radius: 20px;\n"
"    border: 2px;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(78, 78, 234);\n"
"    border: 2px double;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(89, 203, 255);\n"
"}\n"
"")
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout.addWidget(self.pushButton_7)
        self.pushButton_9 = QtWidgets.QPushButton(self.warmup_wincontrol_widget)
        self.pushButton_9.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_9.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_9.setToolTipDuration(700)
        self.pushButton_9.setStyleSheet("QPushButton {\n"
"    font: 20px;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(85, 170, 255);\n"
"    border-radius: 20px;\n"
"    border: 2px;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(78, 78, 234);\n"
"    border: 2px double;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(89, 203, 255);\n"
"}\n"
"")
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout.addWidget(self.pushButton_9)
        self.pushButton_8 = QtWidgets.QPushButton(self.warmup_wincontrol_widget)
        self.pushButton_8.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_8.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_8.setToolTipDuration(700)
        self.pushButton_8.setStyleSheet("QPushButton {\n"
"    font: 20px;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(85, 170, 255);\n"
"    border-radius: 20px;\n"
"    border: 2px;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(78, 78, 234);\n"
"    border: 2px double;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(89, 203, 255);\n"
"}\n"
"")
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout.addWidget(self.pushButton_8)
        self.verticalLayout.addWidget(self.warmup_wincontrol_widget)
        self.warm_up_dis_widget = QtWidgets.QWidget(Form)
        self.warm_up_dis_widget.setStyleSheet("")
        self.warm_up_dis_widget.setObjectName("warm_up_dis_widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.warm_up_dis_widget)
        self.horizontalLayout_3.setContentsMargins(15, 0, 15, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.show_pic_lb = QtWidgets.QLabel(self.warm_up_dis_widget)
        self.show_pic_lb.setStyleSheet("background-color: rgb(230, 230, 230);")
        self.show_pic_lb.setText("")
        self.show_pic_lb.setObjectName("show_pic_lb")
        self.horizontalLayout_3.addWidget(self.show_pic_lb)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.show_pic_with_word_te = QtWidgets.QTextEdit(self.warm_up_dis_widget)
        self.show_pic_with_word_te.setStyleSheet("background-color: rgb(230, 230, 230);")
        self.show_pic_with_word_te.setReadOnly(True)
        self.show_pic_with_word_te.setObjectName("show_pic_with_word_te")
        self.verticalLayout_2.addWidget(self.show_pic_with_word_te)
        self.show_pic_arrow_lb = QtWidgets.QLabel(self.warm_up_dis_widget)
        self.show_pic_arrow_lb.setStyleSheet("background-color: transparent;\n"
"")
        self.show_pic_arrow_lb.setText("")
        self.show_pic_arrow_lb.setObjectName("show_pic_arrow_lb")
        self.verticalLayout_2.addWidget(self.show_pic_arrow_lb)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.warm_up_dis_widget)
        self.label_3.setStyleSheet("background-color: transparent;\n"
"font: 20pt \"黑体\" Bold;\n"
"color: rgb(255, 255, 255);\n"
"border: none;")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.show_score_dial = QtWidgets.QDial(self.warm_up_dis_widget)
        self.show_score_dial.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.show_score_dial.setStyleSheet("")
        self.show_score_dial.setObjectName("show_score_dial")
        self.gridLayout.addWidget(self.show_score_dial, 0, 1, 2, 1)
        self.show_score_lcd = QtWidgets.QLCDNumber(self.warm_up_dis_widget)
        self.show_score_lcd.setStyleSheet("border: none;")
        self.show_score_lcd.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.show_score_lcd.setObjectName("show_score_lcd")
        self.gridLayout.addWidget(self.show_score_lcd, 1, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout_2.setStretch(0, 8)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_3.setStretch(0, 8)
        self.horizontalLayout_3.setStretch(1, 3)
        self.verticalLayout.addWidget(self.warm_up_dis_widget)
        self.warmup_btnchoice_widget = QtWidgets.QWidget(Form)
        self.warmup_btnchoice_widget.setStyleSheet("")
        self.warmup_btnchoice_widget.setObjectName("warmup_btnchoice_widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.warmup_btnchoice_widget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.start_watch_anima_btn = QtWidgets.QPushButton(self.warmup_btnchoice_widget)
        self.start_watch_anima_btn.setMinimumSize(QtCore.QSize(200, 50))
        self.start_watch_anima_btn.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.start_watch_anima_btn.setFont(font)
        self.start_watch_anima_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.start_watch_anima_btn.setStyleSheet("QPushButton {\n"
"    font: 18px;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(147, 151, 158);\n"
"    border-radius: 25px;\n"
"    border: 2px;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(68, 68, 66);\n"
"    border: 2px double;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(141, 141, 151);\n"
"}")
        self.start_watch_anima_btn.setCheckable(True)
        self.start_watch_anima_btn.setChecked(False)
        self.start_watch_anima_btn.setObjectName("start_watch_anima_btn")
        self.horizontalLayout_2.addWidget(self.start_watch_anima_btn)
        self.start_watch_anima_btn_2 = QtWidgets.QPushButton(self.warmup_btnchoice_widget)
        self.start_watch_anima_btn_2.setMinimumSize(QtCore.QSize(200, 50))
        self.start_watch_anima_btn_2.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.start_watch_anima_btn_2.setFont(font)
        self.start_watch_anima_btn_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.start_watch_anima_btn_2.setStyleSheet("QPushButton {\n"
"    font: 18px;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(147, 151, 158);\n"
"    border-radius: 25px;\n"
"    border: 2px;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(68, 68, 66);\n"
"    border: 2px double;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(141, 141, 151);\n"
"}")
        self.start_watch_anima_btn_2.setCheckable(True)
        self.start_watch_anima_btn_2.setChecked(False)
        self.start_watch_anima_btn_2.setObjectName("start_watch_anima_btn_2")
        self.horizontalLayout_2.addWidget(self.start_watch_anima_btn_2)
        self.pushButton_5 = QtWidgets.QPushButton(self.warmup_btnchoice_widget)
        self.pushButton_5.setMinimumSize(QtCore.QSize(200, 50))
        self.pushButton_5.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet("QPushButton {\n"
"    font: 18px;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(147, 151, 158);\n"
"    border-radius: 25px;\n"
"    border: 2px;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(68, 68, 66);\n"
"    border: 2px double;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(141, 141, 151);\n"
"}")
        self.pushButton_5.setCheckable(True)
        self.pushButton_5.setChecked(False)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_2.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.warmup_btnchoice_widget)
        self.pushButton_6.setMinimumSize(QtCore.QSize(200, 50))
        self.pushButton_6.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_6.setStyleSheet("QPushButton {\n"
"    font: 18px;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(147, 151, 158);\n"
"    border-radius: 25px;\n"
"    border: 2px;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(68, 68, 66);\n"
"    border: 2px double;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(141, 141, 151);\n"
"}")
        self.pushButton_6.setCheckable(True)
        self.pushButton_6.setChecked(False)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_2.addWidget(self.pushButton_6)
        self.verticalLayout.addWidget(self.warmup_btnchoice_widget)
        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 20)
        self.verticalLayout.setStretch(2, 3)

        self.retranslateUi(Form)
        self.pushButton_7.clicked.connect(Form.warmup_min)
        self.pushButton_9.clicked.connect(Form.warmup_max)
        self.pushButton_8.clicked.connect(Form.warmup_close)
        self.start_watch_anima_btn.clicked.connect(Form.start_warmup_animation)
        self.pushButton_5.clicked.connect(Form.jump_from_warmup_to_mainexp)
        self.pushButton_6.clicked.connect(Form.jump_from_warmup_to_getinfo)
        self.start_watch_anima_btn_2.clicked.connect(Form.restart_warmup_animation)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_7.setToolTip(_translate("Form", "<html><head/><body><p>最小化</p></body></html>"))
        self.pushButton_7.setText(_translate("Form", "—"))
        self.pushButton_9.setToolTip(_translate("Form", "<html><head/><body><p>最大化</p></body></html>"))
        self.pushButton_9.setText(_translate("Form", "口"))
        self.pushButton_8.setToolTip(_translate("Form", "关闭"))
        self.pushButton_8.setText(_translate("Form", "X"))
        self.show_pic_with_word_te.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_3.setText(_translate("Form", "主观评分："))
        self.start_watch_anima_btn.setText(_translate("Form", "开始演示动画1"))
        self.start_watch_anima_btn_2.setText(_translate("Form", "继续动画2"))
        self.pushButton_5.setText(_translate("Form", "我已明白，下一步"))
        self.pushButton_6.setText(_translate("Form", "上一步"))
import images_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
