from PyQt5.Qt import *
from PyQt5 import QtCore
from resource.Warmup_Exp import Ui_Form

class WarmupExpPane(QWidget, Ui_Form):


    jumpfrom_warmup_to_mainexp_signal = pyqtSignal()
    jumpfrom_warmup_to_getinfo_signal = pyqtSignal()

    # register_account_pwd_signal = pyqtSignal(str, str)


    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        #打开背景图片的设置
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.m_flag = False
        self.win_max_flag = False
        # self.start_watch_anima_btn.pressed.connect(self.is_animation_run)


    # def is_animation_run(self):
    #     print(self.animation_group.State())
    #     # if self.animation_group.Running():
    #     #     self.start_watch_anima_btn.setEnabled(False)
    #     # else:
    #     #     self.start_watch_anima_btn.setEnabled(True)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            # self.setCursor(QCursor(Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        # self.setCursor(QCursor(Qt.ArrowCursor))

    def warmup_min(self):
        self.setWindowState(Qt.WindowMinimized)

    def warmup_max(self):
        if self.win_max_flag is False:
            self.setWindowState(Qt.WindowMaximized)
            self.win_max_flag = True
        else:
            self.setWindowState(Qt.WindowNoState)
            self.win_max_flag = False

    def warmup_close(self):
        self.close()

    def start_warmup_animation(self):
        # print("开始预热动画")

        # 图片的动画1
        show_pic_anima = QPropertyAnimation(self.show_pic_lb, b"pos", self.warm_up_dis_widget)
        show_pic_anima.setStartValue(QPoint(-725, self.warmup_wincontrol_widget.y() - 3))
        show_pic_anima.setEndValue(self.show_pic_lb.pos())
        # show_pic_anima.setEndValue(QPoint(11, self.warmup_wincontrol_widget.y() - 3 ))
        show_pic_anima.setDuration(1000)
        show_pic_anima.setEasingCurve(QEasingCurve.OutCubic)
        # show_pic_anima.start(QAbstractAnimation.DeleteWhenStopped)

        # 提示文字的动画1
        show_pic_withword_anima = QPropertyAnimation(self.show_pic_with_word_te, b"pos", self.warm_up_dis_widget)
        show_pic_withword_anima.setStartValue(QPoint(1034, self.show_pic_with_word_te.y()))
        show_pic_withword_anima.setEndValue(self.show_pic_with_word_te.pos())
        show_pic_withword_anima.setDuration(1000)
        show_pic_withword_anima.setEasingCurve(QEasingCurve.OutCubic)
        # show_pic_withword_anima.start(QAbstractAnimation.DeleteWhenStopped)

        # 提示箭头的动画1
        # show_pic_witharrow_anima = QPropertyAnimation(self.show_pic_arrow_lb, b"pos", self.warm_up_dis_widget)
        # show_pic_witharrow_anima.setStartValue(QPoint(1034, self.show_pic_arrow_lb.y()))
        # show_pic_witharrow_anima.setEndValue(self.show_pic_arrow_lb.pos())
        # show_pic_witharrow_anima.setDuration(1000)
        # show_pic_witharrow_anima.setEasingCurve(QEasingCurve.OutCubic)
        # show_pic_witharrow_anima.start(QAbstractAnimation.DeleteWhenStopped)


        animation_group = QSequentialAnimationGroup(self)
        animation_group.addAnimation(show_pic_anima)
        animation_group.addAnimation(show_pic_withword_anima)
        # animation_group.addAnimation(show_pic_witharrow_anima)

        animation_group.start()
        # 设置一下图片、向导语、得分
        _translate = QtCore.QCoreApplication.translate
        self.show_pic_with_word_te.setHtml(_translate("Form",
                                                      "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                      "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                      "p, li { white-space: pre-wrap; }\n"
                                                      "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                                      "<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'黑体\'; font-size:14pt;\">    </span><span style=\" font-size:16pt;\">当您看到左图这样的照片，可以看出，他是不错的照片，那么您就可以旋转下面旋钮，选择您认为的这张图的分数，(一般很少满分)例如：80分。</span></p>\n"
                                                      "<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
                                                      "<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
                                                      "<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">温馨提示：</span><span style=\" font-size:10pt;\">本次动画只有两个，您可以在在演示完动画向导1时，按继续“动画2”，继续观看动画向导2。</span></p></body></html>"))
        self.show_pic_lb.setStyleSheet("border-image: url(:/Warm_up/images/warmup_dis_better.jpg);")
        self.show_score_lcd.display(80)


    def restart_warmup_animation(self):
        # print("继续动画")
        # 图片的动画2
        show_pic_anima2 = QPropertyAnimation(self.show_pic_lb, b"pos", self.warm_up_dis_widget)
        show_pic_anima2.setStartValue(QPoint(-725, self.warmup_wincontrol_widget.y() - 3))
        show_pic_anima2.setEndValue(self.show_pic_lb.pos())
        # show_pic_anima.setEndValue(QPoint(11, self.warmup_wincontrol_widget.y() - 3 ))
        show_pic_anima2.setDuration(1000)
        show_pic_anima2.setEasingCurve(QEasingCurve.OutBounce)
        # show_pic_anima.start(QAbstractAnimation.DeleteWhenStopped)

        # 提示文字的动画2
        show_pic_withword_anima2 = QPropertyAnimation(self.show_pic_with_word_te, b"pos", self.warm_up_dis_widget)
        show_pic_withword_anima2.setStartValue(QPoint(1034, self.show_pic_with_word_te.y()))
        show_pic_withword_anima2.setEndValue(self.show_pic_with_word_te.pos())
        show_pic_withword_anima2.setDuration(1000)
        show_pic_withword_anima2.setEasingCurve(QEasingCurve.OutBounce)
        # show_pic_withword_anima.start(QAbstractAnimation.DeleteWhenStopped)

        # # 提示箭头的动画2
        # show_pic_witharrow_anima2 = QPropertyAnimation(self.show_pic_arrow_lb, b"pos", self.warm_up_dis_widget)
        # show_pic_witharrow_anima2.setStartValue(QPoint(1034, self.show_pic_arrow_lb.y()))
        # show_pic_witharrow_anima2.setEndValue(self.show_pic_arrow_lb.pos())
        # show_pic_witharrow_anima2.setDuration(1000)
        # show_pic_witharrow_anima2.setEasingCurve(QEasingCurve.OutBounce)

        animation_group = QSequentialAnimationGroup(self)
        animation_group.addAnimation(show_pic_anima2)
        animation_group.addAnimation(show_pic_withword_anima2)
        # animation_group.addAnimation(show_pic_witharrow_anima2)

        animation_group.start()
        _translate = QtCore.QCoreApplication.translate
        self.show_pic_with_word_te.setHtml(_translate("Form",
                                                      "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                      "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                      "p, li { white-space: pre-wrap; }\n"
                                                      "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                                      "<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'黑体\'; font-size:14pt;\">    </span><span style=\" font-size:16pt;\">当您看到左图这样的照片，可以看出，他是很差的照片，那么您就可以旋转下面旋钮，选择您认为的这张图的分数，（一般很少0分）例如：40分。</span></p>\n"
                                                      "<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
                                                      "<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
                                                      "<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">温馨提示：</span><span style=\" font-size:10pt;\">本次动画只有两个，您可以在在演示完动画向导1时，按继续“动画2”，继续观看动画向导2。</span></p></body></html>"))
        self.show_pic_lb.setStyleSheet("border-image: url(:/Warm_up/images/warmup_dis_wrose.jpg);")
        self.show_score_lcd.display(40)

    def jump_from_warmup_to_mainexp(self):
        self.jumpfrom_warmup_to_mainexp_signal.emit()
        # print("下一步")

    def jump_from_warmup_to_getinfo(self):
        self.jumpfrom_warmup_to_getinfo_signal.emit()
        # print("上一步")







if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = WarmupExpPane()
    # window.exit_signal.connect(lambda :print("退出"))
    # window.register_account_pwd_signal.connect(lambda a, p: print(a, p))
    window.show()

    sys.exit(app.exec_())