# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Settings.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1140, 611)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Main_Exp/images/app_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setContentsMargins(5, -1, -1, -1)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.setting_listWidget = QtWidgets.QListWidget(Form)
        self.setting_listWidget.setMinimumSize(QtCore.QSize(125, 0))
        self.setting_listWidget.setMaximumSize(QtCore.QSize(165, 16777215))
        self.setting_listWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.setting_listWidget.setStyleSheet("#setting_listWidget {\n"
"    font: 16px \"黑体\";\n"
"    outline: 0px;\n"
"    max-width: 165px;\n"
"    background-color: rgb(250, 250, 250);\n"
"}\n"
"\n"
"#setting_listWidget::item {\n"
"    min-height: 45px;\n"
"}\n"
"\n"
"#setting_listWidget::item:hover {\n"
"    background-color: rgb(225, 230, 235);\n"
"}\n"
"\n"
"#setting_listWidget::item:selected {\n"
"    color: white;\n"
"    background:qlineargradient(spread:pad,x1:0,y1:0,x2:1,y2:0,stop:0 #4568dc,stop:1 #b06ab3);border-top-left-radius:2px;border-top-right-radius:2px;\n"
"}")
        self.setting_listWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.setting_listWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setting_listWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setting_listWidget.setTextElideMode(QtCore.Qt.ElideLeft)
        self.setting_listWidget.setItemAlignment(QtCore.Qt.AlignCenter)
        self.setting_listWidget.setObjectName("setting_listWidget")
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.setting_listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.setting_listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.setting_listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.setting_listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.setting_listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.setting_listWidget.addItem(item)
        self.horizontalLayout.addWidget(self.setting_listWidget)
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setStyleSheet("")
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 941, 2997))
        self.scrollAreaWidgetContents.setStyleSheet("")
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_35 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_35.setContentsMargins(-1, 10, -1, 100)
        self.verticalLayout_35.setSpacing(30)
        self.verticalLayout_35.setObjectName("verticalLayout_35")
        self.widget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget.setMinimumSize(QtCore.QSize(0, 0))
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.verticalLayout_35.addWidget(self.widget)
        self.database_gbox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.database_gbox.setStyleSheet("QGroupBox {\n"
"    font: 25px \"黑体\";\n"
"    border:none;\n"
"    background-color: rgb(250, 250, 250);\n"
"    border-radius:6px;\n"
"    margin-top:12px;\n"
"}\n"
"QGroupBox:title {\n"
"    color:rgb(28, 120, 167);\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"}")
        self.database_gbox.setObjectName("database_gbox")
        self.verticalLayout_28 = QtWidgets.QVBoxLayout(self.database_gbox)
        self.verticalLayout_28.setContentsMargins(-1, 50, -1, 50)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        self.label_28 = QtWidgets.QLabel(self.database_gbox)
        self.label_28.setText("")
        self.label_28.setObjectName("label_28")
        self.verticalLayout_28.addWidget(self.label_28)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.database_gbox)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("border:none;\n"
"font: 12pt \"黑体\";")
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.database_gbox)
        self.label_2.setStyleSheet("color: rgb(135, 135, 135);\n"
"font: 10pt \"黑体\";")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.horizontalLayout_2.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEdit = QtWidgets.QLineEdit(self.database_gbox)
        self.lineEdit.setMinimumSize(QtCore.QSize(150, 22))
        self.lineEdit.setMaximumSize(QtCore.QSize(150, 22))
        self.lineEdit.setStyleSheet("border:none;\n"
"font: 10pt \"Microsoft YaHei UI\";\n"
"background-color: rgb(240, 240, 240);\n"
"border-radius:10px;")
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_3.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.database_gbox)
        self.pushButton.setMinimumSize(QtCore.QSize(70, 30))
        self.pushButton.setMaximumSize(QtCore.QSize(70, 30))
        self.pushButton.setStyleSheet("QPushButton:hover {\n"
"    background-color: rgb(58, 189, 236);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    \n"
"    background-color: rgb(27, 87, 126);\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(28, 120, 167);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 10pt \"黑体\";\n"
"    border-radius: 12px;\n"
"    border: 10px;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.label_51 = QtWidgets.QLabel(self.database_gbox)
        self.label_51.setText("")
        self.label_51.setObjectName("label_51")
        self.horizontalLayout_3.addWidget(self.label_51)
        self.horizontalLayout_3.setStretch(2, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_28.addLayout(self.verticalLayout)
        self.verticalLayout_35.addWidget(self.database_gbox)
        self.label_46 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_46.setMinimumSize(QtCore.QSize(0, 50))
        self.label_46.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_46.setStyleSheet("color: rgb(173, 173, 173);")
        self.label_46.setObjectName("label_46")
        self.verticalLayout_35.addWidget(self.label_46)
        self.mos_gbox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.mos_gbox.setStyleSheet("QGroupBox {\n"
"    font: 25px \"黑体\";\n"
"    border: none;\n"
"    background-color: rgb(250, 250, 250);\n"
"    border-radius:6px;\n"
"    margin-top:12px;\n"
"}\n"
"QGroupBox:title {\n"
"    color:rgb(28, 120, 167);\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"}")
        self.mos_gbox.setObjectName("mos_gbox")
        self.verticalLayout_31 = QtWidgets.QVBoxLayout(self.mos_gbox)
        self.verticalLayout_31.setContentsMargins(-1, 50, -1, 50)
        self.verticalLayout_31.setSpacing(6)
        self.verticalLayout_31.setObjectName("verticalLayout_31")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setSpacing(30)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_3 = QtWidgets.QLabel(self.mos_gbox)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("border:none;\n"
"font: 12pt \"黑体\";")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_6.addWidget(self.label_3)
        self.label_5 = QtWidgets.QLabel(self.mos_gbox)
        self.label_5.setStyleSheet("color: rgb(135, 135, 135);\n"
"font: 10pt \"黑体\";")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.horizontalLayout_6.setStretch(1, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.comboBox = QtWidgets.QComboBox(self.mos_gbox)
        self.comboBox.setMinimumSize(QtCore.QSize(200, 0))
        self.comboBox.setMaximumSize(QtCore.QSize(200, 16777215))
        self.comboBox.setStyleSheet("QComboBox {\n"
"    border: 1px solid #bebebe;\n"
"    padding: 1px 18px 1px 3px;\n"
"    font: normal normal 13px \"Microsoft YaHei\";\n"
"    color: #555555;\n"
"    background: transparent;\n"
"    border-radius:10px;\n"
"}\n"
" \n"
" \n"
"QComboBox:editable{\n"
"    background: transparent;\n"
"}\n"
" \n"
"QComboBox:!on{\n"
"}\n"
" \n"
"QComboBox:on{ /* the popup opens */\n"
"    color: #555555;\n"
"    border-color: #327cc0;\n"
"    background: transparent;\n"
"}\n"
" \n"
"QComboBox QAbstractItemView {\n"
"    outline: 0; \n"
"    border: 1px solid #327cc0;\n"
"    background-color: #F1F3F3;\n"
"    font: normal normal 14px \"Microsoft YaHei\";\n"
"}\n"
" \n"
"QComboBox QAbstractItemView::item {\n"
"    height: 15px;\n"
"    color: #555555;\n"
"    background-color: transparent;\n"
"}\n"
" \n"
"QComboBox QAbstractItemView::item:hover {\n"
"    color: #FFFFFF;\n"
"    background-color: #327cc0;\n"
"}\n"
" \n"
"QComboBox QAbstractItemView::item:selected {\n"
"    color: #FFFFFF;\n"
"    background-color: #327cc0;\n"
"}\n"
" \n"
"QComboBox QAbstractScrollArea QScrollBar:vertical {\n"
"    background-color: #d0d2d4;\n"
"}\n"
" \n"
"QComboBox QAbstractScrollArea QScrollBar::handle:vertical {\n"
"    background: rgb(160,160,160);\n"
"}\n"
" \n"
"QComboBox QAbstractScrollArea QScrollBar::handle:vertical:hover {\n"
"    background: rgb(90, 91, 93);\n"
"}")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_4.addWidget(self.comboBox)
        self.label_29 = QtWidgets.QLabel(self.mos_gbox)
        self.label_29.setText("")
        self.label_29.setObjectName("label_29")
        self.horizontalLayout_4.addWidget(self.label_29)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.verticalLayout_12.addLayout(self.verticalLayout_2)
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setSpacing(10)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_4 = QtWidgets.QLabel(self.mos_gbox)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("border:none;\n"
"font: 12pt \"黑体\";")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_11.addWidget(self.label_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.mos_gbox)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(150, 22))
        self.lineEdit_3.setMaximumSize(QtCore.QSize(150, 22))
        self.lineEdit_3.setStyleSheet("border:none;\n"
"font: 10pt \"Microsoft YaHei UI\";\n"
"background-color: rgb(240, 240, 240);\n"
"border-radius:10px;")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_5.addWidget(self.lineEdit_3)
        self.pushButton_3 = QtWidgets.QPushButton(self.mos_gbox)
        self.pushButton_3.setMinimumSize(QtCore.QSize(70, 30))
        self.pushButton_3.setMaximumSize(QtCore.QSize(70, 30))
        self.pushButton_3.setStyleSheet("QPushButton:hover {\n"
"    background-color: rgb(58, 189, 236);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    \n"
"    background-color: rgb(27, 87, 126);\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(28, 120, 167);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 10pt \"黑体\";\n"
"    border-radius: 12px;\n"
"    border: 10px;\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_5.addWidget(self.pushButton_3)
        self.verticalLayout_11.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_26.addLayout(self.verticalLayout_11)
        self.label_30 = QtWidgets.QLabel(self.mos_gbox)
        self.label_30.setText("")
        self.label_30.setObjectName("label_30")
        self.horizontalLayout_26.addWidget(self.label_30)
        self.horizontalLayout_26.setStretch(1, 1)
        self.verticalLayout_12.addLayout(self.horizontalLayout_26)
        self.verticalLayout_31.addLayout(self.verticalLayout_12)
        self.verticalLayout_35.addWidget(self.mos_gbox)
        self.label_47 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_47.setMinimumSize(QtCore.QSize(0, 50))
        self.label_47.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_47.setStyleSheet("color: rgb(173, 173, 173);")
        self.label_47.setObjectName("label_47")
        self.verticalLayout_35.addWidget(self.label_47)
        self.exp_gbox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.exp_gbox.setStyleSheet("QGroupBox {\n"
"    font: 25px \"黑体\";\n"
"    border: none;\n"
"    background-color: rgb(250, 250, 250);\n"
"    border-radius:6px;\n"
"    margin-top:12px;\n"
"}\n"
"QGroupBox:title {\n"
"    color:rgb(28, 120, 167);\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"}")
        self.exp_gbox.setObjectName("exp_gbox")
        self.verticalLayout_34 = QtWidgets.QVBoxLayout(self.exp_gbox)
        self.verticalLayout_34.setContentsMargins(-1, 50, -1, 50)
        self.verticalLayout_34.setObjectName("verticalLayout_34")
        self.verticalLayout_33 = QtWidgets.QVBoxLayout()
        self.verticalLayout_33.setSpacing(30)
        self.verticalLayout_33.setObjectName("verticalLayout_33")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout()
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.label_6 = QtWidgets.QLabel(self.exp_gbox)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("border:none;\n"
"font: 12pt \"黑体\";")
        self.label_6.setObjectName("label_6")
        self.verticalLayout_20.addWidget(self.label_6)
        self.verticalLayout_30 = QtWidgets.QVBoxLayout()
        self.verticalLayout_30.setSpacing(20)
        self.verticalLayout_30.setObjectName("verticalLayout_30")
        self.horizontalLayout_46 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_46.setSpacing(30)
        self.horizontalLayout_46.setObjectName("horizontalLayout_46")
        self.label_60 = QtWidgets.QLabel(self.exp_gbox)
        self.label_60.setStyleSheet("border:none;\n"
"font: 12pt \"黑体\";")
        self.label_60.setObjectName("label_60")
        self.horizontalLayout_46.addWidget(self.label_60, 0, QtCore.Qt.AlignHCenter)
        self.label_61 = QtWidgets.QLabel(self.exp_gbox)
        self.label_61.setStyleSheet("border:none;\n"
"font: 12pt \"黑体\";")
        self.label_61.setObjectName("label_61")
        self.horizontalLayout_46.addWidget(self.label_61, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_30.addLayout(self.horizontalLayout_46)
        self.horizontalLayout_45 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_45.setSpacing(10)
        self.horizontalLayout_45.setObjectName("horizontalLayout_45")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_16.setSpacing(15)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_27.setContentsMargins(20, -1, -1, -1)
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_7 = QtWidgets.QLabel(self.exp_gbox)
        self.label_7.setStyleSheet("border:none;\n"
"font: 10pt \"黑体\";")
        self.label_7.setObjectName("label_7")
        self.verticalLayout_3.addWidget(self.label_7)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(20, -1, -1, -1)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalSlider = QtWidgets.QSlider(self.exp_gbox)
        self.horizontalSlider.setMinimumSize(QtCore.QSize(233, 15))
        self.horizontalSlider.setMaximumSize(QtCore.QSize(233, 16777215))
        self.horizontalSlider.setStyleSheet("QSlider:horizontal {\n"
"    min-height: 15px;\n"
"}\n"
"QSlider::groove:horizontal {\n"
"    height: 2px;\n"
"    background: rgb(222, 222, 222); \n"
"}\n"
"QSlider::handle:horizontal {\n"
"    width: 18px;\n"
"    margin-top: -9px;\n"
"    margin-bottom: -9px;\n"
"    border-radius: 9px;\n"
"    background: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.6 rgba(28, 120, 167, 255), stop:0.7 rgba(210, 210, 210, 100));\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.6 rgba(126, 161, 255, 255), stop:0.7 rgba(255, 255, 255, 100));\n"
"}")
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setMaximum(20)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalLayout_7.addWidget(self.horizontalSlider)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.exp_gbox)
        self.lineEdit_4.setEnabled(False)
        self.lineEdit_4.setMinimumSize(QtCore.QSize(60, 22))
        self.lineEdit_4.setMaximumSize(QtCore.QSize(60, 22))
        self.lineEdit_4.setStyleSheet("border:none;\n"
"font: 11pt \"Microsoft YaHei UI\";\n"
"background-color: rgb(240, 240, 240);\n"
"border-radius:10px;")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_7.addWidget(self.lineEdit_4)
        self.pushButton_4 = QtWidgets.QPushButton(self.exp_gbox)
        self.pushButton_4.setMinimumSize(QtCore.QSize(70, 30))
        self.pushButton_4.setMaximumSize(QtCore.QSize(70, 30))
        self.pushButton_4.setStyleSheet("QPushButton:hover {\n"
"    background-color: rgb(58, 189, 236);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    \n"
"    background-color: rgb(27, 87, 126);\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(28, 120, 167);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 10pt \"黑体\";\n"
"    border-radius: 12px;\n"
"    border: 10px;\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_7.addWidget(self.pushButton_4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_27.addLayout(self.verticalLayout_3)
        self.label_31 = QtWidgets.QLabel(self.exp_gbox)
        self.label_31.setText("")
        self.label_31.setObjectName("label_31")
        self.horizontalLayout_27.addWidget(self.label_31)
        self.horizontalLayout_27.setStretch(1, 1)
        self.verticalLayout_16.addLayout(self.horizontalLayout_27)
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_28.setContentsMargins(20, -1, -1, -1)
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_8 = QtWidgets.QLabel(self.exp_gbox)
        self.label_8.setStyleSheet("border:none;\n"
"font: 10pt \"黑体\";")
        self.label_8.setObjectName("label_8")
        self.verticalLayout_13.addWidget(self.label_8)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setContentsMargins(20, -1, -1, -1)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.horizontalSlider_2 = QtWidgets.QSlider(self.exp_gbox)
        self.horizontalSlider_2.setMinimumSize(QtCore.QSize(233, 15))
        self.horizontalSlider_2.setMaximumSize(QtCore.QSize(233, 16777215))
        self.horizontalSlider_2.setStyleSheet("QSlider:horizontal {\n"
"    min-height: 15px;\n"
"}\n"
"QSlider::groove:horizontal {\n"
"    height: 2px;\n"
"    background: rgb(222, 222, 222); \n"
"}\n"
"QSlider::handle:horizontal {\n"
"    width: 18px;\n"
"    margin-top: -9px;\n"
"    margin-bottom: -9px;\n"
"    border-radius: 9px;\n"
"    background: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.6 rgba(28, 120, 167, 255), stop:0.7 rgba(210, 210, 210, 100));\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.6 rgba(126, 161, 255, 255), stop:0.7 rgba(255, 255, 255, 100));\n"
"}")
        self.horizontalSlider_2.setMinimum(1)
        self.horizontalSlider_2.setMaximum(20)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.horizontalLayout_11.addWidget(self.horizontalSlider_2)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.exp_gbox)
        self.lineEdit_5.setEnabled(False)
        self.lineEdit_5.setMinimumSize(QtCore.QSize(60, 22))
        self.lineEdit_5.setMaximumSize(QtCore.QSize(60, 22))
        self.lineEdit_5.setStyleSheet("border:none;\n"
"font: 11pt \"Microsoft YaHei UI\";\n"
"background-color: rgb(240, 240, 240);\n"
"border-radius:10px;")
        self.lineEdit_5.setReadOnly(True)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout_11.addWidget(self.lineEdit_5)
        self.pushButton_5 = QtWidgets.QPushButton(self.exp_gbox)
        self.pushButton_5.setMinimumSize(QtCore.QSize(70, 30))
        self.pushButton_5.setMaximumSize(QtCore.QSize(70, 30))
        self.pushButton_5.setStyleSheet("QPushButton:hover {\n"
"    background-color: rgb(58, 189, 236);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    \n"
"    background-color: rgb(27, 87, 126);\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(28, 120, 167);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 10pt \"黑体\";\n"
"    border-radius: 12px;\n"
"    border: 10px;\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_11.addWidget(self.pushButton_5)
        self.verticalLayout_13.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_28.addLayout(self.verticalLayout_13)
        self.label_32 = QtWidgets.QLabel(self.exp_gbox)
        self.label_32.setText("")
        self.label_32.setObjectName("label_32")
        self.horizontalLayout_28.addWidget(self.label_32)
        self.horizontalLayout_28.setStretch(1, 1)
        self.verticalLayout_16.addLayout(self.horizontalLayout_28)
        self.horizontalLayout_29 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_29.setContentsMargins(20, -1, -1, -1)
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_10 = QtWidgets.QLabel(self.exp_gbox)
        self.label_10.setStyleSheet("border:none;\n"
"font: 10pt \"黑体\";")
        self.label_10.setObjectName("label_10")
        self.verticalLayout_14.addWidget(self.label_10)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setContentsMargins(20, -1, -1, -1)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.horizontalSlider_3 = QtWidgets.QSlider(self.exp_gbox)
        self.horizontalSlider_3.setMinimumSize(QtCore.QSize(233, 15))
        self.horizontalSlider_3.setMaximumSize(QtCore.QSize(233, 16777215))
        self.horizontalSlider_3.setStyleSheet("QSlider:horizontal {\n"
"    min-height: 15px;\n"
"}\n"
"QSlider::groove:horizontal {\n"
"    height: 2px;\n"
"    background: rgb(222, 222, 222); \n"
"}\n"
"QSlider::handle:horizontal {\n"
"    width: 18px;\n"
"    margin-top: -9px;\n"
"    margin-bottom: -9px;\n"
"    border-radius: 9px;\n"
"    background: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.6 rgba(28, 120, 167, 255), stop:0.7 rgba(210, 210, 210, 100));\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.6 rgba(126, 161, 255, 255), stop:0.7 rgba(255, 255, 255, 100));\n"
"}")
        self.horizontalSlider_3.setMinimum(1)
        self.horizontalSlider_3.setMaximum(20)
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")
        self.horizontalLayout_10.addWidget(self.horizontalSlider_3)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.exp_gbox)
        self.lineEdit_7.setEnabled(False)
        self.lineEdit_7.setMinimumSize(QtCore.QSize(60, 22))
        self.lineEdit_7.setMaximumSize(QtCore.QSize(60, 22))
        self.lineEdit_7.setStyleSheet("border:none;\n"
"font: 11pt \"Microsoft YaHei UI\";\n"
"background-color: rgb(240, 240, 240);\n"
"border-radius:10px;")
        self.lineEdit_7.setReadOnly(True)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.horizontalLayout_10.addWidget(self.lineEdit_7)
        self.pushButton_7 = QtWidgets.QPushButton(self.exp_gbox)
        self.pushButton_7.setMinimumSize(QtCore.QSize(70, 30))
        self.pushButton_7.setMaximumSize(QtCore.QSize(70, 30))
        self.pushButton_7.setStyleSheet("QPushButton:hover {\n"
"    background-color: rgb(58, 189, 236);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    \n"
"    background-color: rgb(27, 87, 126);\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(28, 120, 167);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 10pt \"黑体\";\n"
"    border-radius: 12px;\n"
"    border: 10px;\n"
"}")
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_10.addWidget(self.pushButton_7)
        self.verticalLayout_14.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_29.addLayout(self.verticalLayout_14)
        self.label_33 = QtWidgets.QLabel(self.exp_gbox)
        self.label_33.setText("")
        self.label_33.setObjectName("label_33")
        self.horizontalLayout_29.addWidget(self.label_33)
        self.horizontalLayout_29.setStretch(1, 1)
        self.verticalLayout_16.addLayout(self.horizontalLayout_29)
        self.horizontalLayout_30 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_30.setContentsMargins(20, -1, -1, -1)
        self.horizontalLayout_30.setObjectName("horizontalLayout_30")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_11 = QtWidgets.QLabel(self.exp_gbox)
        self.label_11.setStyleSheet("border:none;\n"
"font: 10pt \"黑体\";")
        self.label_11.setObjectName("label_11")
        self.verticalLayout_15.addWidget(self.label_11)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(20, -1, -1, -1)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.horizontalSlider_4 = QtWidgets.QSlider(self.exp_gbox)
        self.horizontalSlider_4.setMinimumSize(QtCore.QSize(233, 15))
        self.horizontalSlider_4.setMaximumSize(QtCore.QSize(233, 16777215))
        self.horizontalSlider_4.setStyleSheet("QSlider:horizontal {\n"
"    min-height: 15px;\n"
"}\n"
"QSlider::groove:horizontal {\n"
"    height: 2px;\n"
"    background: rgb(222, 222, 222); \n"
"}\n"
"QSlider::handle:horizontal {\n"
"    width: 18px;\n"
"    margin-top: -9px;\n"
"    margin-bottom: -9px;\n"
"    border-radius: 9px;\n"
"    background: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.6 rgba(28, 120, 167, 255), stop:0.7 rgba(210, 210, 210, 100));\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.6 rgba(126, 161, 255, 255), stop:0.7 rgba(255, 255, 255, 100));\n"
"}")
        self.horizontalSlider_4.setMinimum(1)
        self.horizontalSlider_4.setMaximum(15)
        self.horizontalSlider_4.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_4.setObjectName("horizontalSlider_4")
        self.horizontalLayout_8.addWidget(self.horizontalSlider_4)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.exp_gbox)
        self.lineEdit_8.setEnabled(False)
        self.lineEdit_8.setMinimumSize(QtCore.QSize(60, 22))
        self.lineEdit_8.setMaximumSize(QtCore.QSize(60, 22))
        self.lineEdit_8.setStyleSheet("border:none;\n"
"font: 11pt \"Microsoft YaHei UI\";\n"
"background-color: rgb(240, 240, 240);\n"
"border-radius:10px;")
        self.lineEdit_8.setReadOnly(True)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.horizontalLayout_8.addWidget(self.lineEdit_8)
        self.pushButton_8 = QtWidgets.QPushButton(self.exp_gbox)
        self.pushButton_8.setMinimumSize(QtCore.QSize(70, 30))
        self.pushButton_8.setMaximumSize(QtCore.QSize(70, 30))
        self.pushButton_8.setStyleSheet("QPushButton:hover {\n"
"    background-color: rgb(58, 189, 236);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    \n"
"    background-color: rgb(27, 87, 126);\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(28, 120, 167);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 10pt \"黑体\";\n"
"    border-radius: 12px;\n"
"    border: 10px;\n"
"}")
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_8.addWidget(self.pushButton_8)
        self.verticalLayout_15.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_30.addLayout(self.verticalLayout_15)
        self.label_34 = QtWidgets.QLabel(self.exp_gbox)
        self.label_34.setText("")
        self.label_34.setObjectName("label_34")
        self.horizontalLayout_30.addWidget(self.label_34)
        self.horizontalLayout_30.setStretch(1, 1)
        self.verticalLayout_16.addLayout(self.horizontalLayout_30)
        self.horizontalLayout_45.addLayout(self.verticalLayout_16)
        self.label_62 = QtWidgets.QLabel(self.exp_gbox)
        self.label_62.setStyleSheet("color: rgb(191, 191, 191);")
        self.label_62.setObjectName("label_62")
        self.horizontalLayout_45.addWidget(self.label_62)
        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.verticalLayout_17.setSpacing(15)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.horizontalLayout_41 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_41.setContentsMargins(20, -1, -1, -1)
        self.horizontalLayout_41.setObjectName("horizontalLayout_41")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_53 = QtWidgets.QLabel(self.exp_gbox)
        self.label_53.setStyleSheet("border:none;\n"
"font: 10pt \"黑体\";")
        self.label_53.setObjectName("label_53")
        self.verticalLayout_10.addWidget(self.label_53)
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_23.setContentsMargins(20, -1, -1, -1)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.horizontalSlider_5 = QtWidgets.QSlider(self.exp_gbox)
        self.horizontalSlider_5.setMinimumSize(QtCore.QSize(233, 15))
        self.horizontalSlider_5.setMaximumSize(QtCore.QSize(233, 16777215))
        self.horizontalSlider_5.setStyleSheet("QSlider:horizontal {\n"
"    min-height: 15px;\n"
"}\n"
"QSlider::groove:horizontal {\n"
"    height: 2px;\n"
"    background: rgb(222, 222, 222); \n"
"}\n"
"QSlider::handle:horizontal {\n"
"    width: 18px;\n"
"    margin-top: -9px;\n"
"    margin-bottom: -9px;\n"
"    border-radius: 9px;\n"
"    background: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.6 rgba(28, 120, 167, 255), stop:0.7 rgba(210, 210, 210, 100));\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.6 rgba(126, 161, 255, 255), stop:0.7 rgba(255, 255, 255, 100));\n"
"}")
        self.horizontalSlider_5.setMinimum(1)
        self.horizontalSlider_5.setMaximum(10)
        self.horizontalSlider_5.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_5.setObjectName("horizontalSlider_5")
        self.horizontalLayout_23.addWidget(self.horizontalSlider_5)
        self.lineEdit_14 = QtWidgets.QLineEdit(self.exp_gbox)
        self.lineEdit_14.setEnabled(False)
        self.lineEdit_14.setMinimumSize(QtCore.QSize(60, 22))
        self.lineEdit_14.setMaximumSize(QtCore.QSize(60, 22))
        self.lineEdit_14.setStyleSheet("border:none;\n"
"font: 11pt \"Microsoft YaHei UI\";\n"
"background-color: rgb(240, 240, 240);\n"
"border-radius:10px;")
        self.lineEdit_14.setReadOnly(True)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.horizontalLayout_23.addWidget(self.lineEdit_14)
        self.pushButton_15 = QtWidgets.QPushButton(self.exp_gbox)
        self.pushButton_15.setMinimumSize(QtCore.QSize(70, 30))
        self.pushButton_15.setMaximumSize(QtCore.QSize(70, 30))
        self.pushButton_15.setStyleSheet("QPushButton:hover {\n"
"    background-color: rgb(58, 189, 236);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    \n"
"    background-color: rgb(27, 87, 126);\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(28, 120, 167);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 10pt \"黑体\";\n"
"    border-radius: 12px;\n"
"    border: 10px;\n"
"}")
        self.pushButton_15.setObjectName("pushButton_15")
        self.horizontalLayout_23.addWidget(self.pushButton_15)
        self.verticalLayout_10.addLayout(self.horizontalLayout_23)
        self.horizontalLayout_41.addLayout(self.verticalLayout_10)
        self.label_54 = QtWidgets.QLabel(self.exp_gbox)
        self.label_54.setText("")
        self.label_54.setObjectName("label_54")
        self.horizontalLayout_41.addWidget(self.label_54)
        self.horizontalLayout_41.setStretch(1, 1)
        self.verticalLayout_17.addLayout(self.horizontalLayout_41)
        self.horizontalLayout_42 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_42.setContentsMargins(20, -1, -1, -1)
        self.horizontalLayout_42.setObjectName("horizontalLayout_42")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout()
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.label_55 = QtWidgets.QLabel(self.exp_gbox)
        self.label_55.setStyleSheet("border:none;\n"
"font: 10pt \"黑体\";")
        self.label_55.setObjectName("label_55")
        self.verticalLayout_21.addWidget(self.label_55)
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_24.setContentsMargins(20, -1, -1, -1)
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.horizontalSlider_6 = QtWidgets.QSlider(self.exp_gbox)
        self.horizontalSlider_6.setMinimumSize(QtCore.QSize(233, 15))
        self.horizontalSlider_6.setMaximumSize(QtCore.QSize(233, 16777215))
        self.horizontalSlider_6.setStyleSheet("QSlider:horizontal {\n"
"    min-height: 15px;\n"
"}\n"
"QSlider::groove:horizontal {\n"
"    height: 2px;\n"
"    background: rgb(222, 222, 222); \n"
"}\n"
"QSlider::handle:horizontal {\n"
"    width: 18px;\n"
"    margin-top: -9px;\n"
"    margin-bottom: -9px;\n"
"    border-radius: 9px;\n"
"    background: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.6 rgba(28, 120, 167, 255), stop:0.7 rgba(210, 210, 210, 100));\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.6 rgba(126, 161, 255, 255), stop:0.7 rgba(255, 255, 255, 100));\n"
"}")
        self.horizontalSlider_6.setMinimum(1)
        self.horizontalSlider_6.setMaximum(20)
        self.horizontalSlider_6.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_6.setObjectName("horizontalSlider_6")
        self.horizontalLayout_24.addWidget(self.horizontalSlider_6)
        self.lineEdit_15 = QtWidgets.QLineEdit(self.exp_gbox)
        self.lineEdit_15.setEnabled(False)
        self.lineEdit_15.setMinimumSize(QtCore.QSize(60, 22))
        self.lineEdit_15.setMaximumSize(QtCore.QSize(60, 22))
        self.lineEdit_15.setStyleSheet("border:none;\n"
"font: 11pt \"Microsoft YaHei UI\";\n"
"background-color: rgb(240, 240, 240);\n"
"border-radius:10px;")
        self.lineEdit_15.setReadOnly(True)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.horizontalLayout_24.addWidget(self.lineEdit_15)
        self.pushButton_16 = QtWidgets.QPushButton(self.exp_gbox)
        self.pushButton_16.setMinimumSize(QtCore.QSize(70, 30))
        self.pushButton_16.setMaximumSize(QtCore.QSize(70, 30))
        self.pushButton_16.setStyleSheet("QPushButton:hover {\n"
"    background-color: rgb(58, 189, 236);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    \n"
"    background-color: rgb(27, 87, 126);\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(28, 120, 167);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 10pt \"黑体\";\n"
"    border-radius: 12px;\n"
"    border: 10px;\n"
"}")
        self.pushButton_16.setObjectName("pushButton_16")
        self.horizontalLayout_24.addWidget(self.pushButton_16)
        self.verticalLayout_21.addLayout(self.horizontalLayout_24)
        self.horizontalLayout_42.addLayout(self.verticalLayout_21)
        self.label_56 = QtWidgets.QLabel(self.exp_gbox)
        self.label_56.setText("")
        self.label_56.setObjectName("label_56")
        self.horizontalLayout_42.addWidget(self.label_56)
        self.horizontalLayout_42.setStretch(1, 1)
        self.verticalLayout_17.addLayout(self.horizontalLayout_42)
        self.horizontalLayout_43 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_43.setContentsMargins(20, -1, -1, -1)
        self.horizontalLayout_43.setObjectName("horizontalLayout_43")
        self.verticalLayout_29 = QtWidgets.QVBoxLayout()
        self.verticalLayout_29.setObjectName("verticalLayout_29")
        self.label_57 = QtWidgets.QLabel(self.exp_gbox)
        self.label_57.setStyleSheet("border:none;\n"
"font: 10pt \"黑体\";")
        self.label_57.setObjectName("label_57")
        self.verticalLayout_29.addWidget(self.label_57)
        self.horizontalLayout_44 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_44.setContentsMargins(20, -1, -1, -1)
        self.horizontalLayout_44.setObjectName("horizontalLayout_44")
        self.horizontalSlider_7 = QtWidgets.QSlider(self.exp_gbox)
        self.horizontalSlider_7.setMinimumSize(QtCore.QSize(233, 15))
        self.horizontalSlider_7.setMaximumSize(QtCore.QSize(233, 16777215))
        self.horizontalSlider_7.setStyleSheet("QSlider:horizontal {\n"
"    min-height: 15px;\n"
"}\n"
"QSlider::groove:horizontal {\n"
"    height: 2px;\n"
"    background: rgb(222, 222, 222); \n"
"}\n"
"QSlider::handle:horizontal {\n"
"    width: 18px;\n"
"    margin-top: -9px;\n"
"    margin-bottom: -9px;\n"
"    border-radius: 9px;\n"
"    background: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.6 rgba(28, 120, 167, 255), stop:0.7 rgba(210, 210, 210, 100));\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.6 rgba(126, 161, 255, 255), stop:0.7 rgba(255, 255, 255, 100));\n"
"}")
        self.horizontalSlider_7.setMinimum(1)
        self.horizontalSlider_7.setMaximum(20)
        self.horizontalSlider_7.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_7.setObjectName("horizontalSlider_7")
        self.horizontalLayout_44.addWidget(self.horizontalSlider_7)
        self.lineEdit_16 = QtWidgets.QLineEdit(self.exp_gbox)
        self.lineEdit_16.setEnabled(False)
        self.lineEdit_16.setMinimumSize(QtCore.QSize(60, 22))
        self.lineEdit_16.setMaximumSize(QtCore.QSize(60, 22))
        self.lineEdit_16.setStyleSheet("border:none;\n"
"font: 11pt \"Microsoft YaHei UI\";\n"
"background-color: rgb(240, 240, 240);\n"
"border-radius:10px;")
        self.lineEdit_16.setReadOnly(True)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.horizontalLayout_44.addWidget(self.lineEdit_16)
        self.pushButton_17 = QtWidgets.QPushButton(self.exp_gbox)
        self.pushButton_17.setMinimumSize(QtCore.QSize(70, 30))
        self.pushButton_17.setMaximumSize(QtCore.QSize(70, 30))
        self.pushButton_17.setStyleSheet("QPushButton:hover {\n"
"    background-color: rgb(58, 189, 236);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    \n"
"    background-color: rgb(27, 87, 126);\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(28, 120, 167);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 10pt \"黑体\";\n"
"    border-radius: 12px;\n"
"    border: 10px;\n"
"}")
        self.pushButton_17.setObjectName("pushButton_17")
        self.horizontalLayout_44.addWidget(self.pushButton_17)
        self.verticalLayout_29.addLayout(self.horizontalLayout_44)
        self.horizontalLayout_43.addLayout(self.verticalLayout_29)
        self.label_58 = QtWidgets.QLabel(self.exp_gbox)
        self.label_58.setText("")
        self.label_58.setObjectName("label_58")
        self.horizontalLayout_43.addWidget(self.label_58)
        self.horizontalLayout_43.setStretch(1, 1)
        self.verticalLayout_17.addLayout(self.horizontalLayout_43)
        self.label_59 = QtWidgets.QLabel(self.exp_gbox)
        self.label_59.setText("")
        self.label_59.setObjectName("label_59")
        self.verticalLayout_17.addWidget(self.label_59)
        self.horizontalLayout_45.addLayout(self.verticalLayout_17)
        self.horizontalLayout_45.setStretch(0, 1)
        self.horizontalLayout_45.setStretch(2, 1)
        self.verticalLayout_30.addLayout(self.horizontalLayout_45)
        self.verticalLayout_20.addLayout(self.verticalLayout_30)
        self.verticalLayout_33.addLayout(self.verticalLayout_20)
        self.verticalLayout_32 = QtWidgets.QVBoxLayout()
        self.verticalLayout_32.setSpacing(10)
        self.verticalLayout_32.setObjectName("verticalLayout_32")
        self.label_9 = QtWidgets.QLabel(self.exp_gbox)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("border:none;\n"
"font: 12pt \"黑体\";")
        self.label_9.setObjectName("label_9")
        self.verticalLayout_32.addWidget(self.label_9)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.comboBox_2 = QtWidgets.QComboBox(self.exp_gbox)
        self.comboBox_2.setMinimumSize(QtCore.QSize(250, 0))
        self.comboBox_2.setMaximumSize(QtCore.QSize(250, 16777215))
        self.comboBox_2.setStyleSheet("QComboBox {\n"
"    border: 1px solid #bebebe;\n"
"    padding: 1px 18px 1px 3px;\n"
"    font: normal normal 13px \"Microsoft YaHei\";\n"
"    color: #555555;\n"
"    background: transparent;\n"
"    border-radius:10px;\n"
"}\n"
" \n"
" \n"
"QComboBox:editable{\n"
"    background: transparent;\n"
"}\n"
" \n"
"QComboBox:!on{\n"
"}\n"
" \n"
"QComboBox:on{ /* the popup opens */\n"
"    color: #555555;\n"
"    border-color: #327cc0;\n"
"    background: transparent;\n"
"}\n"
" \n"
"QComboBox QAbstractItemView {\n"
"    outline: 0; \n"
"    border: 1px solid #327cc0;\n"
"    background-color: #F1F3F3;\n"
"    font: normal normal 14px \"Microsoft YaHei\";\n"
"}\n"
" \n"
"QComboBox QAbstractItemView::item {\n"
"    height: 15px;\n"
"    color: #555555;\n"
"    background-color: transparent;\n"
"}\n"
" \n"
"QComboBox QAbstractItemView::item:hover {\n"
"    color: #FFFFFF;\n"
"    background-color: #327cc0;\n"
"}\n"
" \n"
"QComboBox QAbstractItemView::item:selected {\n"
"    color: #FFFFFF;\n"
"    background-color: #327cc0;\n"
"}\n"
" \n"
"QComboBox QAbstractScrollArea QScrollBar:vertical {\n"
"    background-color: #d0d2d4;\n"
"}\n"
" \n"
"QComboBox QAbstractScrollArea QScrollBar::handle:vertical {\n"
"    background: rgb(160,160,160);\n"
"}\n"
" \n"
"QComboBox QAbstractScrollArea QScrollBar::handle:vertical:hover {\n"
"    background: rgb(90, 91, 93);\n"
"}")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.horizontalLayout_9.addWidget(self.comboBox_2)
        self.label_35 = QtWidgets.QLabel(self.exp_gbox)
        self.label_35.setText("")
        self.label_35.setObjectName("label_35")
        self.horizontalLayout_9.addWidget(self.label_35)
        self.horizontalLayout_9.setStretch(1, 1)
        self.verticalLayout_32.addLayout(self.horizontalLayout_9)
        self.verticalLayout_33.addLayout(self.verticalLayout_32)
        self.verticalLayout_34.addLayout(self.verticalLayout_33)
        self.verticalLayout_35.addWidget(self.exp_gbox)
        self.label_48 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_48.setMinimumSize(QtCore.QSize(0, 50))
        self.label_48.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_48.setStyleSheet("color: rgb(173, 173, 173);")
        self.label_48.setObjectName("label_48")
        self.verticalLayout_35.addWidget(self.label_48)
        self.photo_dis_gbox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.photo_dis_gbox.setStyleSheet("QGroupBox {\n"
"    font: 25px \"黑体\";\n"
"    border: none;\n"
"    background-color: rgb(250, 250, 250);\n"
"    border-radius:6px;\n"
"    margin-top:12px;\n"
"}\n"
"QGroupBox:title {\n"
"    color:rgb(28, 120, 167);\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"}")
        self.photo_dis_gbox.setObjectName("photo_dis_gbox")
        self.verticalLayout_24 = QtWidgets.QVBoxLayout(self.photo_dis_gbox)
        self.verticalLayout_24.setContentsMargins(-1, 50, -1, 50)
        self.verticalLayout_24.setSpacing(30)
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.horizontalLayout_32 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_32.setObjectName("horizontalLayout_32")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_17 = QtWidgets.QLabel(self.photo_dis_gbox)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("border:none;\n"
"font: 12pt \"黑体\";")
        self.label_17.setObjectName("label_17")
        self.verticalLayout_6.addWidget(self.label_17)
        self.dis_ratio_cbox = QtWidgets.QComboBox(self.photo_dis_gbox)
        self.dis_ratio_cbox.setMinimumSize(QtCore.QSize(80, 0))
        self.dis_ratio_cbox.setMaximumSize(QtCore.QSize(80, 16777215))
        self.dis_ratio_cbox.setStyleSheet("QComboBox {\n"
"    border: 1px solid #bebebe;\n"
"    padding: 1px 18px 1px 3px;\n"
"    font: normal normal 13px \"Microsoft YaHei\";\n"
"    color: #555555;\n"
"    background: transparent;\n"
"    border-radius:10px;\n"
"}\n"
" \n"
" \n"
"QComboBox:editable{\n"
"    background: transparent;\n"
"}\n"
" \n"
"QComboBox:!on{\n"
"}\n"
" \n"
"QComboBox:on{ /* the popup opens */\n"
"    color: #555555;\n"
"    border-color: #327cc0;\n"
"    background: transparent;\n"
"}\n"
" \n"
"QComboBox QAbstractItemView {\n"
"    outline: 0; \n"
"    border: 1px solid #327cc0;\n"
"    background-color: #F1F3F3;\n"
"    font: normal normal 14px \"Microsoft YaHei\";\n"
"}\n"
" \n"
"QComboBox QAbstractItemView::item {\n"
"    height: 15px;\n"
"    color: #555555;\n"
"    background-color: transparent;\n"
"}\n"
" \n"
"QComboBox QAbstractItemView::item:hover {\n"
"    color: #FFFFFF;\n"
"    background-color: #327cc0;\n"
"}\n"
" \n"
"QComboBox QAbstractItemView::item:selected {\n"
"    color: #FFFFFF;\n"
"    background-color: #327cc0;\n"
"}\n"
" \n"
"QComboBox QAbstractScrollArea QScrollBar:vertical {\n"
"    background-color: #d0d2d4;\n"
"}\n"
" \n"
"QComboBox QAbstractScrollArea QScrollBar::handle:vertical {\n"
"    background: rgb(160,160,160);\n"
"}\n"
" \n"
"QComboBox QAbstractScrollArea QScrollBar::handle:vertical:hover {\n"
"    background: rgb(90, 91, 93);\n"
"}")
        self.dis_ratio_cbox.setObjectName("dis_ratio_cbox")
        self.dis_ratio_cbox.addItem("")
        self.dis_ratio_cbox.addItem("")
        self.verticalLayout_6.addWidget(self.dis_ratio_cbox)
        self.horizontalLayout_32.addLayout(self.verticalLayout_6)
        self.label_36 = QtWidgets.QLabel(self.photo_dis_gbox)
        self.label_36.setText("")
        self.label_36.setObjectName("label_36")
        self.horizontalLayout_32.addWidget(self.label_36)
        self.horizontalLayout_32.setStretch(1, 1)
        self.verticalLayout_24.addLayout(self.horizontalLayout_32)
        self.verticalLayout_18 = QtWidgets.QVBoxLayout()
        self.verticalLayout_18.setSpacing(10)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.label_12 = QtWidgets.QLabel(self.photo_dis_gbox)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("border:none;\n"
"font: 12pt \"黑体\";")
        self.label_12.setObjectName("label_12")
        self.verticalLayout_18.addWidget(self.label_12)
        self.horizontalLayout_33 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_33.setObjectName("horizontalLayout_33")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(20, -1, -1, -1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_13 = QtWidgets.QLabel(self.photo_dis_gbox)
        self.label_13.setStyleSheet("border:none;\n"
"font: 10pt \"黑体\";")
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_12.addWidget(self.label_13)
        self.test_size_cbox = QtWidgets.QComboBox(self.photo_dis_gbox)
        self.test_size_cbox.setMinimumSize(QtCore.QSize(150, 0))
        self.test_size_cbox.setMaximumSize(QtCore.QSize(150, 16777215))
        self.test_size_cbox.setStyleSheet("QComboBox {\n"
"    border: 1px solid #bebebe;\n"
"    padding: 1px 18px 1px 3px;\n"
"    font: normal normal 13px \"Microsoft YaHei\";\n"
"    color: #555555;\n"
"    background: transparent;\n"
"    border-radius:10px;\n"
"}\n"
" \n"
" \n"
"QComboBox:editable{\n"
"    background: transparent;\n"
"}\n"
" \n"
"QComboBox:!on{\n"
"}\n"
" \n"
"QComboBox:on{ /* the popup opens */\n"
"    color: #555555;\n"
"    border-color: #327cc0;\n"
"    background: transparent;\n"
"}\n"
" \n"
"QComboBox QAbstractItemView {\n"
"    outline: 0; \n"
"    border: 1px solid #327cc0;\n"
"    background-color: #F1F3F3;\n"
"    font: normal normal 14px \"Microsoft YaHei\";\n"
"}\n"
" \n"
"QComboBox QAbstractItemView::item {\n"
"    height: 15px;\n"
"    color: #555555;\n"
"    background-color: transparent;\n"
"}\n"
" \n"
"QComboBox QAbstractItemView::item:hover {\n"
"    color: #FFFFFF;\n"
"    background-color: #327cc0;\n"
"}\n"
" \n"
"QComboBox QAbstractItemView::item:selected {\n"
"    color: #FFFFFF;\n"
"    background-color: #327cc0;\n"
"}\n"
" \n"
"QComboBox QAbstractScrollArea QScrollBar:vertical {\n"
"    background-color: #d0d2d4;\n"
"}\n"
" \n"
"QComboBox QAbstractScrollArea QScrollBar::handle:vertical {\n"
"    background: rgb(160,160,160);\n"
"}\n"
" \n"
"QComboBox QAbstractScrollArea QScrollBar::handle:vertical:hover {\n"
"    background: rgb(90, 91, 93);\n"
"}")
        self.test_size_cbox.setObjectName("test_size_cbox")
        self.horizontalLayout_12.addWidget(self.test_size_cbox)
        self.pushButton_9 = QtWidgets.QPushButton(self.photo_dis_gbox)
        self.pushButton_9.setMinimumSize(QtCore.QSize(60, 30))
        self.pushButton_9.setMaximumSize(QtCore.QSize(60, 30))
        self.pushButton_9.setStyleSheet("QPushButton:hover {\n"
"    background-color: rgb(58, 189, 236);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    \n"
"    background-color: rgb(27, 87, 126);\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(28, 120, 167);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 10pt \"黑体\";\n"
"    border-radius: 12px;\n"
"    border: 10px;\n"
"}")
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_12.addWidget(self.pushButton_9)
        self.verticalLayout_4.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_14 = QtWidgets.QLabel(self.photo_dis_gbox)
        self.label_14.setStyleSheet("border:none;\n"
"font: 10pt \"黑体\";")
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_13.addWidget(self.label_14)
        self.gt_size_cbox = QtWidgets.QComboBox(self.photo_dis_gbox)
        self.gt_size_cbox.setMinimumSize(QtCore.QSize(150, 0))
        self.gt_size_cbox.setMaximumSize(QtCore.QSize(150, 16777215))
        self.gt_size_cbox.setStyleSheet("QComboBox {\n"
"    border: 1px solid #bebebe;\n"
"    padding: 1px 18px 1px 3px;\n"
"    font: normal normal 13px \"Microsoft YaHei\";\n"
"    color: #555555;\n"
"    background: transparent;\n"
"    border-radius:10px;\n"
"}\n"
" \n"
" \n"
"QComboBox:editable{\n"
"    background: transparent;\n"
"}\n"
" \n"
"QComboBox:!on{\n"
"}\n"
" \n"
"QComboBox:on{ /* the popup opens */\n"
"    color: #555555;\n"
"    border-color: #327cc0;\n"
"    background: transparent;\n"
"}\n"
" \n"
"QComboBox QAbstractItemView {\n"
"    outline: 0; \n"
"    border: 1px solid #327cc0;\n"
"    background-color: #F1F3F3;\n"
"    font: normal normal 14px \"Microsoft YaHei\";\n"
"}\n"
" \n"
"QComboBox QAbstractItemView::item {\n"
"    height: 15px;\n"
"    color: #555555;\n"
"    background-color: transparent;\n"
"}\n"
" \n"
"QComboBox QAbstractItemView::item:hover {\n"
"    color: #FFFFFF;\n"
"    background-color: #327cc0;\n"
"}\n"
" \n"
"QComboBox QAbstractItemView::item:selected {\n"
"    color: #FFFFFF;\n"
"    background-color: #327cc0;\n"
"}\n"
" \n"
"QComboBox QAbstractScrollArea QScrollBar:vertical {\n"
"    background-color: #d0d2d4;\n"
"}\n"
" \n"
"QComboBox QAbstractScrollArea QScrollBar::handle:vertical {\n"
"    background: rgb(160,160,160);\n"
"}\n"
" \n"
"QComboBox QAbstractScrollArea QScrollBar::handle:vertical:hover {\n"
"    background: rgb(90, 91, 93);\n"
"}")
        self.gt_size_cbox.setObjectName("gt_size_cbox")
        self.horizontalLayout_13.addWidget(self.gt_size_cbox)
        self.pushButton_10 = QtWidgets.QPushButton(self.photo_dis_gbox)
        self.pushButton_10.setEnabled(False)
        self.pushButton_10.setMinimumSize(QtCore.QSize(60, 30))
        self.pushButton_10.setMaximumSize(QtCore.QSize(60, 30))
        self.pushButton_10.setStyleSheet("background-color: rgb(250,250,250);\n"
"border:none;")
        self.pushButton_10.setText("")
        self.pushButton_10.setObjectName("pushButton_10")
        self.horizontalLayout_13.addWidget(self.pushButton_10)
        self.verticalLayout_4.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_33.addLayout(self.verticalLayout_4)
        self.label_37 = QtWidgets.QLabel(self.photo_dis_gbox)
        self.label_37.setText("")
        self.label_37.setObjectName("label_37")
        self.horizontalLayout_33.addWidget(self.label_37)
        self.horizontalLayout_33.setStretch(1, 1)
        self.verticalLayout_18.addLayout(self.horizontalLayout_33)
        self.verticalLayout_24.addLayout(self.verticalLayout_18)
        self.verticalLayout_22 = QtWidgets.QVBoxLayout()
        self.verticalLayout_22.setSpacing(10)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.label_15 = QtWidgets.QLabel(self.photo_dis_gbox)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("border:none;\n"
"font: 12pt \"黑体\";")
        self.label_15.setObjectName("label_15")
        self.verticalLayout_22.addWidget(self.label_15)
        self.horizontalLayout_34 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_34.setContentsMargins(20, -1, -1, -1)
        self.horizontalLayout_34.setObjectName("horizontalLayout_34")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_16 = QtWidgets.QLabel(self.photo_dis_gbox)
        self.label_16.setMinimumSize(QtCore.QSize(0, 30))
        self.label_16.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_16.setStyleSheet("border:none;\n"
"font: 10pt \"黑体\";")
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_14.addWidget(self.label_16)
        self.inter_cbox = QtWidgets.QComboBox(self.photo_dis_gbox)
        self.inter_cbox.setMinimumSize(QtCore.QSize(180, 0))
        self.inter_cbox.setMaximumSize(QtCore.QSize(180, 16777215))
        self.inter_cbox.setStyleSheet("QComboBox {\n"
"    border: 1px solid #bebebe;\n"
"    padding: 1px 18px 1px 3px;\n"
"    font: normal normal 13px \"Microsoft YaHei\";\n"
"    color: #555555;\n"
"    background: transparent;\n"
"    border-radius:10px;\n"
"}\n"
" \n"
" \n"
"QComboBox:editable{\n"
"    background: transparent;\n"
"}\n"
" \n"
"QComboBox:!on{\n"
"}\n"
" \n"
"QComboBox:on{ /* the popup opens */\n"
"    color: #555555;\n"
"    border-color: #327cc0;\n"
"    background: transparent;\n"
"}\n"
" \n"
"QComboBox QAbstractItemView {\n"
"    outline: 0; \n"
"    border: 1px solid #327cc0;\n"
"    background-color: #F1F3F3;\n"
"    font: normal normal 14px \"Microsoft YaHei\";\n"
"}\n"
" \n"
"QComboBox QAbstractItemView::item {\n"
"    height: 15px;\n"
"    color: #555555;\n"
"    background-color: transparent;\n"
"}\n"
" \n"
"QComboBox QAbstractItemView::item:hover {\n"
"    color: #FFFFFF;\n"
"    background-color: #327cc0;\n"
"}\n"
" \n"
"QComboBox QAbstractItemView::item:selected {\n"
"    color: #FFFFFF;\n"
"    background-color: #327cc0;\n"
"}\n"
" \n"
"QComboBox QAbstractScrollArea QScrollBar:vertical {\n"
"    background-color: #d0d2d4;\n"
"}\n"
" \n"
"QComboBox QAbstractScrollArea QScrollBar::handle:vertical {\n"
"    background: rgb(160,160,160);\n"
"}\n"
" \n"
"QComboBox QAbstractScrollArea QScrollBar::handle:vertical:hover {\n"
"    background: rgb(90, 91, 93);\n"
"}")
        self.inter_cbox.setObjectName("inter_cbox")
        self.inter_cbox.addItem("")
        self.inter_cbox.addItem("")
        self.horizontalLayout_14.addWidget(self.inter_cbox)
        self.horizontalLayout_34.addLayout(self.horizontalLayout_14)
        self.label_38 = QtWidgets.QLabel(self.photo_dis_gbox)
        self.label_38.setText("")
        self.label_38.setObjectName("label_38")
        self.horizontalLayout_34.addWidget(self.label_38)
        self.horizontalLayout_34.setStretch(1, 1)
        self.verticalLayout_22.addLayout(self.horizontalLayout_34)
        self.verticalLayout_24.addLayout(self.verticalLayout_22)
        self.verticalLayout_23 = QtWidgets.QVBoxLayout()
        self.verticalLayout_23.setSpacing(15)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_18 = QtWidgets.QLabel(self.photo_dis_gbox)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("border:none;\n"
"font: 12pt \"黑体\";")
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_15.addWidget(self.label_18)
        self.label_19 = QtWidgets.QLabel(self.photo_dis_gbox)
        self.label_19.setStyleSheet("color: rgb(135, 135, 135);\n"
"font: 10pt \"黑体\";")
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_15.addWidget(self.label_19)
        self.horizontalLayout_15.setStretch(1, 1)
        self.verticalLayout_23.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_25.setContentsMargins(-1, -1, -1, 6)
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(20, -1, -1, -1)
        self.verticalLayout_5.setSpacing(12)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.radioButton = QtWidgets.QRadioButton(self.photo_dis_gbox)
        self.radioButton.setStyleSheet("\n"
"font:10pt \"黑体\";")
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout_5.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.photo_dis_gbox)
        self.radioButton_2.setStyleSheet("font:10pt \"黑体\";")
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout_5.addWidget(self.radioButton_2)
        self.radioButton_3 = QtWidgets.QRadioButton(self.photo_dis_gbox)
        self.radioButton_3.setStyleSheet("font:10pt \"黑体\";")
        self.radioButton_3.setObjectName("radioButton_3")
        self.verticalLayout_5.addWidget(self.radioButton_3)
        self.radioButton_4 = QtWidgets.QRadioButton(self.photo_dis_gbox)
        self.radioButton_4.setStyleSheet("font:10pt \"黑体\";")
        self.radioButton_4.setObjectName("radioButton_4")
        self.verticalLayout_5.addWidget(self.radioButton_4)
        self.radioButton_5 = QtWidgets.QRadioButton(self.photo_dis_gbox)
        self.radioButton_5.setStyleSheet("font:10pt \"黑体\";")
        self.radioButton_5.setObjectName("radioButton_5")
        self.verticalLayout_5.addWidget(self.radioButton_5)
        self.horizontalLayout_25.addLayout(self.verticalLayout_5)
        self.label_39 = QtWidgets.QLabel(self.photo_dis_gbox)
        self.label_39.setText("")
        self.label_39.setObjectName("label_39")
        self.horizontalLayout_25.addWidget(self.label_39)
        self.verticalLayout_23.addLayout(self.horizontalLayout_25)
        self.verticalLayout_24.addLayout(self.verticalLayout_23)
        self.verticalLayout_35.addWidget(self.photo_dis_gbox)
        self.label_49 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_49.setMinimumSize(QtCore.QSize(0, 50))
        self.label_49.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_49.setStyleSheet("color: rgb(173, 173, 173);")
        self.label_49.setObjectName("label_49")
        self.verticalLayout_35.addWidget(self.label_49)
        self.tester_gbox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.tester_gbox.setStyleSheet("QGroupBox {\n"
"    font: 25px \"黑体\";\n"
"    border: none;\n"
"    background-color: rgb(250, 250, 250);\n"
"    border-radius:6px;\n"
"    margin-top:12px;\n"
"}\n"
"QGroupBox:title {\n"
"    color:rgb(28, 120, 167);\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"}")
        self.tester_gbox.setObjectName("tester_gbox")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.tester_gbox)
        self.verticalLayout_9.setContentsMargins(-1, 50, -1, 50)
        self.verticalLayout_9.setSpacing(10)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_20 = QtWidgets.QLabel(self.tester_gbox)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("border:none;\n"
"font: 12pt \"黑体\";")
        self.label_20.setObjectName("label_20")
        self.verticalLayout_9.addWidget(self.label_20)
        self.horizontalLayout_36 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_36.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_36.setObjectName("horizontalLayout_36")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.tester_gbox)
        self.lineEdit_9.setMinimumSize(QtCore.QSize(150, 22))
        self.lineEdit_9.setMaximumSize(QtCore.QSize(150, 22))
        self.lineEdit_9.setStyleSheet("border:none;\n"
"font: 10pt \"Microsoft YaHei UI\";\n"
"background-color: rgb(240, 240, 240);\n"
"border-radius:10px;")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.horizontalLayout_16.addWidget(self.lineEdit_9)
        self.pushButton_11 = QtWidgets.QPushButton(self.tester_gbox)
        self.pushButton_11.setMinimumSize(QtCore.QSize(70, 30))
        self.pushButton_11.setMaximumSize(QtCore.QSize(70, 30))
        self.pushButton_11.setStyleSheet("QPushButton:hover {\n"
"    background-color: rgb(58, 189, 236);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    \n"
"    background-color: rgb(27, 87, 126);\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(28, 120, 167);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 10pt \"黑体\";\n"
"    border-radius: 12px;\n"
"    border: 10px;\n"
"}")
        self.pushButton_11.setObjectName("pushButton_11")
        self.horizontalLayout_16.addWidget(self.pushButton_11)
        self.horizontalLayout_36.addLayout(self.horizontalLayout_16)
        self.label_40 = QtWidgets.QLabel(self.tester_gbox)
        self.label_40.setText("")
        self.label_40.setObjectName("label_40")
        self.horizontalLayout_36.addWidget(self.label_40)
        self.horizontalLayout_36.setStretch(1, 1)
        self.verticalLayout_9.addLayout(self.horizontalLayout_36)
        self.verticalLayout_35.addWidget(self.tester_gbox)
        self.label_50 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_50.setMinimumSize(QtCore.QSize(0, 50))
        self.label_50.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_50.setStyleSheet("color: rgb(173, 173, 173);")
        self.label_50.setObjectName("label_50")
        self.verticalLayout_35.addWidget(self.label_50)
        self.others_gbox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.others_gbox.setStyleSheet("QGroupBox {\n"
"    font: 25px \"黑体\";\n"
"    border: none;\n"
"    background-color: rgb(250, 250, 250);\n"
"    border-radius:6px;\n"
"    margin-top:12px;\n"
"}\n"
"QGroupBox:title {\n"
"    color:rgb(28, 120, 167);\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"}")
        self.others_gbox.setObjectName("others_gbox")
        self.verticalLayout_27 = QtWidgets.QVBoxLayout(self.others_gbox)
        self.verticalLayout_27.setContentsMargins(-1, 50, -1, 50)
        self.verticalLayout_27.setSpacing(25)
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout()
        self.verticalLayout_19.setSpacing(10)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.label_21 = QtWidgets.QLabel(self.others_gbox)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("border:none;\n"
"font: 12pt \"黑体\";")
        self.label_21.setObjectName("label_21")
        self.verticalLayout_19.addWidget(self.label_21)
        self.horizontalLayout_37 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_37.setObjectName("horizontalLayout_37")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.others_gbox)
        self.lineEdit_10.setMinimumSize(QtCore.QSize(0, 22))
        self.lineEdit_10.setMaximumSize(QtCore.QSize(16777215, 22))
        self.lineEdit_10.setStyleSheet("border:none;\n"
"font: 10pt \"Microsoft YaHei UI\";\n"
"background-color: rgb(240, 240, 240);\n"
"border-radius:10px;")
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.horizontalLayout_17.addWidget(self.lineEdit_10)
        self.pushButton_12 = QtWidgets.QPushButton(self.others_gbox)
        self.pushButton_12.setMinimumSize(QtCore.QSize(110, 30))
        self.pushButton_12.setMaximumSize(QtCore.QSize(110, 30))
        self.pushButton_12.setStyleSheet("QPushButton:hover {\n"
"    background-color: rgb(58, 189, 236);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    \n"
"    background-color: rgb(27, 87, 126);\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(28, 120, 167);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 10pt \"黑体\";\n"
"    border-radius: 12px;\n"
"    border: 10px;\n"
"}")
        self.pushButton_12.setObjectName("pushButton_12")
        self.horizontalLayout_17.addWidget(self.pushButton_12)
        self.horizontalLayout_37.addLayout(self.horizontalLayout_17)
        self.label_41 = QtWidgets.QLabel(self.others_gbox)
        self.label_41.setText("")
        self.label_41.setObjectName("label_41")
        self.horizontalLayout_37.addWidget(self.label_41)
        self.horizontalLayout_37.setStretch(1, 1)
        self.verticalLayout_19.addLayout(self.horizontalLayout_37)
        self.verticalLayout_27.addLayout(self.verticalLayout_19)
        self.verticalLayout_25 = QtWidgets.QVBoxLayout()
        self.verticalLayout_25.setSpacing(10)
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.horizontalLayout_38 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_38.setObjectName("horizontalLayout_38")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label_22 = QtWidgets.QLabel(self.others_gbox)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("border:none;\n"
"font: 12pt \"黑体\";")
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_19.addWidget(self.label_22)
        self.checkBox = QtWidgets.QCheckBox(self.others_gbox)
        self.checkBox.setStyleSheet("border:none;\n"
"font: 10pt \"黑体\";")
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_19.addWidget(self.checkBox)
        self.horizontalLayout_38.addLayout(self.horizontalLayout_19)
        self.label_42 = QtWidgets.QLabel(self.others_gbox)
        self.label_42.setText("")
        self.label_42.setObjectName("label_42")
        self.horizontalLayout_38.addWidget(self.label_42)
        self.horizontalLayout_38.setStretch(1, 1)
        self.verticalLayout_25.addLayout(self.horizontalLayout_38)
        self.horizontalLayout_39 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_39.setContentsMargins(20, -1, -1, -1)
        self.horizontalLayout_39.setObjectName("horizontalLayout_39")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_18.setSpacing(40)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_23 = QtWidgets.QLabel(self.others_gbox)
        self.label_23.setMinimumSize(QtCore.QSize(200, 0))
        self.label_23.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("color: rgb(135, 135, 135);\n"
"font:10pt \"黑体\";")
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName("label_23")
        self.horizontalLayout_18.addWidget(self.label_23)
        self.label_27 = QtWidgets.QLabel(self.others_gbox)
        self.label_27.setMinimumSize(QtCore.QSize(200, 0))
        self.label_27.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_27.setFont(font)
        self.label_27.setStyleSheet("color: rgb(135, 135, 135);\n"
"font:10pt \"黑体\";")
        self.label_27.setAlignment(QtCore.Qt.AlignCenter)
        self.label_27.setObjectName("label_27")
        self.horizontalLayout_18.addWidget(self.label_27)
        self.label_52 = QtWidgets.QLabel(self.others_gbox)
        self.label_52.setMinimumSize(QtCore.QSize(200, 0))
        self.label_52.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_52.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_52.setStyleSheet("color: rgb(135, 135, 135);\n"
"font:10pt \"黑体\";")
        self.label_52.setAlignment(QtCore.Qt.AlignCenter)
        self.label_52.setObjectName("label_52")
        self.horizontalLayout_18.addWidget(self.label_52)
        self.horizontalLayout_18.setStretch(0, 1)
        self.horizontalLayout_18.setStretch(1, 1)
        self.verticalLayout_7.addLayout(self.horizontalLayout_18)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setSpacing(40)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.label_24 = QtWidgets.QLabel(self.others_gbox)
        self.label_24.setMinimumSize(QtCore.QSize(200, 0))
        self.label_24.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_24.setStyleSheet("font:10pt \"黑体\";")
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.horizontalLayout_20.addWidget(self.label_24, 0, QtCore.Qt.AlignHCenter)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.others_gbox)
        self.lineEdit_11.setMinimumSize(QtCore.QSize(200, 22))
        self.lineEdit_11.setMaximumSize(QtCore.QSize(200, 22))
        self.lineEdit_11.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_11.setStyleSheet("border:none;\n"
"font: 10pt \"Microsoft YaHei UI\";")
        self.lineEdit_11.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.horizontalLayout_20.addWidget(self.lineEdit_11)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.others_gbox)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(200, 0))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.lineEdit_2.setStyleSheet("border:none;\n"
"font: 10pt \"Microsoft YaHei UI\";")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_20.addWidget(self.lineEdit_2)
        self.horizontalLayout_20.setStretch(0, 1)
        self.horizontalLayout_20.setStretch(1, 1)
        self.horizontalLayout_20.setStretch(2, 1)
        self.verticalLayout_7.addLayout(self.horizontalLayout_20)
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setSpacing(40)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.label_25 = QtWidgets.QLabel(self.others_gbox)
        self.label_25.setMinimumSize(QtCore.QSize(200, 0))
        self.label_25.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_25.setStyleSheet("font:10pt \"黑体\";")
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName("label_25")
        self.horizontalLayout_21.addWidget(self.label_25, 0, QtCore.Qt.AlignHCenter)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.others_gbox)
        self.lineEdit_12.setMinimumSize(QtCore.QSize(200, 22))
        self.lineEdit_12.setMaximumSize(QtCore.QSize(200, 22))
        self.lineEdit_12.setStyleSheet("border:none;\n"
"font: 10pt \"Microsoft YaHei UI\";")
        self.lineEdit_12.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.horizontalLayout_21.addWidget(self.lineEdit_12)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.others_gbox)
        self.lineEdit_6.setMinimumSize(QtCore.QSize(200, 0))
        self.lineEdit_6.setMaximumSize(QtCore.QSize(200, 16777215))
        self.lineEdit_6.setStyleSheet("border:none;\n"
"font: 10pt \"Microsoft YaHei UI\";")
        self.lineEdit_6.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.horizontalLayout_21.addWidget(self.lineEdit_6)
        self.horizontalLayout_21.setStretch(0, 1)
        self.horizontalLayout_21.setStretch(1, 1)
        self.horizontalLayout_21.setStretch(2, 1)
        self.verticalLayout_7.addLayout(self.horizontalLayout_21)
        self.horizontalLayout_31 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_31.setSpacing(40)
        self.horizontalLayout_31.setObjectName("horizontalLayout_31")
        self.label_63 = QtWidgets.QLabel(self.others_gbox)
        self.label_63.setMinimumSize(QtCore.QSize(200, 0))
        self.label_63.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_63.setStyleSheet("font:10pt \"黑体\";")
        self.label_63.setAlignment(QtCore.Qt.AlignCenter)
        self.label_63.setObjectName("label_63")
        self.horizontalLayout_31.addWidget(self.label_63, 0, QtCore.Qt.AlignHCenter)
        self.lineEdit_18 = QtWidgets.QLineEdit(self.others_gbox)
        self.lineEdit_18.setMinimumSize(QtCore.QSize(200, 22))
        self.lineEdit_18.setMaximumSize(QtCore.QSize(200, 22))
        self.lineEdit_18.setStyleSheet("border:none;\n"
"font: 10pt \"Microsoft YaHei UI\";")
        self.lineEdit_18.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.horizontalLayout_31.addWidget(self.lineEdit_18)
        self.lineEdit_19 = QtWidgets.QLineEdit(self.others_gbox)
        self.lineEdit_19.setMinimumSize(QtCore.QSize(200, 0))
        self.lineEdit_19.setMaximumSize(QtCore.QSize(200, 16777215))
        self.lineEdit_19.setStyleSheet("border:none;\n"
"font: 10pt \"Microsoft YaHei UI\";")
        self.lineEdit_19.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.horizontalLayout_31.addWidget(self.lineEdit_19)
        self.horizontalLayout_31.setStretch(0, 1)
        self.horizontalLayout_31.setStretch(1, 1)
        self.horizontalLayout_31.setStretch(2, 1)
        self.verticalLayout_7.addLayout(self.horizontalLayout_31)
        self.horizontalLayout_35 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_35.setSpacing(40)
        self.horizontalLayout_35.setObjectName("horizontalLayout_35")
        self.label_64 = QtWidgets.QLabel(self.others_gbox)
        self.label_64.setMinimumSize(QtCore.QSize(200, 0))
        self.label_64.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_64.setStyleSheet("font:10pt \"黑体\";")
        self.label_64.setAlignment(QtCore.Qt.AlignCenter)
        self.label_64.setObjectName("label_64")
        self.horizontalLayout_35.addWidget(self.label_64, 0, QtCore.Qt.AlignHCenter)
        self.lineEdit_20 = QtWidgets.QLineEdit(self.others_gbox)
        self.lineEdit_20.setMinimumSize(QtCore.QSize(200, 22))
        self.lineEdit_20.setMaximumSize(QtCore.QSize(200, 22))
        self.lineEdit_20.setStyleSheet("border:none;\n"
"font: 10pt \"Microsoft YaHei UI\";")
        self.lineEdit_20.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.horizontalLayout_35.addWidget(self.lineEdit_20)
        self.lineEdit_21 = QtWidgets.QLineEdit(self.others_gbox)
        self.lineEdit_21.setMinimumSize(QtCore.QSize(200, 0))
        self.lineEdit_21.setMaximumSize(QtCore.QSize(200, 16777215))
        self.lineEdit_21.setStyleSheet("border:none;\n"
"font: 10pt \"Microsoft YaHei UI\";")
        self.lineEdit_21.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.horizontalLayout_35.addWidget(self.lineEdit_21)
        self.horizontalLayout_35.setStretch(0, 1)
        self.horizontalLayout_35.setStretch(1, 1)
        self.horizontalLayout_35.setStretch(2, 1)
        self.verticalLayout_7.addLayout(self.horizontalLayout_35)
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setSpacing(40)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.label_26 = QtWidgets.QLabel(self.others_gbox)
        self.label_26.setMinimumSize(QtCore.QSize(200, 0))
        self.label_26.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_26.setStyleSheet("font:10pt \"黑体\";")
        self.label_26.setAlignment(QtCore.Qt.AlignCenter)
        self.label_26.setObjectName("label_26")
        self.horizontalLayout_22.addWidget(self.label_26, 0, QtCore.Qt.AlignHCenter)
        self.lineEdit_13 = QtWidgets.QLineEdit(self.others_gbox)
        self.lineEdit_13.setMinimumSize(QtCore.QSize(200, 22))
        self.lineEdit_13.setMaximumSize(QtCore.QSize(200, 22))
        self.lineEdit_13.setStyleSheet("border:none;\n"
"font: 10pt \"Microsoft YaHei UI\";")
        self.lineEdit_13.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.horizontalLayout_22.addWidget(self.lineEdit_13)
        self.lineEdit_17 = QtWidgets.QLineEdit(self.others_gbox)
        self.lineEdit_17.setMinimumSize(QtCore.QSize(200, 0))
        self.lineEdit_17.setMaximumSize(QtCore.QSize(200, 16777215))
        self.lineEdit_17.setStyleSheet("border:none;\n"
"font: 10pt \"Microsoft YaHei UI\";")
        self.lineEdit_17.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.horizontalLayout_22.addWidget(self.lineEdit_17)
        self.horizontalLayout_22.setStretch(0, 1)
        self.horizontalLayout_22.setStretch(1, 1)
        self.horizontalLayout_22.setStretch(2, 1)
        self.verticalLayout_7.addLayout(self.horizontalLayout_22)
        self.horizontalLayout_39.addLayout(self.verticalLayout_7)
        self.label_43 = QtWidgets.QLabel(self.others_gbox)
        self.label_43.setText("")
        self.label_43.setObjectName("label_43")
        self.horizontalLayout_39.addWidget(self.label_43)
        self.horizontalLayout_39.setStretch(0, 2)
        self.horizontalLayout_39.setStretch(1, 1)
        self.verticalLayout_25.addLayout(self.horizontalLayout_39)
        self.verticalLayout_27.addLayout(self.verticalLayout_25)
        self.verticalLayout_26 = QtWidgets.QVBoxLayout()
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.label_45 = QtWidgets.QLabel(self.others_gbox)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_45.setFont(font)
        self.label_45.setStyleSheet("border:none;\n"
"font: 12pt \"黑体\";")
        self.label_45.setObjectName("label_45")
        self.verticalLayout_26.addWidget(self.label_45)
        self.horizontalLayout_40 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_40.setSpacing(10)
        self.horizontalLayout_40.setObjectName("horizontalLayout_40")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setContentsMargins(20, -1, -1, -1)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.pushButton_14 = QtWidgets.QPushButton(self.others_gbox)
        self.pushButton_14.setMinimumSize(QtCore.QSize(70, 30))
        self.pushButton_14.setMaximumSize(QtCore.QSize(70, 30))
        self.pushButton_14.setStyleSheet("QPushButton:hover {\n"
"    background-color: rgb(58, 189, 236);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    \n"
"    background-color: rgb(27, 87, 126);\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(28, 120, 167);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 10pt \"黑体\";\n"
"    border-radius: 12px;\n"
"    border: 10px;\n"
"}")
        self.pushButton_14.setObjectName("pushButton_14")
        self.verticalLayout_8.addWidget(self.pushButton_14)
        self.pushButton_13 = QtWidgets.QPushButton(self.others_gbox)
        self.pushButton_13.setMinimumSize(QtCore.QSize(70, 30))
        self.pushButton_13.setMaximumSize(QtCore.QSize(70, 30))
        self.pushButton_13.setStyleSheet("QPushButton:hover {\n"
"    background-color: rgb(58, 189, 236);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    \n"
"    background-color: rgb(27, 87, 126);\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(28, 120, 167);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 10pt \"黑体\";\n"
"    border-radius: 12px;\n"
"    border: 10px;\n"
"}")
        self.pushButton_13.setObjectName("pushButton_13")
        self.verticalLayout_8.addWidget(self.pushButton_13)
        self.horizontalLayout_40.addLayout(self.verticalLayout_8)
        self.label_44 = QtWidgets.QLabel(self.others_gbox)
        self.label_44.setText("")
        self.label_44.setObjectName("label_44")
        self.horizontalLayout_40.addWidget(self.label_44)
        self.horizontalLayout_40.setStretch(1, 1)
        self.verticalLayout_26.addLayout(self.horizontalLayout_40)
        self.verticalLayout_27.addLayout(self.verticalLayout_26)
        self.verticalLayout_35.addWidget(self.others_gbox)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.scrollArea)
        self.horizontalLayout.setStretch(1, 1)

        self.retranslateUi(Form)
        self.setting_listWidget.setCurrentRow(-1)
        self.pushButton.clicked.connect(Form.database_path)
        self.pushButton_3.clicked.connect(Form.mos_path)
        self.pushButton_11.clicked.connect(Form.testee_path)
        self.pushButton_14.clicked.connect(Form.learn_more)
        self.pushButton_13.clicked.connect(Form.feedback)
        self.horizontalSlider.valueChanged['int'].connect(Form.dsis_t1)
        self.horizontalSlider_2.valueChanged['int'].connect(Form.dsis_t2)
        self.horizontalSlider_3.valueChanged['int'].connect(Form.dsis_t3)
        self.horizontalSlider_4.valueChanged['int'].connect(Form.dsis_t4)
        self.horizontalSlider_5.valueChanged['int'].connect(Form.ss_t1)
        self.horizontalSlider_6.valueChanged['int'].connect(Form.ss_t2)
        self.horizontalSlider_7.valueChanged['int'].connect(Form.ss_t3)
        self.pushButton_4.clicked.connect(Form.dsis_t1_ensure)
        self.pushButton_5.clicked.connect(Form.dsis_t2_ensure)
        self.pushButton_7.clicked.connect(Form.dsis_t3_ensure)
        self.pushButton_8.clicked.connect(Form.dsis_t4_ensure)
        self.pushButton_15.clicked.connect(Form.ss_t1_ensure)
        self.pushButton_16.clicked.connect(Form.ss_t2_ensure)
        self.pushButton_17.clicked.connect(Form.ss_t3_ensure)
        self.comboBox.currentIndexChanged['int'].connect(Form.mos_content_conclude)
        self.comboBox_2.currentIndexChanged['int'].connect(Form.mark_style_change)
        self.dis_ratio_cbox.currentIndexChanged['int'].connect(Form.display_ratio)
        self.test_size_cbox.currentIndexChanged['int'].connect(Form.test_pic_size)
        self.gt_size_cbox.currentIndexChanged['int'].connect(Form.GT_pic_size)
        self.pushButton_9.clicked.connect(Form.diy_pho_size)
        self.inter_cbox.currentIndexChanged['int'].connect(Form.interp_style)
        self.radioButton.clicked.connect(Form.screen1_dis_style)
        self.radioButton_2.clicked.connect(Form.screenlr_dis_style)
        self.radioButton_3.clicked.connect(Form.screenud_dis_style)
        self.radioButton_4.clicked.connect(Form.screen2_dis_style)
        self.pushButton_9.clicked.connect(Form.goto_diy_pho_size)
        self.radioButton_5.clicked.connect(Form.screen_peid_style)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "设置面板"))
        __sortingEnabled = self.setting_listWidget.isSortingEnabled()
        self.setting_listWidget.setSortingEnabled(False)
        item = self.setting_listWidget.item(0)
        item.setText(_translate("Form", "数据库来源"))
        item = self.setting_listWidget.item(1)
        item.setText(_translate("Form", "MOS记录"))
        item = self.setting_listWidget.item(2)
        item.setText(_translate("Form", "实验参数"))
        item = self.setting_listWidget.item(3)
        item.setText(_translate("Form", "主显示"))
        item = self.setting_listWidget.item(4)
        item.setText(_translate("Form", "受试者信息"))
        item = self.setting_listWidget.item(5)
        item.setText(_translate("Form", "其他"))
        self.setting_listWidget.setSortingEnabled(__sortingEnabled)
        self.database_gbox.setTitle(_translate("Form", "数据库"))
        self.label.setText(_translate("Form", "数据库来源："))
        self.label_2.setText(_translate("Form", "一般为所有待测图片的上级目录，若图片已分组，则为分组目录上一级目录"))
        self.pushButton.setText(_translate("Form", "更改地址"))
        self.label_46.setText(_translate("Form", "--------------------------------------------------------------------------------------------------------------------------------"))
        self.mos_gbox.setTitle(_translate("Form", "MOS记录"))
        self.label_3.setText(_translate("Form", "记录格式："))
        self.label_5.setText(_translate("Form", "记录包含内容"))
        self.comboBox.setItemText(0, _translate("Form", "图片名和得分"))
        self.comboBox.setItemText(1, _translate("Form", "时间戳、图片名和得分"))
        self.label_4.setText(_translate("Form", "记录地址："))
        self.pushButton_3.setText(_translate("Form", "更改地址"))
        self.label_47.setText(_translate("Form", "--------------------------------------------------------------------------------------------------------------------------------"))
        self.exp_gbox.setTitle(_translate("Form", "实验参数"))
        self.label_6.setText(_translate("Form", "时间设置："))
        self.label_60.setText(_translate("Form", "双重刺激失真水平测试（DSIS）"))
        self.label_61.setText(_translate("Form", "单刺激失真水平测试（SS）"))
        self.label_7.setText(_translate("Form", "原始照片显示时间t1（秒）："))
        self.pushButton_4.setText(_translate("Form", "保存更改"))
        self.label_8.setText(_translate("Form", "原始与测试图片间隔时间t2（秒）："))
        self.pushButton_5.setText(_translate("Form", "保存更改"))
        self.label_10.setText(_translate("Form", "测试图片显示时间t3（秒）："))
        self.pushButton_7.setText(_translate("Form", "保存更改"))
        self.label_11.setText(_translate("Form", "测试图片显示结束后时间t4（秒）："))
        self.pushButton_8.setText(_translate("Form", "保存更改"))
        self.label_62.setText(_translate("Form", "|\n"
"|\n"
"|\n"
"|\n"
"|\n"
"|\n"
"|\n"
"|\n"
"|\n"
"|\n"
"|\n"
"|\n"
"|\n"
"|\n"
"|\n"
"|\n"
"|\n"
"|\n"
"|\n"
"|\n"
""))
        self.label_53.setText(_translate("Form", "第一段无显示时间t1（秒）："))
        self.pushButton_15.setText(_translate("Form", "保存更改"))
        self.label_55.setText(_translate("Form", "测试图片显示时间t2（秒）："))
        self.pushButton_16.setText(_translate("Form", "保存更改"))
        self.label_57.setText(_translate("Form", "第二段无显示时间t3（秒）："))
        self.pushButton_17.setText(_translate("Form", "保存更改"))
        self.label_9.setText(_translate("Form", "评分形式设置："))
        self.comboBox_2.setItemText(0, _translate("Form", "滑轮，仅数字，评分范围1-5"))
        self.comboBox_2.setItemText(1, _translate("Form", "滑轮，仅数字，评分范围0-100"))
        self.comboBox_2.setItemText(2, _translate("Form", "条状， 仅数字，评分范围1-5"))
        self.comboBox_2.setItemText(3, _translate("Form", "条状， 仅数字，评分范围0-100"))
        self.label_48.setText(_translate("Form", "--------------------------------------------------------------------------------------------------------------------------------"))
        self.photo_dis_gbox.setTitle(_translate("Form", "图片显示"))
        self.label_17.setText(_translate("Form", "显示比例："))
        self.dis_ratio_cbox.setItemText(0, _translate("Form", "4:3"))
        self.dis_ratio_cbox.setItemText(1, _translate("Form", "16:9"))
        self.label_12.setText(_translate("Form", "图片大小："))
        self.label_13.setText(_translate("Form", "测试图片："))
        self.pushButton_9.setText(_translate("Form", "自定义"))
        self.label_14.setText(_translate("Form", "参考图片（GT）："))
        self.label_15.setText(_translate("Form", "插值方式："))
        self.label_16.setText(_translate("Form", "选择显示图片的插值方式："))
        self.inter_cbox.setItemText(0, _translate("Form", "双线性插值（默认）"))
        self.inter_cbox.setItemText(1, _translate("Form", "线性插值"))
        self.label_18.setText(_translate("Form", "双刺激评分的屏幕与对应实验方法选择："))
        self.label_19.setText(_translate("Form", "选择上下和左右布局时可能会和之前设置的图片尺寸冲突，这种情况下将自适应调整"))
        self.radioButton.setText(_translate("Form", "方式1：仅显示一张图片（右上角显示缩略图）（动态参考）"))
        self.radioButton_2.setText(_translate("Form", "方式2：左右分布显示两张照片（DSIS）"))
        self.radioButton_3.setText(_translate("Form", "方式3：上下分布显示两张图片（DSIS）"))
        self.radioButton_4.setText(_translate("Form", "方式4：经典双屏显示(SS)"))
        self.radioButton_5.setText(_translate("Form", "方式5：PEID实验专用（动态参考+排序）"))
        self.label_49.setText(_translate("Form", "--------------------------------------------------------------------------------------------------------------------------------"))
        self.tester_gbox.setTitle(_translate("Form", "受试者信息"))
        self.label_20.setText(_translate("Form", "存储地址："))
        self.pushButton_11.setText(_translate("Form", "更改设置"))
        self.label_50.setText(_translate("Form", "--------------------------------------------------------------------------------------------------------------------------------"))
        self.others_gbox.setTitle(_translate("Form", "其他"))
        self.label_21.setText(_translate("Form", "皮肤设置："))
        self.pushButton_12.setText(_translate("Form", "待优化"))
        self.label_22.setText(_translate("Form", "快捷键："))
        self.checkBox.setText(_translate("Form", "启用全局快捷键"))
        self.label_23.setText(_translate("Form", "功能说明"))
        self.label_27.setText(_translate("Form", "快捷键"))
        self.label_52.setText(_translate("Form", "全局快捷键"))
        self.label_24.setText(_translate("Form", "开始测评"))
        self.lineEdit_11.setText(_translate("Form", "Alt+S"))
        self.lineEdit_2.setText(_translate("Form", "Ctrl+Shift+S"))
        self.label_25.setText(_translate("Form", "打开设置面板"))
        self.lineEdit_12.setText(_translate("Form", "Ctrl+Shift+D"))
        self.lineEdit_6.setText(_translate("Form", "Ctrl+Shift+D"))
        self.label_63.setText(_translate("Form", "确认评分"))
        self.lineEdit_18.setText(_translate("Form", "Alt+E"))
        self.lineEdit_19.setText(_translate("Form", "Ctrl+Shift+E"))
        self.label_64.setText(_translate("Form", "评分增加"))
        self.lineEdit_20.setText(_translate("Form", "Alt+Up"))
        self.lineEdit_21.setText(_translate("Form", "Ctrl+Shift+Up"))
        self.label_26.setText(_translate("Form", "评分减少"))
        self.lineEdit_13.setText(_translate("Form", "Alt+Down"))
        self.lineEdit_17.setText(_translate("Form", "Ctrl+Shift+Down"))
        self.label_45.setText(_translate("Form", "更多："))
        self.pushButton_14.setText(_translate("Form", "了解更多"))
        self.pushButton_13.setText(_translate("Form", "我要反馈"))
import images_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
