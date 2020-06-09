# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'help_and_tips.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_tips_Wizard(object):
    def setupUi(self, tips_Wizard):
        tips_Wizard.setObjectName("tips_Wizard")
        tips_Wizard.setWindowModality(QtCore.Qt.NonModal)
        tips_Wizard.resize(981, 606)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Main_Exp/images/app_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        tips_Wizard.setWindowIcon(icon)
        tips_Wizard.setStyleSheet("border-color: rgb(255, 255, 255);")
        tips_Wizard.setSizeGripEnabled(False)
        tips_Wizard.setWizardStyle(QtWidgets.QWizard.ClassicStyle)
        tips_Wizard.setOptions(QtWidgets.QWizard.HaveFinishButtonOnEarlyPages|QtWidgets.QWizard.HaveNextButtonOnLastPage)
        tips_Wizard.setTitleFormat(QtCore.Qt.AutoText)
        self.ss_data_style = QtWidgets.QWizardPage()
        self.ss_data_style.setStyleSheet("")
        self.ss_data_style.setObjectName("ss_data_style")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.ss_data_style)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.ss_data_style)
        self.scrollArea.setStyleSheet("QScrollArea{\n"
"    border: 0px solid;\n"
"    border-right-width: 1px;\n"
"    border-right-color: #dcdbdc;\n"
"    background-color: #f5f5f7;\n"
"}\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #f5f5f7;\n"
"    width: 10px;\n"
"    margin: 0px 0 0px 0;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background: Gainsboro;\n"
"    min-height: 20px;\n"
"    border-radius: 5px;\n"
"    border: none;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"    border: 0px solid grey;\n"
"    background: #32CC99;\n"
"    height: 0px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"    border: 0px solid grey;\n"
"    background: #32CC99;\n"
"    height: 0px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"    width: 0px;\n"
"    height: 0px;\n"
"}")
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 927, 852))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, -1)
        self.verticalLayout_9.setSpacing(10)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.textBrowser = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowser.setMinimumSize(QtCore.QSize(0, 80))
        self.textBrowser.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.textBrowser.setStyleSheet("border: none;\n"
"border-color: rgb(255, 255, 255);")
        self.textBrowser.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_9.addWidget(self.textBrowser)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(10, -1, -1, -1)
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/tips/images/tips_ss_1.png"))
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/tips/images/tips_ss_2.png"))
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_10 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap(":/tips/images/tips_ss_3.png"))
        self.label_10.setObjectName("label_10")
        self.verticalLayout_2.addWidget(self.label_10)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.label_11 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.horizontalLayout.addWidget(self.label_11)
        self.horizontalLayout.setStretch(1, 1)
        self.verticalLayout_9.addLayout(self.horizontalLayout)
        self.verticalLayout_9.setStretch(0, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        tips_Wizard.addPage(self.ss_data_style)
        self.dsis_data_style = QtWidgets.QWizardPage()
        self.dsis_data_style.setObjectName("dsis_data_style")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.dsis_data_style)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.dsis_data_style)
        self.scrollArea_2.setStyleSheet("QScrollArea{\n"
"    border: 0px solid;\n"
"    border-right-width: 1px;\n"
"    border-right-color: #dcdbdc;\n"
"    background-color: #f5f5f7;\n"
"}\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #f5f5f7;\n"
"    width: 10px;\n"
"    margin: 0px 0 0px 0;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background: Gainsboro;\n"
"    min-height: 20px;\n"
"    border-radius: 5px;\n"
"    border: none;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"    border: 0px solid grey;\n"
"    background: #32CC99;\n"
"    height: 0px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"    border: 0px solid grey;\n"
"    background: #32CC99;\n"
"    height: 0px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"    width: 0px;\n"
"    height: 0px;\n"
"}")
        self.scrollArea_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 946, 937))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_15.setContentsMargins(0, 0, 0, -1)
        self.verticalLayout_15.setSpacing(10)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_2)
        self.textBrowser_2.setMinimumSize(QtCore.QSize(0, 80))
        self.textBrowser_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.textBrowser_2.setStyleSheet("border: none;\n"
"border-color: rgb(255, 255, 255);")
        self.textBrowser_2.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.verticalLayout_15.addWidget(self.textBrowser_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setContentsMargins(10, -1, -1, -1)
        self.verticalLayout_16.setSpacing(15)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.label_8 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap(":/tips/images/dsis_1.png"))
        self.label_8.setObjectName("label_8")
        self.verticalLayout_16.addWidget(self.label_8)
        self.label_12 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap(":/tips/images/dsis_2.png"))
        self.label_12.setObjectName("label_12")
        self.verticalLayout_16.addWidget(self.label_12)
        self.label_13 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap(":/tips/images/dsis_3.png"))
        self.label_13.setObjectName("label_13")
        self.verticalLayout_16.addWidget(self.label_13)
        self.label_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap(":/tips/images/dsis_4.png"))
        self.label_7.setObjectName("label_7")
        self.verticalLayout_16.addWidget(self.label_7)
        self.horizontalLayout_2.addLayout(self.verticalLayout_16)
        self.label_14 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_2.addWidget(self.label_14)
        self.horizontalLayout_2.setStretch(1, 1)
        self.verticalLayout_15.addLayout(self.horizontalLayout_2)
        self.verticalLayout_15.setStretch(0, 1)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_18.addWidget(self.scrollArea_2)
        tips_Wizard.addPage(self.dsis_data_style)
        self.dis_pane_style = QtWidgets.QWizardPage()
        self.dis_pane_style.setObjectName("dis_pane_style")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.dis_pane_style)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.scrollArea_8 = QtWidgets.QScrollArea(self.dis_pane_style)
        self.scrollArea_8.setStyleSheet("QScrollArea{\n"
"    border: 0px solid;\n"
"    border-right-width: 1px;\n"
"    border-right-color: #dcdbdc;\n"
"    background-color: #f5f5f7;\n"
"}\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #f5f5f7;\n"
"    width: 10px;\n"
"    margin: 0px 0 0px 0;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background: Gainsboro;\n"
"    min-height: 20px;\n"
"    border-radius: 5px;\n"
"    border: none;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"    border: 0px solid grey;\n"
"    background: #32CC99;\n"
"    height: 0px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"    border: 0px solid grey;\n"
"    background: #32CC99;\n"
"    height: 0px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"    width: 0px;\n"
"    height: 0px;\n"
"}")
        self.scrollArea_8.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea_8.setWidgetResizable(True)
        self.scrollArea_8.setObjectName("scrollArea_8")
        self.scrollAreaWidgetContents_8 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_8.setGeometry(QtCore.QRect(0, 0, 943, 525))
        self.scrollAreaWidgetContents_8.setObjectName("scrollAreaWidgetContents_8")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_8)
        self.verticalLayout_17.setContentsMargins(0, 0, 0, -1)
        self.verticalLayout_17.setSpacing(10)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_8)
        self.textBrowser_3.setMinimumSize(QtCore.QSize(0, 120))
        self.textBrowser_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.textBrowser_3.setStyleSheet("border: none;\n"
"border-color: rgb(255, 255, 255);")
        self.textBrowser_3.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.verticalLayout_17.addWidget(self.textBrowser_3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout()
        self.verticalLayout_19.setContentsMargins(10, -1, -1, -1)
        self.verticalLayout_19.setSpacing(15)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.label_9 = QtWidgets.QLabel(self.scrollAreaWidgetContents_8)
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap(":/tips/images/dis_style.png"))
        self.label_9.setObjectName("label_9")
        self.verticalLayout_19.addWidget(self.label_9, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout_3.addLayout(self.verticalLayout_19)
        self.label_17 = QtWidgets.QLabel(self.scrollAreaWidgetContents_8)
        self.label_17.setText("")
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_3.addWidget(self.label_17)
        self.horizontalLayout_3.setStretch(1, 1)
        self.verticalLayout_17.addLayout(self.horizontalLayout_3)
        self.verticalLayout_17.setStretch(1, 1)
        self.scrollArea_8.setWidget(self.scrollAreaWidgetContents_8)
        self.verticalLayout_3.addWidget(self.scrollArea_8)
        tips_Wizard.addPage(self.dis_pane_style)
        self.mark_style = QtWidgets.QWizardPage()
        self.mark_style.setObjectName("mark_style")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.mark_style)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.scrollArea_9 = QtWidgets.QScrollArea(self.mark_style)
        self.scrollArea_9.setStyleSheet("QScrollArea{\n"
"    border: 0px solid;\n"
"    border-right-width: 1px;\n"
"    border-right-color: #dcdbdc;\n"
"    background-color: #f5f5f7;\n"
"}\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #f5f5f7;\n"
"    width: 10px;\n"
"    margin: 0px 0 0px 0;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background: Gainsboro;\n"
"    min-height: 20px;\n"
"    border-radius: 5px;\n"
"    border: none;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"    border: 0px solid grey;\n"
"    background: #32CC99;\n"
"    height: 0px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"    border: 0px solid grey;\n"
"    background: #32CC99;\n"
"    height: 0px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"    width: 0px;\n"
"    height: 0px;\n"
"}")
        self.scrollArea_9.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea_9.setWidgetResizable(True)
        self.scrollArea_9.setObjectName("scrollArea_9")
        self.scrollAreaWidgetContents_9 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_9.setGeometry(QtCore.QRect(0, 0, 1010, 748))
        self.scrollAreaWidgetContents_9.setObjectName("scrollAreaWidgetContents_9")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_9)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_9)
        self.textBrowser_4.setMinimumSize(QtCore.QSize(0, 120))
        self.textBrowser_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.textBrowser_4.setStyleSheet("border: none;\n"
"border-color: rgb(255, 255, 255);")
        self.textBrowser_4.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.verticalLayout_5.addWidget(self.textBrowser_4)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.label_15 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        self.label_15.setText("")
        self.label_15.setPixmap(QtGui.QPixmap(":/tips/images/hualun_5.png"))
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/tips/images/hualun_100.png"))
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/tips/images/slide_5.png"))
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(":/tips/images/slide_100.png"))
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 1, 1, 1)
        self.horizontalLayout_4.addLayout(self.gridLayout)
        self.label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.verticalLayout_5.setStretch(1, 1)
        self.scrollArea_9.setWidget(self.scrollAreaWidgetContents_9)
        self.verticalLayout_4.addWidget(self.scrollArea_9)
        tips_Wizard.addPage(self.mark_style)
        self.tool_hide = QtWidgets.QWizardPage()
        self.tool_hide.setObjectName("tool_hide")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tool_hide)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.scrollArea_10 = QtWidgets.QScrollArea(self.tool_hide)
        self.scrollArea_10.setStyleSheet("QScrollArea{\n"
"    border: 0px solid;\n"
"    border-right-width: 1px;\n"
"    border-right-color: #dcdbdc;\n"
"    background-color: #f5f5f7;\n"
"}\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #f5f5f7;\n"
"    width: 10px;\n"
"    margin: 0px 0 0px 0;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background: Gainsboro;\n"
"    min-height: 20px;\n"
"    border-radius: 5px;\n"
"    border: none;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"    border: 0px solid grey;\n"
"    background: #32CC99;\n"
"    height: 0px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"    border: 0px solid grey;\n"
"    background: #32CC99;\n"
"    height: 0px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"    width: 0px;\n"
"    height: 0px;\n"
"}")
        self.scrollArea_10.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea_10.setWidgetResizable(True)
        self.scrollArea_10.setObjectName("scrollArea_10")
        self.scrollAreaWidgetContents_10 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_10.setGeometry(QtCore.QRect(0, 0, 934, 1010))
        self.scrollAreaWidgetContents_10.setObjectName("scrollAreaWidgetContents_10")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_10)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_10)
        self.textBrowser_5.setMinimumSize(QtCore.QSize(0, 120))
        self.textBrowser_5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.textBrowser_5.setStyleSheet("border: none;\n"
"border-color: rgb(255, 255, 255);")
        self.textBrowser_5.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.verticalLayout_6.addWidget(self.textBrowser_5)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSpacing(10)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_16 = QtWidgets.QLabel(self.scrollAreaWidgetContents_10)
        self.label_16.setText("")
        self.label_16.setPixmap(QtGui.QPixmap(":/tips/images/tool_hide.png"))
        self.label_16.setObjectName("label_16")
        self.gridLayout_2.addWidget(self.label_16, 0, 0, 1, 1)
        self.horizontalLayout_5.addLayout(self.gridLayout_2)
        self.label_20 = QtWidgets.QLabel(self.scrollAreaWidgetContents_10)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_5.addWidget(self.label_20)
        self.verticalLayout_6.addLayout(self.horizontalLayout_5)
        self.verticalLayout_6.setStretch(1, 1)
        self.scrollArea_10.setWidget(self.scrollAreaWidgetContents_10)
        self.verticalLayout_7.addWidget(self.scrollArea_10)
        tips_Wizard.addPage(self.tool_hide)

        self.retranslateUi(tips_Wizard)
        QtCore.QMetaObject.connectSlotsByName(tips_Wizard)

    def retranslateUi(self, tips_Wizard):
        _translate = QtCore.QCoreApplication.translate
        tips_Wizard.setWindowTitle(_translate("tips_Wizard", "一些使用小技巧"))
        self.textBrowser.setHtml(_translate("tips_Wizard", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft YaHei\'; font-size:14pt; font-weight:600;\">Tips 1：</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft YaHei\'; font-size:10pt;\">当您使用的是</span><span style=\" font-family:\'Microsoft YaHei\'; font-size:12pt; font-weight:600; color:#bc0000;\">SS</span><span style=\" font-family:\'Microsoft YaHei\'; font-size:10pt;\">实验，那么您的</span><span style=\" font-family:\'Microsoft YaHei\'; font-size:12pt; font-weight:600; color:#bc0000;\">数据库源文件目录</span><span style=\" font-family:\'Microsoft YaHei\'; font-size:10pt;\">应该是如下的样子(三级目录)，然后地址请您选择根目录下即可；（例如图中的</span><span style=\" font-family:\'Microsoft YaHei\'; font-size:11pt; font-weight:600; color:#5555ff;\">“10.28分组”</span><span style=\" font-family:\'Microsoft YaHei\'; font-size:10pt;\">）</span></p></body></html>"))
        self.textBrowser_2.setHtml(_translate("tips_Wizard", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft YaHei\'; font-size:14pt; font-weight:600;\">Tips 2：</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft YaHei\'; font-size:10pt;\">当您使用的是</span><span style=\" font-family:\'Microsoft YaHei\'; font-size:12pt; font-weight:600; color:#bc0000;\">DSIS</span><span style=\" font-family:\'Microsoft YaHei\'; font-size:10pt;\">实验，那么您的</span><span style=\" font-family:\'Microsoft YaHei\'; font-size:12pt; font-weight:600; color:#bc0000;\">数据库源文件目录</span><span style=\" font-family:\'Microsoft YaHei\'; font-size:10pt;\">应该按照如下要求，然后地址请您选择根目录下即可；（例如图中的</span><span style=\" font-family:\'Microsoft YaHei\'; font-size:11pt; font-weight:600; color:#5555ff;\">“test_for_dsis”</span><span style=\" font-family:\'Microsoft YaHei\'; font-size:10pt;\">）</span></p></body></html>"))
        self.textBrowser_3.setHtml(_translate("tips_Wizard", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft YaHei\'; font-size:14pt; font-weight:600;\">Tips 3：</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft YaHei\'; font-size:10pt;\">您可以选择不同的</span><span style=\" font-family:\'Microsoft YaHei\'; font-size:12pt; font-weight:600; color:#bc0000;\">显示模式</span><span style=\" font-family:\'Microsoft YaHei\'; font-size:10pt;\">，来更好地适用于你设计的实验。但您不必去手动修改面板，系统会自动切换面板，若您未找到时，您可以手动切换面板。</span></p></body></html>"))
        self.textBrowser_4.setHtml(_translate("tips_Wizard", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft YaHei\'; font-size:14pt; font-weight:600;\">Tips 4：</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft YaHei\'; font-size:10pt;\">您可以选择不同的</span><span style=\" font-family:\'Microsoft YaHei\'; font-size:12pt; font-weight:600; color:#bc0000;\">评分等级和样式</span><span style=\" font-family:\'Microsoft YaHei\'; font-size:10pt;\">，来更好地适用于你设计的实验。已有样式如下：</span></p></body></html>"))
        self.label_6.setText(_translate("tips_Wizard", "zz"))
        self.textBrowser_5.setHtml(_translate("tips_Wizard", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft YaHei\'; font-size:14pt; font-weight:600;\">Tips 5：</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft YaHei\'; font-size:10pt;\">当您想专注于主面板，您可以点击右侧</span><span style=\" font-family:\'Microsoft YaHei\'; font-size:12pt; font-weight:600; color:#bc0000;\">评分栏</span><span style=\" font-family:\'Microsoft YaHei\'; font-size:10pt;\">按钮，即可隐藏/显示右侧评分框。</span></p></body></html>"))
        self.label_20.setText(_translate("tips_Wizard", "zz"))
import images_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    tips_Wizard = QtWidgets.QWizard()
    ui = Ui_tips_Wizard()
    ui.setupUi(tips_Wizard)
    tips_Wizard.show()
    sys.exit(app.exec_())
