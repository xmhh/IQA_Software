from PyQt5.Qt import *
from resource.start_choice_ui import Ui_Form
from start_pane_skin import change_skin


class StartChoicePane(QWidget, Ui_Form):

    jumpfrom_start_to_mainexp_signal = pyqtSignal()
    # register_account_pwd_signal = pyqtSignal(str, str)

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        #打开背景图片的设置
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.change_skin_num = 0
        self.m_flag = False

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            # 判断是否鼠标在控件上 后来发现其实不需要，只需要把m_flag初始化！
            # if not (self.start_button.underMouse() or self.exit_button.underMouse() or self.change_skin_button.underMouse() or self.get_info_button.underMouse() ):
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QCursor(Qt.ClosedHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))

    # def enterEvent(self, QEvent):
    #
    #     QEvent.accept()
    #
    # def leaveEvent(self, QEvent):
    #
    #     QEvent.accept()

    def from_start_to_main_exp(self):
        self.jumpfrom_start_to_mainexp_signal.emit()

    def exit_this_exe(self):
        self.close()

    def change_skin(self):
        change_skin(self)

    def get_help_info(self):
        pass






if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = StartChoicePane()
    # window.exit_signal.connect(lambda :print("退出"))
    # window.register_account_pwd_signal.connect(lambda a, p: print(a, p))
    window.show()

    sys.exit(app.exec_())