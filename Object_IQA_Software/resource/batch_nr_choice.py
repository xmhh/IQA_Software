# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'batch_nr_choice.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(480, 328)
        Form.setStyleSheet("")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.choose_pho_gbox = QtWidgets.QGroupBox(Form)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.choose_pho_gbox.setFont(font)
        self.choose_pho_gbox.setStyleSheet("QGroupBox{\n"
"    border: none;\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius:6px;\n"
"    margin-top:12px;\n"
"}\n"
"QGroupBox:title {\n"
"    color:rgb(28, 120, 167);\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"}\n"
"")
        self.choose_pho_gbox.setObjectName("choose_pho_gbox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.choose_pho_gbox)
        self.verticalLayout.setContentsMargins(-1, 20, -1, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.algo_le = QtWidgets.QLineEdit(self.choose_pho_gbox)
        self.algo_le.setEnabled(False)
        self.algo_le.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.algo_le.setFont(font)
        self.algo_le.setStyleSheet("border:none;")
        self.algo_le.setInputMethodHints(QtCore.Qt.ImhNone)
        self.algo_le.setReadOnly(True)
        self.algo_le.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.algo_le.setObjectName("algo_le")
        self.horizontalLayout_4.addWidget(self.algo_le)
        self.algo_chosen_btn_3 = QtWidgets.QPushButton(self.choose_pho_gbox)
        self.algo_chosen_btn_3.setEnabled(False)
        self.algo_chosen_btn_3.setMinimumSize(QtCore.QSize(160, 30))
        self.algo_chosen_btn_3.setMaximumSize(QtCore.QSize(160, 30))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.algo_chosen_btn_3.setFont(font)
        self.algo_chosen_btn_3.setStyleSheet("QPushButton:hover {\n"
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
"    font: 16pt \"楷体\";\n"
"    border-radius: 15px;\n"
"    border: 4px;\n"
"}")
        self.algo_chosen_btn_3.setObjectName("algo_chosen_btn_3")
        self.horizontalLayout_4.addWidget(self.algo_chosen_btn_3)
        self.horizontalLayout_4.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pho_addr_show_le = QtWidgets.QLineEdit(self.choose_pho_gbox)
        self.pho_addr_show_le.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.pho_addr_show_le.setFont(font)
        self.pho_addr_show_le.setStyleSheet("border:none;")
        self.pho_addr_show_le.setInputMethodHints(QtCore.Qt.ImhNone)
        self.pho_addr_show_le.setReadOnly(True)
        self.pho_addr_show_le.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.pho_addr_show_le.setObjectName("pho_addr_show_le")
        self.horizontalLayout_2.addWidget(self.pho_addr_show_le)
        self.choose_pho_btn = QtWidgets.QPushButton(self.choose_pho_gbox)
        self.choose_pho_btn.setMinimumSize(QtCore.QSize(160, 30))
        self.choose_pho_btn.setMaximumSize(QtCore.QSize(160, 30))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.choose_pho_btn.setFont(font)
        self.choose_pho_btn.setStyleSheet("QPushButton:hover {\n"
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
"    font: 16pt \"楷体\";\n"
"    border-radius: 15px;\n"
"    border: 4px;\n"
"}")
        self.choose_pho_btn.setObjectName("choose_pho_btn")
        self.horizontalLayout_2.addWidget(self.choose_pho_btn)
        self.horizontalLayout_2.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.mos_addr_show_le_2 = QtWidgets.QLineEdit(self.choose_pho_gbox)
        self.mos_addr_show_le_2.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.mos_addr_show_le_2.setFont(font)
        self.mos_addr_show_le_2.setStyleSheet("border:none;")
        self.mos_addr_show_le_2.setInputMethodHints(QtCore.Qt.ImhNone)
        self.mos_addr_show_le_2.setReadOnly(True)
        self.mos_addr_show_le_2.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.mos_addr_show_le_2.setObjectName("mos_addr_show_le_2")
        self.horizontalLayout_3.addWidget(self.mos_addr_show_le_2)
        self.choose_pho_btn_2 = QtWidgets.QPushButton(self.choose_pho_gbox)
        self.choose_pho_btn_2.setMinimumSize(QtCore.QSize(160, 30))
        self.choose_pho_btn_2.setMaximumSize(QtCore.QSize(160, 30))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.choose_pho_btn_2.setFont(font)
        self.choose_pho_btn_2.setStyleSheet("QPushButton:hover {\n"
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
"    font: 16pt \"楷体\";\n"
"    border-radius: 15px;\n"
"    border: 4px;\n"
"}")
        self.choose_pho_btn_2.setObjectName("choose_pho_btn_2")
        self.horizontalLayout_3.addWidget(self.choose_pho_btn_2)
        self.horizontalLayout_3.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addWidget(self.choose_pho_gbox)
        self.choose_pho_gbox_2 = QtWidgets.QGroupBox(Form)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.choose_pho_gbox_2.setFont(font)
        self.choose_pho_gbox_2.setStyleSheet("QGroupBox{\n"
"    border: none;\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius:6px;\n"
"    margin-top:12px;\n"
"}\n"
"QGroupBox:title {\n"
"    color:rgb(28, 120, 167);\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"}\n"
"")
        self.choose_pho_gbox_2.setObjectName("choose_pho_gbox_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.choose_pho_gbox_2)
        self.verticalLayout_4.setContentsMargins(10, 2, 10, 2)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.progressBar_2 = QtWidgets.QProgressBar(self.choose_pho_gbox_2)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(11)
        self.progressBar_2.setFont(font)
        self.progressBar_2.setStyleSheet("QProgressBar {\n"
"    border: 2px solid rgb(206, 206, 206);\n"
"    background-color:rgb(255, 255, 255);\n"
"    border-radius:3px ;\n"
"    boder-style: inset;  \n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"    background-color:rgb(112, 112, 112); \n"
"    border-radius:3px;  \n"
"    margin:2px;\n"
"}\n"
"")
        self.progressBar_2.setProperty("value", 0)
        self.progressBar_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.progressBar_2.setTextVisible(True)
        self.progressBar_2.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar_2.setInvertedAppearance(False)
        self.progressBar_2.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.progressBar_2.setObjectName("progressBar_2")
        self.verticalLayout_4.addWidget(self.progressBar_2)
        self.verticalLayout_2.addWidget(self.choose_pho_gbox_2)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.start_mark_btn = QtWidgets.QPushButton(Form)
        self.start_mark_btn.setEnabled(True)
        self.start_mark_btn.setMinimumSize(QtCore.QSize(100, 50))
        self.start_mark_btn.setMaximumSize(QtCore.QSize(100, 50))
        self.start_mark_btn.setStyleSheet("QPushButton:hover {\n"
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
        self.start_mark_btn.setObjectName("start_mark_btn")
        self.horizontalLayout.addWidget(self.start_mark_btn)
        self.exit_btn = QtWidgets.QPushButton(Form)
        self.exit_btn.setEnabled(True)
        self.exit_btn.setMinimumSize(QtCore.QSize(100, 50))
        self.exit_btn.setMaximumSize(QtCore.QSize(100, 50))
        self.exit_btn.setStyleSheet("QPushButton:hover {\n"
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
        self.exit_btn.setObjectName("exit_btn")
        self.horizontalLayout.addWidget(self.exit_btn)
        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        self.choose_pho_btn.clicked.connect(Form.choose_pho)
        self.start_mark_btn.clicked.connect(Form.start)
        self.exit_btn.clicked.connect(Form.bye)
        self.choose_pho_btn_2.clicked.connect(Form.choose_mos)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.choose_pho_gbox.setTitle(_translate("Form", "数据与算法选择"))
        self.algo_chosen_btn_3.setText(_translate("Form", "已选算法"))
        self.choose_pho_btn.setText(_translate("Form", "图片文件夹"))
        self.choose_pho_btn_2.setText(_translate("Form", "评分记录地址"))
        self.choose_pho_gbox_2.setTitle(_translate("Form", "评分进度"))
        self.start_mark_btn.setText(_translate("Form", "开始评分"))
        self.exit_btn.setText(_translate("Form", "退出"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
