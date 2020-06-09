from PyQt5.Qt import *
from resource.gt_pho_easypane import Ui_Form

class GTPhoEasyPane(QWidget, Ui_Form):


    jumpfrom_start_to_getinfo_signal = pyqtSignal()
    # register_account_pwd_signal = pyqtSignal(str, str)

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        #打开背景图片的设置
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)

    def work(self):
        self.showMaximized()







if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = GTPhoEasyPane()
    # window.exit_signal.connect(lambda :print("退出"))
    # window.register_account_pwd_signal.connect(lambda a, p: print(a, p))
    window.show()

    sys.exit(app.exec_())