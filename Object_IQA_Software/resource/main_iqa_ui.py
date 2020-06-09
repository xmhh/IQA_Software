# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_iqa_ui.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1065, 764)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("")
        MainWindow.setInputMethodHints(QtCore.Qt.ImhNone)
        MainWindow.setIconSize(QtCore.QSize(30, 30))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.display_widget = QtWidgets.QWidget(self.centralwidget)
        self.display_widget.setObjectName("display_widget")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.display_widget)
        self.verticalLayout_10.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_10.setContentsMargins(4, 9, 9, 4)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.main_show_gbox = QtWidgets.QGroupBox(self.display_widget)
        self.main_show_gbox.setEnabled(True)
        self.main_show_gbox.setStyleSheet("QGroupBox{\n"
"    border: 1px solid  rgb(80, 80, 80);\n"
"    border-radius:6px;\n"
"    margin-top:12px;\n"
"}\n"
"QGroupBox:title {\n"
"    color:rgb(28, 120, 167);\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"}")
        self.main_show_gbox.setAlignment(QtCore.Qt.AlignCenter)
        self.main_show_gbox.setObjectName("main_show_gbox")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.main_show_gbox)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.img_show_lb = QtWidgets.QLabel(self.main_show_gbox)
        self.img_show_lb.setObjectName("img_show_lb")
        self.horizontalLayout_6.addWidget(self.img_show_lb)
        self.img_show_lb_2 = QtWidgets.QLabel(self.main_show_gbox)
        self.img_show_lb_2.setObjectName("img_show_lb_2")
        self.horizontalLayout_6.addWidget(self.img_show_lb_2)
        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 1)
        self.verticalLayout_10.addWidget(self.main_show_gbox)
        self.horizontalLayout_2.addWidget(self.display_widget)
        self.tool_widget = QtWidgets.QTabWidget(self.centralwidget)
        self.tool_widget.setMinimumSize(QtCore.QSize(300, 0))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.tool_widget.setFont(font)
        self.tool_widget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tool_widget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tool_widget.setIconSize(QtCore.QSize(16, 16))
        self.tool_widget.setElideMode(QtCore.Qt.ElideNone)
        self.tool_widget.setMovable(True)
        self.tool_widget.setObjectName("tool_widget")
        self.NR_IQA_tab = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NR_IQA_tab.sizePolicy().hasHeightForWidth())
        self.NR_IQA_tab.setSizePolicy(sizePolicy)
        self.NR_IQA_tab.setObjectName("NR_IQA_tab")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.NR_IQA_tab)
        self.verticalLayout_11.setContentsMargins(0, 3, 0, 0)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.NR_IQA_tab_layout = QtWidgets.QVBoxLayout()
        self.NR_IQA_tab_layout.setContentsMargins(9, 9, 9, 9)
        self.NR_IQA_tab_layout.setSpacing(6)
        self.NR_IQA_tab_layout.setObjectName("NR_IQA_tab_layout")
        self.choose_pho_gbox = QtWidgets.QGroupBox(self.NR_IQA_tab)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.choose_pho_gbox.setFont(font)
        self.choose_pho_gbox.setStyleSheet("QGroupBox{\n"
"    border: 1px solid  rgb(80, 80, 80);\n"
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
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.choose_pho_gbox)
        self.verticalLayout_7.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_7.setSpacing(6)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
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
        self.horizontalLayout_7.addWidget(self.pho_addr_show_le)
        self.choose_pho_btn = QtWidgets.QPushButton(self.choose_pho_gbox)
        self.choose_pho_btn.setMinimumSize(QtCore.QSize(100, 30))
        self.choose_pho_btn.setMaximumSize(QtCore.QSize(100, 30))
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
        self.horizontalLayout_7.addWidget(self.choose_pho_btn)
        self.verticalLayout_7.addLayout(self.horizontalLayout_7)
        self.NR_IQA_tab_layout.addWidget(self.choose_pho_gbox)
        self.algorithm_gbox = QtWidgets.QGroupBox(self.NR_IQA_tab)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.algorithm_gbox.setFont(font)
        self.algorithm_gbox.setStyleSheet("QGroupBox{\n"
"    border: 1px solid rgb(80,80,80);\n"
"    border-radius:6px;\n"
"    margin-top:12px;\n"
"}\n"
"QGroupBox:title {\n"
"    color:rgb(28, 120, 167);\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"}")
        self.algorithm_gbox.setObjectName("algorithm_gbox")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.algorithm_gbox)
        self.verticalLayout_8.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_8.setSpacing(9)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.al_choose_tip_lb = QtWidgets.QLabel(self.algorithm_gbox)
        self.al_choose_tip_lb.setMinimumSize(QtCore.QSize(0, 40))
        self.al_choose_tip_lb.setStyleSheet("border:none;\n"
"font: 12pt \"楷体\";")
        self.al_choose_tip_lb.setObjectName("al_choose_tip_lb")
        self.horizontalLayout_5.addWidget(self.al_choose_tip_lb)
        self.algorithm_comboBox = QtWidgets.QComboBox(self.algorithm_gbox)
        self.algorithm_comboBox.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.algorithm_comboBox.setFont(font)
        self.algorithm_comboBox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(245, 245, 245);")
        self.algorithm_comboBox.setCurrentText("")
        self.algorithm_comboBox.setObjectName("algorithm_comboBox")
        self.horizontalLayout_5.addWidget(self.algorithm_comboBox)
        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 3)
        self.verticalLayout_6.addLayout(self.horizontalLayout_5)
        self.verticalLayout_6.setStretch(0, 1)
        self.verticalLayout_8.addLayout(self.verticalLayout_6)
        self.NR_IQA_tab_layout.addWidget(self.algorithm_gbox)
        self.scale_gbox = QtWidgets.QGroupBox(self.NR_IQA_tab)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.scale_gbox.setFont(font)
        self.scale_gbox.setStyleSheet("QGroupBox{\n"
"    border: 1px solid rgb(80,80,80);\n"
"    border-radius:6px;\n"
"    margin-top:12px;\n"
"}\n"
"QGroupBox:title {\n"
"    color:rgb(28, 120, 167);\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"}")
        self.scale_gbox.setObjectName("scale_gbox")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.scale_gbox)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.zoom_in_btn = QtWidgets.QPushButton(self.scale_gbox)
        self.zoom_in_btn.setMinimumSize(QtCore.QSize(140, 30))
        self.zoom_in_btn.setMaximumSize(QtCore.QSize(140, 30))
        self.zoom_in_btn.setStyleSheet("QPushButton:hover {\n"
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
        self.zoom_in_btn.setObjectName("zoom_in_btn")
        self.verticalLayout_4.addWidget(self.zoom_in_btn)
        self.zoom_out_btn = QtWidgets.QPushButton(self.scale_gbox)
        self.zoom_out_btn.setMinimumSize(QtCore.QSize(140, 30))
        self.zoom_out_btn.setMaximumSize(QtCore.QSize(140, 30))
        self.zoom_out_btn.setStyleSheet("QPushButton:hover {\n"
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
        self.zoom_out_btn.setObjectName("zoom_out_btn")
        self.verticalLayout_4.addWidget(self.zoom_out_btn)
        self.horizontalLayout_8.addLayout(self.verticalLayout_4)
        self.reset_zoom_btn = QtWidgets.QPushButton(self.scale_gbox)
        self.reset_zoom_btn.setMinimumSize(QtCore.QSize(100, 60))
        self.reset_zoom_btn.setMaximumSize(QtCore.QSize(100, 60))
        self.reset_zoom_btn.setStyleSheet("QPushButton:hover {\n"
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
"    border-radius: 20px;\n"
"    border: 4px;\n"
"}")
        self.reset_zoom_btn.setObjectName("reset_zoom_btn")
        self.horizontalLayout_8.addWidget(self.reset_zoom_btn)
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        self.NR_IQA_tab_layout.addWidget(self.scale_gbox)
        self.start_mark_gbox = QtWidgets.QGroupBox(self.NR_IQA_tab)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.start_mark_gbox.setFont(font)
        self.start_mark_gbox.setStyleSheet("QGroupBox{\n"
"    border: 1px solid rgb(80,80,80);\n"
"    border-radius:6px;\n"
"    margin-top:12px;\n"
"}\n"
"QGroupBox:title {\n"
"    color:rgb(28, 120, 167);\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"}")
        self.start_mark_gbox.setObjectName("start_mark_gbox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.start_mark_gbox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_6 = QtWidgets.QLabel(self.start_mark_gbox)
        self.label_6.setMinimumSize(QtCore.QSize(130, 0))
        self.label_6.setMaximumSize(QtCore.QSize(130, 16777215))
        self.label_6.setStyleSheet("font: 12pt \"楷体\";")
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.real_mark_lb = QtWidgets.QLabel(self.start_mark_gbox)
        self.real_mark_lb.setMinimumSize(QtCore.QSize(60, 0))
        self.real_mark_lb.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.real_mark_lb.setFont(font)
        self.real_mark_lb.setAlignment(QtCore.Qt.AlignCenter)
        self.real_mark_lb.setObjectName("real_mark_lb")
        self.horizontalLayout_4.addWidget(self.real_mark_lb)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 1)
        self.horizontalLayout_9.addLayout(self.verticalLayout_2)
        self.start_mark_btn = QtWidgets.QPushButton(self.start_mark_gbox)
        self.start_mark_btn.setEnabled(True)
        self.start_mark_btn.setMinimumSize(QtCore.QSize(100, 60))
        self.start_mark_btn.setMaximumSize(QtCore.QSize(100, 60))
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
        self.horizontalLayout_9.addWidget(self.start_mark_btn)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.NR_IQA_tab_layout.addWidget(self.start_mark_gbox)
        self.mark_info_gbox = QtWidgets.QGroupBox(self.NR_IQA_tab)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.mark_info_gbox.setFont(font)
        self.mark_info_gbox.setStyleSheet("QGroupBox{\n"
"    border: 1px solid rgb(80,80,80);\n"
"    border-radius:6px;\n"
"    margin-top:12px;\n"
"}\n"
"QGroupBox:title {\n"
"    color:rgb(28, 120, 167);\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"}")
        self.mark_info_gbox.setObjectName("mark_info_gbox")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.mark_info_gbox)
        self.verticalLayout_9.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_9.setSpacing(6)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.all_info_of_iqa_te = QtWidgets.QTextEdit(self.mark_info_gbox)
        self.all_info_of_iqa_te.setStyleSheet("border:none;")
        self.all_info_of_iqa_te.setObjectName("all_info_of_iqa_te")
        self.verticalLayout_9.addWidget(self.all_info_of_iqa_te)
        self.NR_IQA_tab_layout.addWidget(self.mark_info_gbox)
        self.NR_IQA_tab_layout.setStretch(4, 1)
        self.verticalLayout_11.addLayout(self.NR_IQA_tab_layout)
        self.tool_widget.addTab(self.NR_IQA_tab, "")
        self.FR_IQA_tab = QtWidgets.QWidget()
        self.FR_IQA_tab.setObjectName("FR_IQA_tab")
        self.verticalLayout_23 = QtWidgets.QVBoxLayout(self.FR_IQA_tab)
        self.verticalLayout_23.setContentsMargins(0, 3, 0, 0)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout()
        self.verticalLayout_22.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.choose_pho_gbox_2 = QtWidgets.QGroupBox(self.FR_IQA_tab)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.choose_pho_gbox_2.setFont(font)
        self.choose_pho_gbox_2.setStyleSheet("QGroupBox{\n"
"    border: 1px solid  rgb(80, 80, 80);\n"
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
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.choose_pho_gbox_2)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pho_addr_show_le_fr_1 = QtWidgets.QLineEdit(self.choose_pho_gbox_2)
        self.pho_addr_show_le_fr_1.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.pho_addr_show_le_fr_1.setFont(font)
        self.pho_addr_show_le_fr_1.setStyleSheet("border:none;")
        self.pho_addr_show_le_fr_1.setInputMethodHints(QtCore.Qt.ImhNone)
        self.pho_addr_show_le_fr_1.setReadOnly(True)
        self.pho_addr_show_le_fr_1.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.pho_addr_show_le_fr_1.setObjectName("pho_addr_show_le_fr_1")
        self.horizontalLayout.addWidget(self.pho_addr_show_le_fr_1)
        self.choose_pho_btn_fr_1 = QtWidgets.QPushButton(self.choose_pho_gbox_2)
        self.choose_pho_btn_fr_1.setMinimumSize(QtCore.QSize(100, 30))
        self.choose_pho_btn_fr_1.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.choose_pho_btn_fr_1.setFont(font)
        self.choose_pho_btn_fr_1.setStyleSheet("QPushButton:hover {\n"
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
"    font: 15pt \"楷体\";\n"
"    border-radius: 15px;\n"
"    border: 4px;\n"
"}")
        self.choose_pho_btn_fr_1.setObjectName("choose_pho_btn_fr_1")
        self.horizontalLayout.addWidget(self.choose_pho_btn_fr_1)
        self.verticalLayout_13.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pho_addr_show_le_fr_2 = QtWidgets.QLineEdit(self.choose_pho_gbox_2)
        self.pho_addr_show_le_fr_2.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.pho_addr_show_le_fr_2.setFont(font)
        self.pho_addr_show_le_fr_2.setStyleSheet("border:none;")
        self.pho_addr_show_le_fr_2.setInputMethodHints(QtCore.Qt.ImhNone)
        self.pho_addr_show_le_fr_2.setReadOnly(True)
        self.pho_addr_show_le_fr_2.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.pho_addr_show_le_fr_2.setObjectName("pho_addr_show_le_fr_2")
        self.horizontalLayout_3.addWidget(self.pho_addr_show_le_fr_2)
        self.choose_pho_btn_fr_2 = QtWidgets.QPushButton(self.choose_pho_gbox_2)
        self.choose_pho_btn_fr_2.setMinimumSize(QtCore.QSize(100, 30))
        self.choose_pho_btn_fr_2.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.choose_pho_btn_fr_2.setFont(font)
        self.choose_pho_btn_fr_2.setStyleSheet("QPushButton:hover {\n"
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
"    font: 15pt \"楷体\";\n"
"    border-radius: 15px;\n"
"    border: 4px;\n"
"}")
        self.choose_pho_btn_fr_2.setObjectName("choose_pho_btn_fr_2")
        self.horizontalLayout_3.addWidget(self.choose_pho_btn_fr_2)
        self.verticalLayout_13.addLayout(self.horizontalLayout_3)
        self.verticalLayout_22.addWidget(self.choose_pho_gbox_2)
        self.algorithm_gbox_2 = QtWidgets.QGroupBox(self.FR_IQA_tab)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.algorithm_gbox_2.setFont(font)
        self.algorithm_gbox_2.setStyleSheet("QGroupBox{\n"
"    border: 1px solid rgb(80,80,80);\n"
"    border-radius:6px;\n"
"    margin-top:12px;\n"
"}\n"
"QGroupBox:title {\n"
"    color:rgb(28, 120, 167);\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"}")
        self.algorithm_gbox_2.setObjectName("algorithm_gbox_2")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.algorithm_gbox_2)
        self.verticalLayout_14.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_14.setSpacing(9)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.al_choose_tip_lb_2 = QtWidgets.QLabel(self.algorithm_gbox_2)
        self.al_choose_tip_lb_2.setMinimumSize(QtCore.QSize(0, 40))
        self.al_choose_tip_lb_2.setStyleSheet("border:none;\n"
"font: 12pt \"楷体\";")
        self.al_choose_tip_lb_2.setObjectName("al_choose_tip_lb_2")
        self.horizontalLayout_10.addWidget(self.al_choose_tip_lb_2)
        self.fr_algorithm_comboBox = QtWidgets.QComboBox(self.algorithm_gbox_2)
        self.fr_algorithm_comboBox.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.fr_algorithm_comboBox.setFont(font)
        self.fr_algorithm_comboBox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(245, 245, 245);")
        self.fr_algorithm_comboBox.setCurrentText("")
        self.fr_algorithm_comboBox.setObjectName("fr_algorithm_comboBox")
        self.horizontalLayout_10.addWidget(self.fr_algorithm_comboBox)
        self.horizontalLayout_10.setStretch(0, 1)
        self.horizontalLayout_10.setStretch(1, 3)
        self.verticalLayout_15.addLayout(self.horizontalLayout_10)
        self.verticalLayout_15.setStretch(0, 1)
        self.verticalLayout_14.addLayout(self.verticalLayout_15)
        self.verticalLayout_22.addWidget(self.algorithm_gbox_2)
        self.scale_gbox_2 = QtWidgets.QGroupBox(self.FR_IQA_tab)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.scale_gbox_2.setFont(font)
        self.scale_gbox_2.setStyleSheet("QGroupBox{\n"
"    border: 1px solid rgb(80,80,80);\n"
"    border-radius:6px;\n"
"    margin-top:12px;\n"
"}\n"
"QGroupBox:title {\n"
"    color:rgb(28, 120, 167);\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"}")
        self.scale_gbox_2.setObjectName("scale_gbox_2")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.scale_gbox_2)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.zoom_in_btn_fr = QtWidgets.QPushButton(self.scale_gbox_2)
        self.zoom_in_btn_fr.setMinimumSize(QtCore.QSize(140, 30))
        self.zoom_in_btn_fr.setMaximumSize(QtCore.QSize(140, 30))
        self.zoom_in_btn_fr.setStyleSheet("QPushButton:hover {\n"
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
"    font: 15pt \"楷体\";\n"
"    border-radius: 15px;\n"
"    border: 4px;\n"
"}")
        self.zoom_in_btn_fr.setObjectName("zoom_in_btn_fr")
        self.verticalLayout_17.addWidget(self.zoom_in_btn_fr)
        self.zoom_out_btn_fr = QtWidgets.QPushButton(self.scale_gbox_2)
        self.zoom_out_btn_fr.setMinimumSize(QtCore.QSize(140, 30))
        self.zoom_out_btn_fr.setMaximumSize(QtCore.QSize(140, 30))
        self.zoom_out_btn_fr.setStyleSheet("QPushButton:hover {\n"
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
"    font: 15pt \"楷体\";\n"
"    border-radius: 15px;\n"
"    border: 4px;\n"
"}")
        self.zoom_out_btn_fr.setObjectName("zoom_out_btn_fr")
        self.verticalLayout_17.addWidget(self.zoom_out_btn_fr)
        self.horizontalLayout_12.addLayout(self.verticalLayout_17)
        self.reset_zoom_btn_2 = QtWidgets.QPushButton(self.scale_gbox_2)
        self.reset_zoom_btn_2.setMinimumSize(QtCore.QSize(100, 60))
        self.reset_zoom_btn_2.setMaximumSize(QtCore.QSize(100, 60))
        self.reset_zoom_btn_2.setStyleSheet("QPushButton:hover {\n"
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
"    font: 15pt \"楷体\";\n"
"    border-radius: 20px;\n"
"    border: 4px;\n"
"}")
        self.reset_zoom_btn_2.setObjectName("reset_zoom_btn_2")
        self.horizontalLayout_12.addWidget(self.reset_zoom_btn_2)
        self.verticalLayout_21.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout()
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.zoom_only_p1_btn_fr = QtWidgets.QPushButton(self.scale_gbox_2)
        self.zoom_only_p1_btn_fr.setMinimumSize(QtCore.QSize(140, 30))
        self.zoom_only_p1_btn_fr.setMaximumSize(QtCore.QSize(140, 30))
        self.zoom_only_p1_btn_fr.setStyleSheet("QPushButton:hover {\n"
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
"    font: 15pt \"楷体\";\n"
"    border-radius: 15px;\n"
"    border: 4px;\n"
"}")
        self.zoom_only_p1_btn_fr.setObjectName("zoom_only_p1_btn_fr")
        self.verticalLayout_18.addWidget(self.zoom_only_p1_btn_fr)
        self.zoom_only_p2_btn_fr = QtWidgets.QPushButton(self.scale_gbox_2)
        self.zoom_only_p2_btn_fr.setMinimumSize(QtCore.QSize(140, 30))
        self.zoom_only_p2_btn_fr.setMaximumSize(QtCore.QSize(140, 30))
        self.zoom_only_p2_btn_fr.setStyleSheet("QPushButton:hover {\n"
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
"    font: 15pt \"楷体\";\n"
"    border-radius: 15px;\n"
"    border: 4px;\n"
"}")
        self.zoom_only_p2_btn_fr.setObjectName("zoom_only_p2_btn_fr")
        self.verticalLayout_18.addWidget(self.zoom_only_p2_btn_fr)
        self.horizontalLayout_13.addLayout(self.verticalLayout_18)
        self.zoom_all_btn_fr = QtWidgets.QPushButton(self.scale_gbox_2)
        self.zoom_all_btn_fr.setMinimumSize(QtCore.QSize(100, 60))
        self.zoom_all_btn_fr.setMaximumSize(QtCore.QSize(100, 60))
        self.zoom_all_btn_fr.setStyleSheet("QPushButton:hover {\n"
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
"    font: 15pt \"楷体\";\n"
"    border-radius: 20px;\n"
"    border: 4px;\n"
"}")
        self.zoom_all_btn_fr.setObjectName("zoom_all_btn_fr")
        self.horizontalLayout_13.addWidget(self.zoom_all_btn_fr)
        self.verticalLayout_21.addLayout(self.horizontalLayout_13)
        self.verticalLayout_22.addWidget(self.scale_gbox_2)
        self.start_mark_gbox_2 = QtWidgets.QGroupBox(self.FR_IQA_tab)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.start_mark_gbox_2.setFont(font)
        self.start_mark_gbox_2.setStyleSheet("QGroupBox{\n"
"    border: 1px solid rgb(80,80,80);\n"
"    border-radius:6px;\n"
"    margin-top:12px;\n"
"}\n"
"QGroupBox:title {\n"
"    color:rgb(28, 120, 167);\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"}")
        self.start_mark_gbox_2.setObjectName("start_mark_gbox_2")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.start_mark_gbox_2)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout()
        self.verticalLayout_19.setSpacing(2)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.label_7 = QtWidgets.QLabel(self.start_mark_gbox_2)
        self.label_7.setMinimumSize(QtCore.QSize(130, 0))
        self.label_7.setMaximumSize(QtCore.QSize(130, 16777215))
        self.label_7.setStyleSheet("font: 12pt \"楷体\";")
        self.label_7.setObjectName("label_7")
        self.verticalLayout_19.addWidget(self.label_7)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.real_mark_lb_fr = QtWidgets.QLabel(self.start_mark_gbox_2)
        self.real_mark_lb_fr.setMinimumSize(QtCore.QSize(60, 0))
        self.real_mark_lb_fr.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.real_mark_lb_fr.setFont(font)
        self.real_mark_lb_fr.setAlignment(QtCore.Qt.AlignCenter)
        self.real_mark_lb_fr.setObjectName("real_mark_lb_fr")
        self.horizontalLayout_15.addWidget(self.real_mark_lb_fr)
        self.verticalLayout_19.addLayout(self.horizontalLayout_15)
        self.verticalLayout_19.setStretch(0, 1)
        self.verticalLayout_19.setStretch(1, 1)
        self.horizontalLayout_14.addLayout(self.verticalLayout_19)
        self.start_mark_btn_fr = QtWidgets.QPushButton(self.start_mark_gbox_2)
        self.start_mark_btn_fr.setEnabled(True)
        self.start_mark_btn_fr.setMinimumSize(QtCore.QSize(100, 60))
        self.start_mark_btn_fr.setMaximumSize(QtCore.QSize(100, 60))
        self.start_mark_btn_fr.setStyleSheet("QPushButton:hover {\n"
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
"    font: 15pt \"楷体\";\n"
"    border-radius: 20px;\n"
"    border: 4px;\n"
"}")
        self.start_mark_btn_fr.setObjectName("start_mark_btn_fr")
        self.horizontalLayout_14.addWidget(self.start_mark_btn_fr)
        self.verticalLayout_16.addLayout(self.horizontalLayout_14)
        self.verticalLayout_22.addWidget(self.start_mark_gbox_2)
        self.mark_info_gbox_2 = QtWidgets.QGroupBox(self.FR_IQA_tab)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.mark_info_gbox_2.setFont(font)
        self.mark_info_gbox_2.setStyleSheet("QGroupBox{\n"
"    border: 1px solid rgb(80,80,80);\n"
"    border-radius:6px;\n"
"    margin-top:12px;\n"
"}\n"
"QGroupBox:title {\n"
"    color:rgb(28, 120, 167);\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"}")
        self.mark_info_gbox_2.setObjectName("mark_info_gbox_2")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.mark_info_gbox_2)
        self.verticalLayout_20.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_20.setSpacing(6)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.all_info_of_iqa_te_fr = QtWidgets.QTextEdit(self.mark_info_gbox_2)
        self.all_info_of_iqa_te_fr.setStyleSheet("border:none;")
        self.all_info_of_iqa_te_fr.setObjectName("all_info_of_iqa_te_fr")
        self.verticalLayout_20.addWidget(self.all_info_of_iqa_te_fr)
        self.verticalLayout_22.addWidget(self.mark_info_gbox_2)
        self.verticalLayout_22.setStretch(4, 1)
        self.verticalLayout_23.addLayout(self.verticalLayout_22)
        self.tool_widget.addTab(self.FR_IQA_tab, "")
        self.Ours_tab = QtWidgets.QWidget()
        self.Ours_tab.setObjectName("Ours_tab")
        self.tool_widget.addTab(self.Ours_tab, "")
        self.horizontalLayout_2.addWidget(self.tool_widget)
        self.control_hide_widget = QtWidgets.QWidget(self.centralwidget)
        self.control_hide_widget.setMaximumSize(QtCore.QSize(30, 16777215))
        self.control_hide_widget.setObjectName("control_hide_widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.control_hide_widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tool_ishide_pb = QtWidgets.QPushButton(self.control_hide_widget)
        self.tool_ishide_pb.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.tool_ishide_pb.setFont(font)
        self.tool_ishide_pb.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tool_ishide_pb.setStyleSheet("")
        self.tool_ishide_pb.setObjectName("tool_ishide_pb")
        self.verticalLayout.addWidget(self.tool_ishide_pb)
        self.no_use_lb = QtWidgets.QLabel(self.control_hide_widget)
        self.no_use_lb.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.no_use_lb.setFont(font)
        self.no_use_lb.setText("")
        self.no_use_lb.setObjectName("no_use_lb")
        self.verticalLayout.addWidget(self.no_use_lb, 0, QtCore.Qt.AlignHCenter)
        self.no_use_2_lb = QtWidgets.QPushButton(self.control_hide_widget)
        self.no_use_2_lb.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.no_use_2_lb.setFont(font)
        self.no_use_2_lb.setText("")
        self.no_use_2_lb.setObjectName("no_use_2_lb")
        self.verticalLayout.addWidget(self.no_use_2_lb)
        self.horizontalLayout_2.addWidget(self.control_hide_widget)
        self.horizontalLayout_2.setStretch(0, 20)
        self.horizontalLayout_2.setStretch(2, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1065, 25))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")
        self.file_menu = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.file_menu.setFont(font)
        self.file_menu.setObjectName("file_menu")
        self.menuNR_IQA = QtWidgets.QMenu(self.file_menu)
        self.menuNR_IQA.setObjectName("menuNR_IQA")
        self.menuFR_IQA = QtWidgets.QMenu(self.file_menu)
        self.menuFR_IQA.setObjectName("menuFR_IQA")
        self.iqa_menu = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.iqa_menu.setFont(font)
        self.iqa_menu.setObjectName("iqa_menu")
        self.img_enh_menu = QtWidgets.QMenu(self.menubar)
        self.img_enh_menu.setObjectName("img_enh_menu")
        self.img_pro_menu = QtWidgets.QMenu(self.menubar)
        self.img_pro_menu.setObjectName("img_pro_menu")
        self.help_menu = QtWidgets.QMenu(self.menubar)
        self.help_menu.setObjectName("help_menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionBIQI = QtWidgets.QAction(MainWindow)
        self.actionBIQI.setObjectName("actionBIQI")
        self.actionBRISQUE = QtWidgets.QAction(MainWindow)
        self.actionBRISQUE.setObjectName("actionBRISQUE")
        self.actionNIQE = QtWidgets.QAction(MainWindow)
        self.actionNIQE.setObjectName("actionNIQE")
        self.actionBLIINDS_2 = QtWidgets.QAction(MainWindow)
        self.actionBLIINDS_2.setObjectName("actionBLIINDS_2")
        self.actionCPBD = QtWidgets.QAction(MainWindow)
        self.actionCPBD.setObjectName("actionCPBD")
        self.actionDIIVINE = QtWidgets.QAction(MainWindow)
        self.actionDIIVINE.setObjectName("actionDIIVINE")
        self.actionNJQA = QtWidgets.QAction(MainWindow)
        self.actionNJQA.setObjectName("actionNJQA")
        self.actionMSE = QtWidgets.QAction(MainWindow)
        self.actionMSE.setObjectName("actionMSE")
        self.actionRMSE = QtWidgets.QAction(MainWindow)
        self.actionRMSE.setObjectName("actionRMSE")
        self.actionPSNR = QtWidgets.QAction(MainWindow)
        self.actionPSNR.setObjectName("actionPSNR")
        self.actionSSIM = QtWidgets.QAction(MainWindow)
        self.actionSSIM.setObjectName("actionSSIM")
        self.actionUQI = QtWidgets.QAction(MainWindow)
        self.actionUQI.setObjectName("actionUQI")
        self.actionMS_SSIM = QtWidgets.QAction(MainWindow)
        self.actionMS_SSIM.setObjectName("actionMS_SSIM")
        self.actionSCC = QtWidgets.QAction(MainWindow)
        self.actionSCC.setObjectName("actionSCC")
        self.actionRASM = QtWidgets.QAction(MainWindow)
        self.actionRASM.setObjectName("actionRASM")
        self.actionSAM = QtWidgets.QAction(MainWindow)
        self.actionSAM.setObjectName("actionSAM")
        self.actionVIIF_P = QtWidgets.QAction(MainWindow)
        self.actionVIIF_P.setObjectName("actionVIIF_P")
        self.menuNR_IQA.addAction(self.actionBIQI)
        self.menuNR_IQA.addSeparator()
        self.menuNR_IQA.addAction(self.actionBRISQUE)
        self.menuNR_IQA.addSeparator()
        self.menuNR_IQA.addAction(self.actionNIQE)
        self.menuNR_IQA.addSeparator()
        self.menuNR_IQA.addAction(self.actionBLIINDS_2)
        self.menuNR_IQA.addSeparator()
        self.menuNR_IQA.addAction(self.actionCPBD)
        self.menuNR_IQA.addSeparator()
        self.menuNR_IQA.addAction(self.actionNJQA)
        self.menuFR_IQA.addAction(self.actionMSE)
        self.menuFR_IQA.addSeparator()
        self.menuFR_IQA.addAction(self.actionRMSE)
        self.menuFR_IQA.addSeparator()
        self.menuFR_IQA.addAction(self.actionPSNR)
        self.menuFR_IQA.addSeparator()
        self.menuFR_IQA.addAction(self.actionSSIM)
        self.menuFR_IQA.addSeparator()
        self.menuFR_IQA.addAction(self.actionUQI)
        self.menuFR_IQA.addSeparator()
        self.menuFR_IQA.addAction(self.actionMS_SSIM)
        self.menuFR_IQA.addSeparator()
        self.menuFR_IQA.addAction(self.actionSCC)
        self.menuFR_IQA.addSeparator()
        self.menuFR_IQA.addAction(self.actionRASM)
        self.menuFR_IQA.addSeparator()
        self.menuFR_IQA.addAction(self.actionSAM)
        self.menuFR_IQA.addSeparator()
        self.menuFR_IQA.addAction(self.actionVIIF_P)
        self.file_menu.addAction(self.menuNR_IQA.menuAction())
        self.file_menu.addAction(self.menuFR_IQA.menuAction())
        self.menubar.addAction(self.file_menu.menuAction())
        self.menubar.addAction(self.iqa_menu.menuAction())
        self.menubar.addAction(self.img_enh_menu.menuAction())
        self.menubar.addAction(self.img_pro_menu.menuAction())
        self.menubar.addAction(self.help_menu.menuAction())

        self.retranslateUi(MainWindow)
        self.tool_widget.setCurrentIndex(0)
        self.choose_pho_btn.clicked.connect(MainWindow.choose_pho_from_pc)
        self.zoom_in_btn.clicked.connect(MainWindow.pho_zoom_in)
        self.zoom_out_btn.clicked.connect(MainWindow.pho_zoom_out)
        self.reset_zoom_btn.clicked.connect(MainWindow.pho_zoom_reset)
        self.start_mark_btn.clicked.connect(MainWindow.start_mark)
        self.tool_ishide_pb.clicked.connect(MainWindow.ishide_toolmenu)
        self.choose_pho_btn_fr_1.clicked.connect(MainWindow.choose_pho_1_fr)
        self.choose_pho_btn_fr_2.clicked.connect(MainWindow.choose_pho_2_fr)
        self.zoom_in_btn_fr.clicked.connect(MainWindow.pho_zoom_in_fr)
        self.zoom_out_btn_fr.clicked.connect(MainWindow.pho_zoom_out_fr)
        self.zoom_only_p1_btn_fr.clicked.connect(MainWindow.dis_only_p1_fr)
        self.zoom_only_p2_btn_fr.clicked.connect(MainWindow.dis_only_p2_fr)
        self.zoom_all_btn_fr.clicked.connect(MainWindow.dis_all_fr)
        self.reset_zoom_btn_2.clicked.connect(MainWindow.pho_zoom_reset_fr)
        self.start_mark_btn_fr.clicked.connect(MainWindow.start_score_fr)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "图像质量评价主平台"))
        self.main_show_gbox.setTitle(_translate("MainWindow", "主显示区"))
        self.img_show_lb.setText(_translate("MainWindow", "111"))
        self.img_show_lb_2.setText(_translate("MainWindow", "222"))
        self.choose_pho_gbox.setTitle(_translate("MainWindow", "图片文件选择"))
        self.choose_pho_btn.setText(_translate("MainWindow", "选择照片"))
        self.algorithm_gbox.setTitle(_translate("MainWindow", "算法"))
        self.al_choose_tip_lb.setText(_translate("MainWindow", "选择算法："))
        self.scale_gbox.setTitle(_translate("MainWindow", "缩放操作"))
        self.zoom_in_btn.setText(_translate("MainWindow", "放大"))
        self.zoom_out_btn.setText(_translate("MainWindow", "缩小"))
        self.reset_zoom_btn.setText(_translate("MainWindow", "恢复原图"))
        self.start_mark_gbox.setTitle(_translate("MainWindow", "评分结果"))
        self.label_6.setText(_translate("MainWindow", "此图片对的指标为："))
        self.real_mark_lb.setText(_translate("MainWindow", "0"))
        self.start_mark_btn.setText(_translate("MainWindow", "开始评分"))
        self.mark_info_gbox.setTitle(_translate("MainWindow", "评价具体信息"))
        self.tool_widget.setTabText(self.tool_widget.indexOf(self.NR_IQA_tab), _translate("MainWindow", "NR-IQA"))
        self.choose_pho_gbox_2.setTitle(_translate("MainWindow", "图片文件选择"))
        self.choose_pho_btn_fr_1.setText(_translate("MainWindow", "选择图片1"))
        self.choose_pho_btn_fr_2.setText(_translate("MainWindow", "选择图片2"))
        self.algorithm_gbox_2.setTitle(_translate("MainWindow", "算法"))
        self.al_choose_tip_lb_2.setText(_translate("MainWindow", "选择算法："))
        self.scale_gbox_2.setTitle(_translate("MainWindow", "缩放及视图切换操作"))
        self.zoom_in_btn_fr.setText(_translate("MainWindow", "放大"))
        self.zoom_out_btn_fr.setText(_translate("MainWindow", "缩小"))
        self.reset_zoom_btn_2.setText(_translate("MainWindow", "恢复原图"))
        self.zoom_only_p1_btn_fr.setText(_translate("MainWindow", "仅显示图片1"))
        self.zoom_only_p2_btn_fr.setText(_translate("MainWindow", "仅显示图片2"))
        self.zoom_all_btn_fr.setText(_translate("MainWindow", "共同显示"))
        self.start_mark_gbox_2.setTitle(_translate("MainWindow", "评分结果"))
        self.label_7.setText(_translate("MainWindow", "此图片的得分为："))
        self.real_mark_lb_fr.setText(_translate("MainWindow", "0"))
        self.start_mark_btn_fr.setText(_translate("MainWindow", "开始评分"))
        self.mark_info_gbox_2.setTitle(_translate("MainWindow", "评价具体信息"))
        self.tool_widget.setTabText(self.tool_widget.indexOf(self.FR_IQA_tab), _translate("MainWindow", "FR-IQA"))
        self.tool_widget.setTabText(self.tool_widget.indexOf(self.Ours_tab), _translate("MainWindow", "摄影器材IQA"))
        self.tool_ishide_pb.setText(_translate("MainWindow", "工\n"
"具\n"
"栏"))
        self.file_menu.setTitle(_translate("MainWindow", "文件"))
        self.menuNR_IQA.setTitle(_translate("MainWindow", "NR_IQA批处理"))
        self.menuFR_IQA.setTitle(_translate("MainWindow", "FR_IQA批处理"))
        self.iqa_menu.setTitle(_translate("MainWindow", "图像质量评价"))
        self.img_enh_menu.setTitle(_translate("MainWindow", "图像增强"))
        self.img_pro_menu.setTitle(_translate("MainWindow", "基本图像处理"))
        self.help_menu.setTitle(_translate("MainWindow", "帮助"))
        self.actionBIQI.setText(_translate("MainWindow", "BIQI"))
        self.actionBRISQUE.setText(_translate("MainWindow", "BRISQUE"))
        self.actionNIQE.setText(_translate("MainWindow", "NIQE"))
        self.actionBLIINDS_2.setText(_translate("MainWindow", "BLIINDS_2"))
        self.actionCPBD.setText(_translate("MainWindow", "CPBD"))
        self.actionDIIVINE.setText(_translate("MainWindow", "DIIVINE"))
        self.actionNJQA.setText(_translate("MainWindow", "NJQA"))
        self.actionMSE.setText(_translate("MainWindow", "MSE"))
        self.actionRMSE.setText(_translate("MainWindow", "RMSE"))
        self.actionPSNR.setText(_translate("MainWindow", "PSNR"))
        self.actionSSIM.setText(_translate("MainWindow", "SSIM"))
        self.actionUQI.setText(_translate("MainWindow", "UQI"))
        self.actionMS_SSIM.setText(_translate("MainWindow", "MS-SSIM"))
        self.actionSCC.setText(_translate("MainWindow", "SCC"))
        self.actionRASM.setText(_translate("MainWindow", "RASM"))
        self.actionSAM.setText(_translate("MainWindow", "SAM"))
        self.actionVIIF_P.setText(_translate("MainWindow", "VIF_P"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
