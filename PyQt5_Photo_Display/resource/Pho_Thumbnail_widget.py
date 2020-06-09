# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Pho_Thumbnail_widget.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(337, 296)
        Form.setMinimumSize(QtCore.QSize(0, 0))
        Form.setMaximumSize(QtCore.QSize(350, 350))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.show_pic = QtWidgets.QLabel(Form)
        self.show_pic.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.show_pic.setText("")
        self.show_pic.setObjectName("show_pic")
        self.verticalLayout.addWidget(self.show_pic, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.info_Layout = QtWidgets.QVBoxLayout()
        self.info_Layout.setSpacing(0)
        self.info_Layout.setObjectName("info_Layout")
        self.path_Layout = QtWidgets.QHBoxLayout()
        self.path_Layout.setContentsMargins(30, -1, -1, -1)
        self.path_Layout.setSpacing(30)
        self.path_Layout.setObjectName("path_Layout")
        self.label_54 = QtWidgets.QLabel(Form)
        self.label_54.setText("")
        self.label_54.setObjectName("label_54")
        self.path_Layout.addWidget(self.label_54)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setMinimumSize(QtCore.QSize(32, 32))
        self.label_2.setMaximumSize(QtCore.QSize(32, 32))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/thumbnail_pho_wid/images/path.png"))
        self.label_2.setObjectName("label_2")
        self.path_Layout.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setMinimumSize(QtCore.QSize(150, 22))
        self.lineEdit.setMaximumSize(QtCore.QSize(150, 22))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lineEdit.setFont(font)
        self.lineEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit.setStyleSheet("border:none;\n"
"font: 12pt \"Microsoft YaHei UI\";\n"
"background-color: rgb(240, 240, 240);\n"
"border-radius:10px;")
        self.lineEdit.setText("")
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.path_Layout.addWidget(self.lineEdit, 0, QtCore.Qt.AlignHCenter)
        self.label_51 = QtWidgets.QLabel(Form)
        self.label_51.setText("")
        self.label_51.setObjectName("label_51")
        self.path_Layout.addWidget(self.label_51)
        self.path_Layout.setStretch(0, 1)
        self.path_Layout.setStretch(3, 1)
        self.info_Layout.addLayout(self.path_Layout)
        self.rank_Layout = QtWidgets.QHBoxLayout()
        self.rank_Layout.setContentsMargins(30, -1, -1, -1)
        self.rank_Layout.setSpacing(30)
        self.rank_Layout.setObjectName("rank_Layout")
        self.label_56 = QtWidgets.QLabel(Form)
        self.label_56.setText("")
        self.label_56.setObjectName("label_56")
        self.rank_Layout.addWidget(self.label_56)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setMinimumSize(QtCore.QSize(32, 32))
        self.label_4.setMaximumSize(QtCore.QSize(32, 32))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/thumbnail_pho_wid/images/rank.png"))
        self.label_4.setObjectName("label_4")
        self.rank_Layout.addWidget(self.label_4)
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(150, 22))
        self.lineEdit_3.setMaximumSize(QtCore.QSize(150, 22))
        self.lineEdit_3.setStyleSheet("border:none;\n"
"font: 12pt \"Microsoft YaHei UI\";\n"
"background-color: rgb(240, 240, 240);\n"
"border-radius:10px;")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.rank_Layout.addWidget(self.lineEdit_3, 0, QtCore.Qt.AlignHCenter)
        self.label_53 = QtWidgets.QLabel(Form)
        self.label_53.setText("")
        self.label_53.setObjectName("label_53")
        self.rank_Layout.addWidget(self.label_53)
        self.rank_Layout.setStretch(0, 1)
        self.rank_Layout.setStretch(3, 1)
        self.info_Layout.addLayout(self.rank_Layout)
        self.verticalLayout.addLayout(self.info_Layout)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
import images_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
