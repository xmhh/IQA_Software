import json
import os
from PyQt5.Qt import *
from resource.help_and_tips import Ui_tips_Wizard


# from resource.style.FontAwesome import FontAwesomes


class HelpAndTipsPane(QWidget, Ui_tips_Wizard):

    def __init__(self, parent=None):
        super().__init__(parent)

        # 设置qss样式
        # self.setStyleSheet(open("resource/style/setting_pane.qss", "rb").read().decode("utf-8"))
        self.wizard = QWizard()

        # 打开背景图片的设置
        # self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self.wizard)


        # self.setStyleSheet(open("resource/style/setting_pane.qss", "rb").read().decode("utf-8"))

        # self.setWindowFlag(Qt.FramelessWindowHint)







if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = HelpAndTipsPane()
    # window.exit_signal.connect(lambda :print("退出"))
    # window.register_account_pwd_signal.connect(lambda a, p: print(a, p))
    window.wizard.show()

    sys.exit(app.exec_())


