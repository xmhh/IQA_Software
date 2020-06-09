# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Get_Info.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1000, 700)
        Form.setMinimumSize(QtCore.QSize(1000, 700))
        Form.setMaximumSize(QtCore.QSize(1000, 700))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Main_Exp/images/app_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("QWidget#Form{\n"
"    border-image: url(:/Get_Info/images/Get_Info_bg_2.jpg);\n"
"}")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(90, 110, 811, 421))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("border: none;")
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.is_read_bginfo_rB = QtWidgets.QRadioButton(Form)
        self.is_read_bginfo_rB.setGeometry(QtCore.QRect(90, 570, 271, 21))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.is_read_bginfo_rB.setFont(font)
        self.is_read_bginfo_rB.setStyleSheet("color: white;")
        self.is_read_bginfo_rB.setChecked(False)
        self.is_read_bginfo_rB.setObjectName("is_read_bginfo_rB")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(840, 540, 150, 150))
        self.label.setMinimumSize(QtCore.QSize(150, 150))
        self.label.setMaximumSize(QtCore.QSize(150, 150))
        self.label.setStyleSheet("border-image: url(:/Get_Info/images/backgroung_info_qrcode.jpg);\n"
"border: none;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(340, 30, 341, 61))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: transparent;\n"
"font: 25pt \"等线\";\n"
"color: rgb(0, 0, 0);\n"
"border: none;")
        self.label_2.setObjectName("label_2")
        self.go_to_warmup_btn = QtWidgets.QPushButton(Form)
        self.go_to_warmup_btn.setEnabled(False)
        self.go_to_warmup_btn.setGeometry(QtCore.QRect(90, 620, 150, 40))
        self.go_to_warmup_btn.setMinimumSize(QtCore.QSize(150, 40))
        self.go_to_warmup_btn.setMaximumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.go_to_warmup_btn.setFont(font)
        self.go_to_warmup_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.go_to_warmup_btn.setStyleSheet("QPushButton {\n"
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
        self.go_to_warmup_btn.setCheckable(True)
        self.go_to_warmup_btn.setChecked(False)
        self.go_to_warmup_btn.setObjectName("go_to_warmup_btn")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(850, 10, 131, 51))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_5 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_5.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_5.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_5.setToolTipDuration(700)
        self.pushButton_5.setStyleSheet("QPushButton {\n"
"    font: 20px;\n"
"    color: rgb(65, 65, 65);\n"
"    background-color: rgb(231, 231, 231);\n"
"    border-radius: 20px;\n"
"    border: 2px;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(209, 0, 0);\n"
"    border: 2px double;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(223, 223, 223);\n"
"}\n"
"")
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_6.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_6.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_6.setToolTipDuration(700)
        self.pushButton_6.setStyleSheet("QPushButton {\n"
"    font: 20px;\n"
"    color: rgb(65, 65, 65);\n"
"    background-color: rgb(231, 231, 231);\n"
"    border-radius: 20px;\n"
"    border: 2px;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(200, 0, 0);\n"
"    border: 2px double;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(223, 223, 223);\n"
"}\n"
"")
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout.addWidget(self.pushButton_6)
        self.go_to_warmup_btn_2 = QtWidgets.QPushButton(Form)
        self.go_to_warmup_btn_2.setEnabled(True)
        self.go_to_warmup_btn_2.setGeometry(QtCore.QRect(260, 620, 150, 40))
        self.go_to_warmup_btn_2.setMinimumSize(QtCore.QSize(150, 40))
        self.go_to_warmup_btn_2.setMaximumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.go_to_warmup_btn_2.setFont(font)
        self.go_to_warmup_btn_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.go_to_warmup_btn_2.setStyleSheet("QPushButton {\n"
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
        self.go_to_warmup_btn_2.setCheckable(True)
        self.go_to_warmup_btn_2.setChecked(False)
        self.go_to_warmup_btn_2.setObjectName("go_to_warmup_btn_2")

        self.retranslateUi(Form)
        self.pushButton_5.clicked.connect(Form.get_info_pane_min)
        self.pushButton_6.clicked.connect(Form.get_info_pane_close)
        self.go_to_warmup_btn.clicked.connect(Form.jump_from_getinfo_to_warmup)
        self.is_read_bginfo_rB.clicked.connect(Form.is_read_bginfo)
        self.go_to_warmup_btn_2.clicked.connect(Form.jump_from_getinfo_to_start)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'仿宋\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-weight:600; background-color:#ffffff;\">请您阅读一下内容，便于您后面的实验，谢谢！</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; background-color:#ffffff;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'黑体\'; font-size:14pt; font-weight:600; color:#4d4d4d;\">研究背景：</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'FangSong\'; font-size:12pt; color:#4d4d4d;\">   当前随手拍照分享已经成为人们日常生活中的重要组成部分。针对智能手机、单反相机等拍照设备及镜头配件的质量评价也因此成为极具商业价值的研究方向，并培育出了法国DXO实验室等众多评测机构。传统摄影器材的质量评价涵盖了清晰度、畸变、动态范围和色彩精度等多种客观检测内容，但如何从多个单项指标的测试中综合得到摄影器材的整体评价，目前依然是一个难题。目前，包括DXO实验室在内的诸多评测机构都没有公开具体的评分算法，其评分的客观性也因此受到质疑。在摄影器材的质量评价中，客观指标的评价和主观质量评价也同样存在差异。例如人们都有过这样的体验：两个不同品牌手机的拍摄图片质量对比中，尽管这两个手机相机的分辨率、对比度等指标都相近，但拍摄的图片的质量感觉可能会有明显差异，其中存在的理论和技术问题正是我们图像所的一个在研课题。</span><span style=\" font-size:12pt;\"> </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'FangSong\'; font-size:12pt; color:#4d4d4d;\">    不仅如此，图像所正在研究一个摄影器材的主观拍摄质量的评价方法，并且尝试提供市场上主流手机的拍摄质量评价排名。</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'黑体\'; font-size:14pt; font-weight:600; color:#4d4d4d;\">实验方法：</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'FangSong\'; font-size:12pt; color:#4d4d4d;\">  针对本次</span><span style=\" font-size:12pt;\">图像主观评价实验，我们采用单刺激离散质量评价方法，但会在第二张屏幕上以幻灯片形式播放同组其他照片，用以辅助您做出判断</span><span style=\" font-family:\'FangSong\'; font-size:12pt; color:#4d4d4d;\">。测试图片共xxx张，分为xxx个组（不同场景），需要您配合的是：</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'FangSong\'; font-size:12pt; color:#4d4d4d;\">     1.请您用手机扫描右下角的二维码，以帮助我们此次主观实验的信息采集，其中主要包括性别、年龄段、是否佩戴眼镜等一些简单内容，我们保证只会将其用于后续模型研究之中。</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'FangSong\'; font-size:12pt; color:#4d4d4d;\">     2.接下来您将首先观看实验预热动画，以帮助您熟悉此次主观实验的内容和评价方法。其中您可以选择反复观看，直至您熟悉如何进行实验的评价。</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'FangSong\'; font-size:12pt; color:#4d4d4d;\">     3.在熟悉实验内容后，您可以选择“继续实验，下一步”，或返回上一步查看具体实验背景和方法，或点击“我已熟悉如何评价”进行正式实验。</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'FangSong\'; font-size:12pt; color:#4d4d4d;\">   4.具体实验：您将在屏幕左侧看到一张照片，并根据他的好坏，给出您认为的得分，得分范围为0-100分，分数越高表示图片质量越好，分数越低则表示质量越低。（大致对应：0分：几乎看不出是什么；20分：非常差；40分：很差；60分：一般；80分：很好；100分：极好的，几乎完美）因此，在实验过程中，屏幕将以第二屏幕幻灯片形式播放同场景的其他照片，用于辅助您观察并评价左侧图片的好坏。一张照片您将有10s的观察时间，接着您有12s的观察时间，做出判断。然后不断持续进行。为了您更好的进行实验，防止审美疲劳，请您根据工作人员的要求进行测试时间的安排。</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'FangSong\'; font-size:12pt; color:#4d4d4d;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'FangSong\'; font-size:12pt; color:#4d4d4d;\">     最后，再次感谢您参与此次图像质量评价实验！祝您实验愉快，生活愉快~</span></p></body></html>"))
        self.is_read_bginfo_rB.setText(_translate("Form", "我已了解此次主观实验的内容"))
        self.label_2.setText(_translate("Form", "实验背景及方法"))
        self.go_to_warmup_btn.setText(_translate("Form", "开始测试预热"))
        self.pushButton_5.setToolTip(_translate("Form", "<html><head/><body><p>最小化</p></body></html>"))
        self.pushButton_5.setText(_translate("Form", "—"))
        self.pushButton_6.setToolTip(_translate("Form", "关闭"))
        self.pushButton_6.setText(_translate("Form", "X"))
        self.go_to_warmup_btn_2.setText(_translate("Form", "返回上一步"))
import images_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
