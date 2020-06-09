from PyQt5.Qt import *
from resource.Get_Info import Ui_Form

class GetInfoPane(QWidget, Ui_Form):


    jumpfrom_getinfo_to_warmup_signal = pyqtSignal()
    jumpfrom_getinfo_to_start_signal = pyqtSignal()

    # register_account_pwd_signal = pyqtSignal(str, str)

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        #打开背景图片的设置
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.m_flag = False
        self.label.setText('<a href="https://www.wjx.cn/jq/58583120.aspx"><img src="./resource/images/backgroung_info_qrcode.jpg"></a>')
        self.label.setOpenExternalLinks(True)
        print(self.label.openExternalLinks())

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

    def get_info_pane_min(self):
        self.setWindowState(Qt.WindowMinimized)

    def get_info_pane_close(self):
        self.close()

    def jump_from_getinfo_to_warmup(self):
        self.jumpfrom_getinfo_to_warmup_signal.emit()

    def jump_from_getinfo_to_start(self):
        self.jumpfrom_getinfo_to_start_signal.emit()

    def is_read_bginfo(self):
        if self.is_read_bginfo_rB.isChecked():
            self.go_to_warmup_btn.setEnabled(True)
        else:
            self.go_to_warmup_btn.setEnabled(False)





if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = GetInfoPane()
    # window.exit_signal.connect(lambda :print("退出"))
    # window.register_account_pwd_signal.connect(lambda a, p: print(a, p))
    window.show()


    sys.exit(app.exec_())