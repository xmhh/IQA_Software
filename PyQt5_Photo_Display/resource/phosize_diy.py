# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'phosize_diy.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(385, 293)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Main_Exp/images/app_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName("verticalLayout")
        self.photo_dis_gbox = QtWidgets.QGroupBox(self.widget)
        self.photo_dis_gbox.setStyleSheet("QGroupBox {\n"
"    font: 20px \"黑体\";\n"
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
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.photo_dis_gbox)
        self.verticalLayout_4.setContentsMargins(-1, 30, -1, 20)
        self.verticalLayout_4.setSpacing(15)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
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
        self.dis_ratio_cbox.setEnabled(False)
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
        self.verticalLayout_4.addLayout(self.horizontalLayout_32)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
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
        self.horizontalLayout_2.addWidget(self.label_12)
        self.label_13 = QtWidgets.QLabel(self.photo_dis_gbox)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: rgb(135, 135, 135);\n"
"font: 10pt \"黑体\";")
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_2.addWidget(self.label_13)
        self.label_2 = QtWidgets.QLabel(self.photo_dis_gbox)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.horizontalLayout_2.setStretch(1, 1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEdit = QtWidgets.QLineEdit(self.photo_dis_gbox)
        self.lineEdit.setMinimumSize(QtCore.QSize(50, 30))
        self.lineEdit.setStyleSheet("border:none;\n"
"font: 10pt \"Microsoft YaHei UI\";\n"
"border-radius:10px;")
        self.lineEdit.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_3.addWidget(self.lineEdit)
        self.label_3 = QtWidgets.QLabel(self.photo_dis_gbox)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.photo_dis_gbox)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_2.setStyleSheet("border:none;\n"
"font: 10pt \"Microsoft YaHei UI\";\n"
"background-color: rgb(240, 240, 240);\n"
"border-radius:10px;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_3.addWidget(self.lineEdit_2)
        self.label = QtWidgets.QLabel(self.photo_dis_gbox)
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.horizontalLayout_3.setStretch(3, 1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout.addWidget(self.photo_dis_gbox)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ensure_btn = QtWidgets.QPushButton(self.widget)
        self.ensure_btn.setEnabled(True)
        self.ensure_btn.setMinimumSize(QtCore.QSize(100, 50))
        self.ensure_btn.setMaximumSize(QtCore.QSize(100, 50))
        self.ensure_btn.setStyleSheet("QPushButton:hover {\n"
"    background-color: rgb(58, 189, 236);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    \n"
"    background-color: rgb(27, 87, 126);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    \n"
"    background-color:rgb(244, 0, 0);\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(28, 120, 167);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 16pt \"楷体\";\n"
"    border-radius: 20px;\n"
"    border: 4px;\n"
"}")
        self.ensure_btn.setObjectName("ensure_btn")
        self.horizontalLayout.addWidget(self.ensure_btn)
        self.rechange_btn = QtWidgets.QPushButton(self.widget)
        self.rechange_btn.setEnabled(True)
        self.rechange_btn.setMinimumSize(QtCore.QSize(100, 50))
        self.rechange_btn.setMaximumSize(QtCore.QSize(100, 50))
        self.rechange_btn.setStyleSheet("QPushButton:hover {\n"
"    background-color: rgb(58, 189, 236);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    \n"
"    background-color: rgb(27, 87, 126);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    \n"
"    background-color:rgb(244, 0, 0);\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(28, 120, 167);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 16pt \"楷体\";\n"
"    border-radius: 20px;\n"
"    border: 4px;\n"
"}")
        self.rechange_btn.setObjectName("rechange_btn")
        self.horizontalLayout.addWidget(self.rechange_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addWidget(self.widget)

        self.retranslateUi(Form)
        self.lineEdit.textChanged['QString'].connect(Form.diy_pho_size_changed)
        self.ensure_btn.clicked.connect(Form.ensure_diy_phosize)
        self.rechange_btn.clicked.connect(Form.rechange_diy_phosize)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.photo_dis_gbox.setTitle(_translate("Form", "图片大小自定义"))
        self.label_17.setText(_translate("Form", "显示比例："))
        self.dis_ratio_cbox.setItemText(0, _translate("Form", "4:3"))
        self.dis_ratio_cbox.setItemText(1, _translate("Form", "16:9"))
        self.label_12.setText(_translate("Form", "图片大小："))
        self.label_3.setText(_translate("Form", "×"))
        self.ensure_btn.setText(_translate("Form", "确认更改"))
        self.rechange_btn.setText(_translate("Form", "重新修改"))
import images_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
