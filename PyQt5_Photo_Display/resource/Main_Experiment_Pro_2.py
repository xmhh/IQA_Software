# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main_Experiment_Pro_2.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1147, 791)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Main_Exp/images/app_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QtCore.QSize(24, 24))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.central_layout = QtWidgets.QHBoxLayout()
        self.central_layout.setSpacing(0)
        self.central_layout.setObjectName("central_layout")
        self.dis_tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.dis_tabWidget.setEnabled(True)
        self.dis_tabWidget.setObjectName("dis_tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.display_widget = QtWidgets.QWidget(self.tab)
        self.display_widget.setStyleSheet("border:2px double;\n"
"border-color: rgb(223, 223, 223);")
        self.display_widget.setObjectName("display_widget")
        self.gridLayout = QtWidgets.QGridLayout(self.display_widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.show_pic_lb = QtWidgets.QLabel(self.display_widget)
        self.show_pic_lb.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.show_pic_lb.setText("")
        self.show_pic_lb.setObjectName("show_pic_lb")
        self.gridLayout.addWidget(self.show_pic_lb, 0, 0, 1, 1)
        self.verticalLayout_7.addWidget(self.display_widget)
        self.dis_tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.display_widget_lr = QtWidgets.QWidget(self.tab_3)
        self.display_widget_lr.setStyleSheet("border:2px double;\n"
"border-color: rgb(223, 223, 223);")
        self.display_widget_lr.setObjectName("display_widget_lr")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.display_widget_lr)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.show_pic_lb_2 = QtWidgets.QLabel(self.display_widget_lr)
        self.show_pic_lb_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.show_pic_lb_2.setWhatsThis("")
        self.show_pic_lb_2.setText("")
        self.show_pic_lb_2.setObjectName("show_pic_lb_2")
        self.horizontalLayout.addWidget(self.show_pic_lb_2, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.show_pic_lb_4 = QtWidgets.QLabel(self.display_widget_lr)
        self.show_pic_lb_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.show_pic_lb_4.setText("")
        self.show_pic_lb_4.setObjectName("show_pic_lb_4")
        self.horizontalLayout.addWidget(self.show_pic_lb_4, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout_6.addWidget(self.display_widget_lr)
        self.dis_tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.display_widget_ud = QtWidgets.QWidget(self.tab_2)
        self.display_widget_ud.setStyleSheet("border:2px double;\n"
"border-color: rgb(223, 223, 223);")
        self.display_widget_ud.setObjectName("display_widget_ud")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.display_widget_ud)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.show_pic_lb_3 = QtWidgets.QLabel(self.display_widget_ud)
        self.show_pic_lb_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.show_pic_lb_3.setText("")
        self.show_pic_lb_3.setObjectName("show_pic_lb_3")
        self.verticalLayout_4.addWidget(self.show_pic_lb_3, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.show_pic_lb_5 = QtWidgets.QLabel(self.display_widget_ud)
        self.show_pic_lb_5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.show_pic_lb_5.setText("")
        self.show_pic_lb_5.setObjectName("show_pic_lb_5")
        self.verticalLayout_4.addWidget(self.show_pic_lb_5, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout_8.addWidget(self.display_widget_ud)
        self.dis_tabWidget.addTab(self.tab_2, "")
        self.central_layout.addWidget(self.dis_tabWidget)
        self.tool_widget = QtWidgets.QTabWidget(self.centralwidget)
        self.tool_widget.setMinimumSize(QtCore.QSize(400, 0))
        self.tool_widget.setMaximumSize(QtCore.QSize(600, 16777215))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.tool_widget.setFont(font)
        self.tool_widget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tool_widget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tool_widget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tool_widget.setIconSize(QtCore.QSize(16, 16))
        self.tool_widget.setElideMode(QtCore.Qt.ElideNone)
        self.tool_widget.setMovable(True)
        self.tool_widget.setObjectName("tool_widget")
        self.toolbox = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolbox.sizePolicy().hasHeightForWidth())
        self.toolbox.setSizePolicy(sizePolicy)
        self.toolbox.setObjectName("toolbox")
        self.verticalLayout_27 = QtWidgets.QVBoxLayout(self.toolbox)
        self.verticalLayout_27.setContentsMargins(0, 3, 0, 0)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        self.tool_widget_2 = QtWidgets.QWidget(self.toolbox)
        self.tool_widget_2.setMinimumSize(QtCore.QSize(290, 0))
        self.tool_widget_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tool_widget_2.setObjectName("tool_widget_2")
        self.verticalLayout_28 = QtWidgets.QVBoxLayout(self.tool_widget_2)
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        self.thumbnail_widget = QtWidgets.QWidget(self.tool_widget_2)
        self.thumbnail_widget.setMinimumSize(QtCore.QSize(290, 0))
        self.thumbnail_widget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.thumbnail_widget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.thumbnail_widget.setStyleSheet("border-radius:20px;\n"
"background-color: rgb(213, 213, 213);")
        self.thumbnail_widget.setObjectName("thumbnail_widget")
        self.verticalLayout_29 = QtWidgets.QVBoxLayout(self.thumbnail_widget)
        self.verticalLayout_29.setContentsMargins(3, 3, 12, 10)
        self.verticalLayout_29.setObjectName("verticalLayout_29")
        self.Thumbnail_pic_lb = QtWidgets.QLabel(self.thumbnail_widget)
        self.Thumbnail_pic_lb.setMinimumSize(QtCore.QSize(290, 0))
        self.Thumbnail_pic_lb.setMaximumSize(QtCore.QSize(600, 600))
        self.Thumbnail_pic_lb.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Thumbnail_pic_lb.setStyleSheet("border:2px double;\n"
"border-color: rgb(223, 223, 223);")
        self.Thumbnail_pic_lb.setText("")
        self.Thumbnail_pic_lb.setAlignment(QtCore.Qt.AlignCenter)
        self.Thumbnail_pic_lb.setObjectName("Thumbnail_pic_lb")
        self.verticalLayout_29.addWidget(self.Thumbnail_pic_lb, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.Thumbnail_info_lb_2 = QtWidgets.QLabel(self.thumbnail_widget)
        self.Thumbnail_info_lb_2.setMinimumSize(QtCore.QSize(291, 25))
        self.Thumbnail_info_lb_2.setMaximumSize(QtCore.QSize(600, 40))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.Thumbnail_info_lb_2.setFont(font)
        self.Thumbnail_info_lb_2.setStyleSheet("border:none;")
        self.Thumbnail_info_lb_2.setObjectName("Thumbnail_info_lb_2")
        self.verticalLayout_29.addWidget(self.Thumbnail_info_lb_2)
        self.progressBar_2 = QtWidgets.QProgressBar(self.thumbnail_widget)
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
        self.verticalLayout_29.addWidget(self.progressBar_2)
        self.Thumbnail_info_lb = QtWidgets.QLabel(self.thumbnail_widget)
        self.Thumbnail_info_lb.setMinimumSize(QtCore.QSize(291, 25))
        self.Thumbnail_info_lb.setMaximumSize(QtCore.QSize(600, 40))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.Thumbnail_info_lb.setFont(font)
        self.Thumbnail_info_lb.setStyleSheet("border:none;")
        self.Thumbnail_info_lb.setObjectName("Thumbnail_info_lb")
        self.verticalLayout_29.addWidget(self.Thumbnail_info_lb)
        self.progressBar = QtWidgets.QProgressBar(self.thumbnail_widget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(11)
        self.progressBar.setFont(font)
        self.progressBar.setStyleSheet("QProgressBar {\n"
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
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_29.addWidget(self.progressBar)
        self.verticalLayout_29.setStretch(0, 8)
        self.verticalLayout_29.setStretch(1, 1)
        self.verticalLayout_29.setStretch(2, 2)
        self.verticalLayout_29.setStretch(3, 1)
        self.verticalLayout_29.setStretch(4, 2)
        self.verticalLayout_28.addWidget(self.thumbnail_widget)
        self.get_score_and_goback_widget = QtWidgets.QWidget(self.tool_widget_2)
        self.get_score_and_goback_widget.setMinimumSize(QtCore.QSize(290, 0))
        self.get_score_and_goback_widget.setMaximumSize(QtCore.QSize(600, 16777215))
        self.get_score_and_goback_widget.setStyleSheet("border-radius: 20px;")
        self.get_score_and_goback_widget.setObjectName("get_score_and_goback_widget")
        self.verticalLayout_30 = QtWidgets.QVBoxLayout(self.get_score_and_goback_widget)
        self.verticalLayout_30.setObjectName("verticalLayout_30")
        self.dial_mark_widget = QtWidgets.QWidget(self.get_score_and_goback_widget)
        self.dial_mark_widget.setObjectName("dial_mark_widget")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.dial_mark_widget)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.verticalLayout_31 = QtWidgets.QVBoxLayout()
        self.verticalLayout_31.setObjectName("verticalLayout_31")
        self.label_3 = QtWidgets.QLabel(self.dial_mark_widget)
        self.label_3.setMinimumSize(QtCore.QSize(160, 0))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(213, 213, 213);\n"
"border-radius:20px;\n"
"color: rgb(255, 255, 255)\n"
"")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_31.addWidget(self.label_3)
        self.show_score_lcd = QtWidgets.QLCDNumber(self.dial_mark_widget)
        self.show_score_lcd.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.show_score_lcd.setAutoFillBackground(False)
        self.show_score_lcd.setStyleSheet("border:2px double;\n"
"border-color: rgb(223, 223, 223);\n"
"background-color: rgb(213, 213, 213);\n"
"color: rgb(90, 90, 90);")
        self.show_score_lcd.setFrameShape(QtWidgets.QFrame.Box)
        self.show_score_lcd.setFrameShadow(QtWidgets.QFrame.Raised)
        self.show_score_lcd.setSmallDecimalPoint(False)
        self.show_score_lcd.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.show_score_lcd.setObjectName("show_score_lcd")
        self.verticalLayout_31.addWidget(self.show_score_lcd)
        self.horizontalLayout_11.addLayout(self.verticalLayout_31)
        self.show_score_dial = QtWidgets.QDial(self.dial_mark_widget)
        self.show_score_dial.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.show_score_dial.setStyleSheet("background-color: rgb(213, 213, 213);")
        self.show_score_dial.setNotchesVisible(True)
        self.show_score_dial.setObjectName("show_score_dial")
        self.horizontalLayout_11.addWidget(self.show_score_dial)
        self.verticalLayout_30.addWidget(self.dial_mark_widget)
        self.slider_mark_widget = QtWidgets.QWidget(self.get_score_and_goback_widget)
        self.slider_mark_widget.setObjectName("slider_mark_widget")
        self.verticalLayout_32 = QtWidgets.QVBoxLayout(self.slider_mark_widget)
        self.verticalLayout_32.setSpacing(20)
        self.verticalLayout_32.setObjectName("verticalLayout_32")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setContentsMargins(20, 10, 20, 10)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_2 = QtWidgets.QLabel(self.slider_mark_widget)
        self.label_2.setMinimumSize(QtCore.QSize(50, 50))
        self.label_2.setMaximumSize(QtCore.QSize(50, 50))
        self.label_2.setStyleSheet("border-image: url(:/Main_Exp/images/bad.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_16.addWidget(self.label_2, 0, QtCore.Qt.AlignBottom)
        self.label_8 = QtWidgets.QLabel(self.slider_mark_widget)
        self.label_8.setMinimumSize(QtCore.QSize(0, 30))
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_16.addWidget(self.label_8)
        self.label_5 = QtWidgets.QLabel(self.slider_mark_widget)
        self.label_5.setMinimumSize(QtCore.QSize(50, 50))
        self.label_5.setMaximumSize(QtCore.QSize(50, 50))
        self.label_5.setStyleSheet("")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_16.addWidget(self.label_5)
        self.label_9 = QtWidgets.QLabel(self.slider_mark_widget)
        self.label_9.setMinimumSize(QtCore.QSize(0, 30))
        self.label_9.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_16.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.slider_mark_widget)
        self.label_10.setMinimumSize(QtCore.QSize(50, 50))
        self.label_10.setMaximumSize(QtCore.QSize(50, 50))
        self.label_10.setStyleSheet("border-image: url(:/Main_Exp/images/good.png);")
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_16.addWidget(self.label_10, 0, QtCore.Qt.AlignVCenter)
        self.horizontalLayout_16.setStretch(1, 1)
        self.horizontalLayout_16.setStretch(3, 1)
        self.verticalLayout_32.addLayout(self.horizontalLayout_16)
        self.horizontalSlider = QtWidgets.QSlider(self.slider_mark_widget)
        self.horizontalSlider.setStyleSheet("QSlider:horizontal {\n"
"    min-height: 28px;\n"
"}\n"
"QSlider::groove:horizontal {\n"
"    height: 5px;\n"
"    background: rgb(222, 222, 222); \n"
"}\n"
"QSlider::handle:horizontal {\n"
"    width: 28px;\n"
"    margin-top: -14px;\n"
"    margin-bottom: -14px;\n"
"    border-radius: 14px;\n"
"    background: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.6 rgba(28, 120, 167, 255), stop:0.7 rgba(210, 210, 210, 100));\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.6 rgba(126, 161, 255, 255), stop:0.7 rgba(255, 255, 255, 100));\n"
"}")
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.verticalLayout_32.addWidget(self.horizontalSlider)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_4 = QtWidgets.QLabel(self.slider_mark_widget)
        self.label_4.setMinimumSize(QtCore.QSize(0, 80))
        self.label_4.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(213, 213, 213);\n"
"border-radius:20px;\n"
"color: rgb(255, 255, 255)\n"
"")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_17.addWidget(self.label_4)
        self.show_score_lcd_2 = QtWidgets.QLCDNumber(self.slider_mark_widget)
        self.show_score_lcd_2.setMinimumSize(QtCore.QSize(0, 40))
        self.show_score_lcd_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.show_score_lcd_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.show_score_lcd_2.setAutoFillBackground(False)
        self.show_score_lcd_2.setStyleSheet("border:2px double;\n"
"border-color: rgb(223, 223, 223);\n"
"background-color: rgb(213, 213, 213);\n"
"color: rgb(90, 90, 90);")
        self.show_score_lcd_2.setFrameShape(QtWidgets.QFrame.Box)
        self.show_score_lcd_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.show_score_lcd_2.setSmallDecimalPoint(False)
        self.show_score_lcd_2.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.show_score_lcd_2.setObjectName("show_score_lcd_2")
        self.horizontalLayout_17.addWidget(self.show_score_lcd_2)
        self.verticalLayout_32.addLayout(self.horizontalLayout_17)
        self.verticalLayout_30.addWidget(self.slider_mark_widget)
        self.label_11 = QtWidgets.QLabel(self.get_score_and_goback_widget)
        self.label_11.setMinimumSize(QtCore.QSize(0, 25))
        self.label_11.setMaximumSize(QtCore.QSize(600, 40))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("border-radius: 3px;\n"
"border:2px double;\n"
"border-color: rgb(223, 223, 223);\n"
"background-color: rgb(213, 213, 213);")
        self.label_11.setObjectName("label_11")
        self.verticalLayout_30.addWidget(self.label_11)
        self.ensure_score_of_this_picture_btn = QtWidgets.QPushButton(self.get_score_and_goback_widget)
        self.ensure_score_of_this_picture_btn.setMinimumSize(QtCore.QSize(0, 60))
        self.ensure_score_of_this_picture_btn.setMaximumSize(QtCore.QSize(600, 16777215))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.ensure_score_of_this_picture_btn.setFont(font)
        self.ensure_score_of_this_picture_btn.setStyleSheet("QPushButton:hover {\n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    \n"
"    background-color: rgb(62, 125, 188);\n"
"    border: 2px double;\n"
"    border-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    color: rgb(88, 88, 88);\n"
"    background-color: rgb(208, 208, 208);\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(73, 147, 221);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 10pt \"微软雅黑\";\n"
"    border-radius: 20px;\n"
"}")
        self.ensure_score_of_this_picture_btn.setCheckable(False)
        self.ensure_score_of_this_picture_btn.setChecked(False)
        self.ensure_score_of_this_picture_btn.setObjectName("ensure_score_of_this_picture_btn")
        self.verticalLayout_30.addWidget(self.ensure_score_of_this_picture_btn)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_18.setContentsMargins(0, 0, -1, -1)
        self.horizontalLayout_18.setSpacing(7)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.goto_pre_photo_btn = QtWidgets.QPushButton(self.get_score_and_goback_widget)
        self.goto_pre_photo_btn.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.goto_pre_photo_btn.setFont(font)
        self.goto_pre_photo_btn.setStyleSheet("QPushButton:hover {\n"
"    background-color: rgb(83, 250, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    \n"
"    background-color: rgb(63, 190, 0);\n"
"    border: 2px double;\n"
"    border-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    \n"
"    background-color: rgb(208, 0, 0);\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(74, 223, 109);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 10pt \"微软雅黑\";\n"
"    border-radius: 20px;\n"
"}")
        self.goto_pre_photo_btn.setCheckable(False)
        self.goto_pre_photo_btn.setChecked(False)
        self.goto_pre_photo_btn.setObjectName("goto_pre_photo_btn")
        self.horizontalLayout_18.addWidget(self.goto_pre_photo_btn)
        self.goto_next_photo_btn = QtWidgets.QPushButton(self.get_score_and_goback_widget)
        self.goto_next_photo_btn.setEnabled(False)
        self.goto_next_photo_btn.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.goto_next_photo_btn.setFont(font)
        self.goto_next_photo_btn.setStyleSheet("QPushButton:hover {\n"
"    background-color: rgb(255, 170, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    \n"
"    background-color: rgb(191, 127, 0);\n"
"    border: 2px double;\n"
"    border-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    \n"
"    background-color: rgb(208, 0, 0);\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(229, 153, 0);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 10pt \"微软雅黑\";\n"
"    border-radius: 20px;\n"
"}")
        self.goto_next_photo_btn.setCheckable(False)
        self.goto_next_photo_btn.setChecked(False)
        self.goto_next_photo_btn.setObjectName("goto_next_photo_btn")
        self.horizontalLayout_18.addWidget(self.goto_next_photo_btn)
        self.verticalLayout_30.addLayout(self.horizontalLayout_18)
        self.verticalLayout_30.setStretch(0, 1)
        self.verticalLayout_30.setStretch(1, 1)
        self.verticalLayout_28.addWidget(self.get_score_and_goback_widget)
        self.verticalLayout_28.setStretch(0, 1)
        self.verticalLayout_28.setStretch(1, 1)
        self.verticalLayout_27.addWidget(self.tool_widget_2)
        self.tool_widget.addTab(self.toolbox, "")
        self.Thumbnail_of_this_group = QtWidgets.QWidget()
        self.Thumbnail_of_this_group.setObjectName("Thumbnail_of_this_group")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.Thumbnail_of_this_group)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label = QtWidgets.QLabel(self.Thumbnail_of_this_group)
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
        self.horizontalLayout_6.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.Thumbnail_of_this_group)
        self.lineEdit.setMinimumSize(QtCore.QSize(150, 30))
        self.lineEdit.setMaximumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border:none;\n"
"font: 15pt \"Microsoft YaHei UI\";\n"
"color: rgb(255, 85, 0);\n"
"background-color: rgb(240, 240, 240);\n"
"border-radius:10px;")
        self.lineEdit.setText("")
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_6.addWidget(self.lineEdit)
        self.label_51 = QtWidgets.QLabel(self.Thumbnail_of_this_group)
        self.label_51.setText("")
        self.label_51.setObjectName("label_51")
        self.horizontalLayout_6.addWidget(self.label_51)
        self.horizontalLayout_6.setStretch(2, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.listWidget = QtWidgets.QListWidget(self.Thumbnail_of_this_group)
        self.listWidget.setMinimumSize(QtCore.QSize(300, 0))
        self.listWidget.setMaximumSize(QtCore.QSize(600, 16777215))
        self.listWidget.setStyleSheet("#listWidget {\n"
"    font: 16px \"黑体\";\n"
"    outline: 0px;\n"
"    background-color: rgb(250, 250, 250);\n"
"}\n"
"\n"
"#listWidget::item {\n"
"    min-height: 80px;\n"
"}\n"
"\n"
"#listWidget::item:hover {\n"
"    background-color: rgb(225, 230, 235);\n"
"}\n"
"\n"
"#listWidget::item:selected {\n"
"    color: white;\n"
"}")
        self.listWidget.setAutoScrollMargin(16)
        self.listWidget.setDragEnabled(True)
        self.listWidget.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.listWidget.setIconSize(QtCore.QSize(132, 99))
        self.listWidget.setGridSize(QtCore.QSize(0, 100))
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.compare_widget = QtWidgets.QWidget(self.Thumbnail_of_this_group)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.compare_widget.setFont(font)
        self.compare_widget.setObjectName("compare_widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.compare_widget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.equal_btn = QtWidgets.QPushButton(self.compare_widget)
        self.equal_btn.setMinimumSize(QtCore.QSize(200, 50))
        self.equal_btn.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(15)
        self.equal_btn.setFont(font)
        self.equal_btn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.equal_btn.setStyleSheet("QPushButton:hover {\n"
"    background:qlineargradient(spread:pad,x1:0,y1:0,x2:1,y2:0,stop:0 #fffbd5,stop:1 #0083b0);border-top-left-radius:2px;border-top-right-radius:2px;\n"
"    \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background:qlineargradient(spread:pad,x1:0,y1:0,x2:1,y2:0,stop:0 #23074d,stop:1 #cc5333);border-top-left-radius:2px;border-top-right-radius:2px;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    color: rgb(88, 88, 88);\n"
"    background-color: rgb(208, 208, 208);\n"
"}\n"
"\n"
"QPushButton {\n"
"    border:2px double;\n"
"    border-color: rgb(223, 223, 223);\n"
"    background:qlineargradient(spread:pad,x1:0,y1:0,x2:1,y2:0,stop:0 #4568dc,stop:1 #b06ab3);border-top-left-radius:2px;border-top-right-radius:2px;\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius:10px;\n"
"}")
        self.equal_btn.setObjectName("equal_btn")
        self.horizontalLayout_2.addWidget(self.equal_btn)
        self.verticalLayout.addWidget(self.compare_widget)
        self.verticalLayout.setStretch(1, 1)
        self.tool_widget.addTab(self.Thumbnail_of_this_group, "")
        self.central_layout.addWidget(self.tool_widget)
        self.control_hide_widget = QtWidgets.QWidget(self.centralwidget)
        self.control_hide_widget.setMaximumSize(QtCore.QSize(30, 16777215))
        self.control_hide_widget.setObjectName("control_hide_widget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.control_hide_widget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.tool_ishide_pb = QtWidgets.QPushButton(self.control_hide_widget)
        self.tool_ishide_pb.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.tool_ishide_pb.setFont(font)
        self.tool_ishide_pb.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tool_ishide_pb.setStyleSheet("QPushButton:hover {\n"
"    background-color: rgb(239, 239, 239);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    \n"
"    background-color: rgb(207, 207, 207);\n"
"    border: 2px double;\n"
"    border-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    color: rgb(88, 88, 88);\n"
"    background-color: rgb(208, 208, 208);\n"
"}\n"
"\n"
"QPushButton {\n"
"    border:2px double;\n"
"    border-color: rgb(223, 223, 223);\n"
"    background-color: rgb(213, 213, 213);\n"
"    color: rgb(0, 0, 0);\n"
"    border-radius:10px;\n"
"}")
        self.tool_ishide_pb.setObjectName("tool_ishide_pb")
        self.verticalLayout_5.addWidget(self.tool_ishide_pb)
        self.second_pane_show_lb = QtWidgets.QPushButton(self.control_hide_widget)
        self.second_pane_show_lb.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.second_pane_show_lb.setFont(font)
        self.second_pane_show_lb.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.second_pane_show_lb.setStyleSheet("QPushButton:hover {\n"
"    background-color: rgb(239, 239, 239);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    \n"
"    background-color: rgb(207, 207, 207);\n"
"    border: 2px double;\n"
"    border-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    color: rgb(88, 88, 88);\n"
"    background-color: rgb(208, 208, 208);\n"
"}\n"
"\n"
"QPushButton {\n"
"    border:2px double;\n"
"    border-color: rgb(223, 223, 223);\n"
"    background-color: rgb(213, 213, 213);\n"
"    color: rgb(0, 0, 0);\n"
"    border-radius:10px;\n"
"}")
        self.second_pane_show_lb.setObjectName("second_pane_show_lb")
        self.verticalLayout_5.addWidget(self.second_pane_show_lb)
        self.no_use_lb = QtWidgets.QLabel(self.control_hide_widget)
        self.no_use_lb.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.no_use_lb.setFont(font)
        self.no_use_lb.setText("")
        self.no_use_lb.setObjectName("no_use_lb")
        self.verticalLayout_5.addWidget(self.no_use_lb)
        self.no_use_2_lb = QtWidgets.QPushButton(self.control_hide_widget)
        self.no_use_2_lb.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.no_use_2_lb.setFont(font)
        self.no_use_2_lb.setText("")
        self.no_use_2_lb.setObjectName("no_use_2_lb")
        self.verticalLayout_5.addWidget(self.no_use_2_lb)
        self.central_layout.addWidget(self.control_hide_widget)
        self.central_layout.setStretch(0, 7)
        self.central_layout.setStretch(1, 3)
        self.verticalLayout_2.addLayout(self.central_layout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1147, 25))
        self.menubar.setMinimumSize(QtCore.QSize(0, 25))
        self.menubar.setMaximumSize(QtCore.QSize(16777215, 25))
        self.menubar.setObjectName("menubar")
        self.more_info_menu = QtWidgets.QMenu(self.menubar)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Main_Exp/images/more.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.more_info_menu.setIcon(icon1)
        self.more_info_menu.setObjectName("more_info_menu")
        self.settings_menu = QtWidgets.QMenu(self.menubar)
        self.settings_menu.setStyleSheet("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Main_Exp/images/setting.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settings_menu.setIcon(icon2)
        self.settings_menu.setObjectName("settings_menu")
        MainWindow.setMenuBar(self.menubar)
        self.action_set_database_source = QtWidgets.QAction(MainWindow)
        self.action_set_database_source.setObjectName("action_set_database_source")
        self.action_set_saveMOS_path = QtWidgets.QAction(MainWindow)
        self.action_set_saveMOS_path.setObjectName("action_set_saveMOS_path")
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.action_7 = QtWidgets.QAction(MainWindow)
        self.action_7.setObjectName("action_7")
        self.action_9 = QtWidgets.QAction(MainWindow)
        self.action_9.setObjectName("action_9")
        self.action_11 = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/Main_Exp/images/help_of_exp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_11.setIcon(icon3)
        self.action_11.setObjectName("action_11")
        self.action_14 = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/Main_Exp/images/about_us.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_14.setIcon(icon4)
        self.action_14.setObjectName("action_14")
        self.action_2 = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/Main_Exp/images/database_setting.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_2.setIcon(icon5)
        self.action_2.setObjectName("action_2")
        self.actionMOS = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/Main_Exp/images/mos_record.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMOS.setIcon(icon6)
        self.actionMOS.setObjectName("actionMOS")
        self.action_4 = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/Main_Exp/images/exp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_4.setIcon(icon7)
        self.action_4.setObjectName("action_4")
        self.action_5 = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/Main_Exp/images/dis.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_5.setIcon(icon8)
        self.action_5.setObjectName("action_5")
        self.action_6 = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/Main_Exp/images/testee.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_6.setIcon(icon9)
        self.action_6.setObjectName("action_6")
        self.action_8 = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/Main_Exp/images/others.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_8.setIcon(icon10)
        self.action_8.setObjectName("action_8")
        self.more_info_menu.addAction(self.action_11)
        self.more_info_menu.addSeparator()
        self.more_info_menu.addAction(self.action_14)
        self.settings_menu.addAction(self.action_2)
        self.settings_menu.addSeparator()
        self.settings_menu.addAction(self.actionMOS)
        self.settings_menu.addSeparator()
        self.settings_menu.addAction(self.action_4)
        self.settings_menu.addSeparator()
        self.settings_menu.addAction(self.action_5)
        self.settings_menu.addSeparator()
        self.settings_menu.addAction(self.action_6)
        self.settings_menu.addSeparator()
        self.settings_menu.addAction(self.action_8)
        self.menubar.addAction(self.settings_menu.menuAction())
        self.menubar.addAction(self.more_info_menu.menuAction())

        self.retranslateUi(MainWindow)
        self.dis_tabWidget.setCurrentIndex(0)
        self.tool_widget.setCurrentIndex(0)
        self.tool_ishide_pb.clicked.connect(MainWindow.hide_tool)
        self.second_pane_show_lb.clicked.connect(MainWindow.second_showpane_show)
        self.show_score_dial.valueChanged['int'].connect(MainWindow.get_user_MOS)
        self.horizontalSlider.valueChanged['int'].connect(MainWindow.get_user_MOS)
        self.ensure_score_of_this_picture_btn.clicked.connect(MainWindow.ensure_this_MOS)
        self.goto_pre_photo_btn.clicked.connect(MainWindow.go_to_pre_photo)
        self.goto_next_photo_btn.clicked.connect(MainWindow.go_to_next_photo)
        self.equal_btn.clicked.connect(MainWindow.ensure_this_sort)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "图像质量评价主实验台"))
        self.dis_tabWidget.setToolTip(_translate("MainWindow", "此面板可用于单刺激实验，同时在右上角显示缩略图；或用于双刺激实验（一屏多张）。用户不必选择。"))
        self.dis_tabWidget.setTabText(self.dis_tabWidget.indexOf(self.tab), _translate("MainWindow", "标准"))
        self.show_pic_lb_2.setToolTip(_translate("MainWindow", "失真照片"))
        self.show_pic_lb_4.setToolTip(_translate("MainWindow", "原始照片"))
        self.dis_tabWidget.setTabText(self.dis_tabWidget.indexOf(self.tab_3), _translate("MainWindow", "单屏左右显示"))
        self.show_pic_lb_3.setToolTip(_translate("MainWindow", "失真照片"))
        self.show_pic_lb_5.setToolTip(_translate("MainWindow", "原始照片"))
        self.dis_tabWidget.setTabText(self.dis_tabWidget.indexOf(self.tab_2), _translate("MainWindow", "单屏上下显示"))
        self.Thumbnail_info_lb_2.setText(_translate("MainWindow", "当前测试组内进度为："))
        self.Thumbnail_info_lb.setText(_translate("MainWindow", "测试总进度为："))
        self.label_3.setText(_translate("MainWindow", "主观评分为："))
        self.label_4.setText(_translate("MainWindow", "主观评分为：\n"
"(分数越高，质量越好)"))
        self.label_11.setText(_translate("MainWindow", "当前照片为："))
        self.ensure_score_of_this_picture_btn.setText(_translate("MainWindow", "确认评分(&E)"))
        self.goto_pre_photo_btn.setText(_translate("MainWindow", "开始评测（&S）"))
        self.goto_next_photo_btn.setText(_translate("MainWindow", "剩余评分时间为："))
        self.tool_widget.setTabText(self.tool_widget.indexOf(self.toolbox), _translate("MainWindow", "评分框"))
        self.label.setText(_translate("MainWindow", "剩余排序时间："))
        self.equal_btn.setText(_translate("MainWindow", "确定此排序"))
        self.tool_widget.setTabText(self.tool_widget.indexOf(self.Thumbnail_of_this_group), _translate("MainWindow", "本组图片缩略图"))
        self.tool_ishide_pb.setText(_translate("MainWindow", "\n"
"工\n"
"具\n"
"栏\n"
""))
        self.second_pane_show_lb.setText(_translate("MainWindow", "\n"
"第\n"
"二\n"
"屏\n"
"幕\n"
""))
        self.more_info_menu.setTitle(_translate("MainWindow", "更多"))
        self.settings_menu.setTitle(_translate("MainWindow", "设置"))
        self.action_set_database_source.setText(_translate("MainWindow", "数据库源地址"))
        self.action_set_saveMOS_path.setText(_translate("MainWindow", "保存MOS文件地址"))
        self.action.setText(_translate("MainWindow", "主展示图片的宽(width)"))
        self.action_3.setText(_translate("MainWindow", "测试图片的宽长比"))
        self.action_7.setText(_translate("MainWindow", "主界面演示时间"))
        self.action_9.setText(_translate("MainWindow", "中灰度场的时间"))
        self.action_11.setText(_translate("MainWindow", "实验帮助"))
        self.action_14.setText(_translate("MainWindow", "有关我们"))
        self.action_2.setText(_translate("MainWindow", "数据库设置"))
        self.action_2.setShortcut(_translate("MainWindow", "Ctrl+Shift+D"))
        self.actionMOS.setText(_translate("MainWindow", "MOS记录"))
        self.action_4.setText(_translate("MainWindow", "实验参数"))
        self.action_5.setText(_translate("MainWindow", "主显示界面"))
        self.action_6.setText(_translate("MainWindow", "测试者信息"))
        self.action_8.setText(_translate("MainWindow", "其他设置"))
import images_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
