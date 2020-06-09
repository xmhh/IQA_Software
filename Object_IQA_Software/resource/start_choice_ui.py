# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'start_choice_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(900, 600)
        Form.setMinimumSize(QtCore.QSize(900, 600))
        Form.setMaximumSize(QtCore.QSize(900, 600))
        Form.setStyleSheet("QWidget#Form{\n"
"    border-image: url(:/start_choice_ui/images/start_choice_ui_bg__bluesky.jpg);\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(-1, -1, -1, 25)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.title_zh = QtWidgets.QLineEdit(Form)
        self.title_zh.setEnabled(False)
        self.title_zh.setMinimumSize(QtCore.QSize(500, 125))
        self.title_zh.setMaximumSize(QtCore.QSize(500, 125))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(33)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.title_zh.setFont(font)
        self.title_zh.setStyleSheet("background-color: transparent;\n"
"font: 33pt \"黑体\" ;\n"
"color: rgb(255, 255, 255);\n"
"border: none;\n"
"\n"
"")
        self.title_zh.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.title_zh.setReadOnly(True)
        self.title_zh.setObjectName("title_zh")
        self.verticalLayout_3.addWidget(self.title_zh)
        self.title_en = QtWidgets.QLineEdit(Form)
        self.title_en.setEnabled(False)
        self.title_en.setMinimumSize(QtCore.QSize(500, 0))
        self.title_en.setMaximumSize(QtCore.QSize(500, 16777215))
        self.title_en.setStyleSheet("background-color: transparent;\n"
"color:rgb(255, 255, 255);\n"
"font: 17px \"Sitka Display\";\n"
"border: none;")
        self.title_en.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.title_en.setObjectName("title_en")
        self.verticalLayout_3.addWidget(self.title_en)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.label = QtWidgets.QLabel(Form)
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(40, -1, 35, 15)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.start_button = QtWidgets.QPushButton(Form)
        self.start_button.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.start_button.sizePolicy().hasHeightForWidth())
        self.start_button.setSizePolicy(sizePolicy)
        self.start_button.setMinimumSize(QtCore.QSize(120, 120))
        self.start_button.setMaximumSize(QtCore.QSize(120, 120))
        self.start_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.start_button.setStyleSheet("QPushButton:hover {\n"
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
"    font: 30pt \"楷体\";\n"
"    border-radius: 60px;\n"
"    border: 4px;\n"
"}")
        self.start_button.setObjectName("start_button")
        self.horizontalLayout_2.addWidget(self.start_button)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, 20, -1, -1)
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.exit_button = QtWidgets.QPushButton(Form)
        self.exit_button.setMinimumSize(QtCore.QSize(150, 40))
        self.exit_button.setMaximumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.exit_button.setFont(font)
        self.exit_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.exit_button.setStyleSheet("QPushButton:hover {\n"
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
"    font: 18pt \"楷体\";\n"
"    border-radius: 20px;\n"
"    border: 4px;\n"
"}")
        self.exit_button.setCheckable(True)
        self.exit_button.setChecked(False)
        self.exit_button.setObjectName("exit_button")
        self.verticalLayout_2.addWidget(self.exit_button)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.change_skin_button = QtWidgets.QPushButton(Form)
        self.change_skin_button.setMinimumSize(QtCore.QSize(70, 40))
        self.change_skin_button.setMaximumSize(QtCore.QSize(70, 40))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.change_skin_button.setFont(font)
        self.change_skin_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.change_skin_button.setStyleSheet("QPushButton:hover {\n"
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
"    font: 18pt \"楷体\";\n"
"    border-radius: 20px;\n"
"    border: 4px;\n"
"}")
        self.change_skin_button.setCheckable(True)
        self.change_skin_button.setChecked(False)
        self.change_skin_button.setObjectName("change_skin_button")
        self.horizontalLayout.addWidget(self.change_skin_button)
        self.get_info_button = QtWidgets.QPushButton(Form)
        self.get_info_button.setMinimumSize(QtCore.QSize(70, 40))
        self.get_info_button.setMaximumSize(QtCore.QSize(70, 40))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.get_info_button.setFont(font)
        self.get_info_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.get_info_button.setStyleSheet("QPushButton:hover {\n"
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
"    font: 18pt \"楷体\";\n"
"    border-radius: 20px;\n"
"    border: 4px;\n"
"}")
        self.get_info_button.setCheckable(True)
        self.get_info_button.setChecked(False)
        self.get_info_button.setObjectName("get_info_button")
        self.horizontalLayout.addWidget(self.get_info_button)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 8)
        self.horizontalLayout_2.setStretch(2, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 8)
        self.verticalLayout.setStretch(2, 1)

        self.retranslateUi(Form)
        self.start_button.clicked.connect(Form.from_start_to_main_exp)
        self.exit_button.clicked.connect(Form.exit_this_exe)
        self.change_skin_button.clicked.connect(Form.change_skin)
        self.get_info_button.clicked.connect(Form.get_help_info)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.title_zh.setText(_translate("Form", "图像质量评价实验平台"))
        self.title_en.setText(_translate("Form", "Image Subjective Quality Evaluation Experimental Platform"))
        self.start_button.setText(_translate("Form", "开始"))
        self.exit_button.setText(_translate("Form", "退出"))
        self.change_skin_button.setText(_translate("Form", "换肤"))
        self.get_info_button.setText(_translate("Form", "帮助"))
import images_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
