from PyQt5.Qt import *
from resource.start_ui import Ui_Form

class StartPane(QWidget, Ui_Form):


    jumpfrom_start_to_getinfo_signal = pyqtSignal()
    # register_account_pwd_signal = pyqtSignal(str, str)

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        #打开背景图片的设置
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.m_flag = False

        self.pushButton_2.setToolTip('了解更多有关我们课题组的信息')
        self.lineEdit.setEnabled(False)
        self.lineEdit_2.setEnabled(False)

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


    def start_show_more_info(self):
        project_link = "http://gr.xjtu.edu.cn/web/xqmou/iqa"
        QDesktopServices.openUrl(QUrl(project_link))

    def jumpfrom_start_to_getinfo(self):
        self.jumpfrom_start_to_getinfo_signal.emit()

    def start_pane_min(self):
        self.setWindowState(Qt.WindowMinimized)

    def start_pane_close(self):
        self.close()




if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = StartPane()
    # window.exit_signal.connect(lambda :print("退出"))
    # window.register_account_pwd_signal.connect(lambda a, p: print(a, p))
    window.show()

    sys.exit(app.exec_())