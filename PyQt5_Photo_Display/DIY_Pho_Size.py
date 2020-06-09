import json
import os
from PyQt5.Qt import *
from resource.phosize_diy import Ui_Form


# from PyQt5_Photo_Display.resource.style.FontAwesome import FontAwesomes


class DIYPhoSizePane(QWidget, Ui_Form):
    refresh_pho_size_in_mainpane_signal = pyqtSignal()

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent=None, *args, **kwargs)
        # 设置qss样式
        # self.setStyleSheet(open("resource/style/setting_pane.qss", "rb").read().decode("utf-8"))

        # 打开背景图片的设置
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)

        with open("./settings/configure.json", "r", encoding='UTF-8') as f:
            self.configure = json.load(f)
        f.close()

    def set_constrain(self, max_size):
        self.max_size = max_size
        size_validator = QIntValidator(1, self.max_size)
        self.lineEdit.setValidator(size_validator)
        self.label_13.setText('当前最大可设置的宽为：' + str(self.max_size) )


    def diy_pho_size_changed(self, item):
        if item == '':
            pass
        else:
            if int(item) > int(self.max_size):
                size = self.max_size
                self.lineEdit.setText(str(size))
            else:
                size = int(item)
            mode = self.configure['PhotoDis']['DisplayScale']['CurrentDisScale']
            print('宽长比：', mode)
            if mode == '0':
                ratio = 4/3
            else:
                ratio = 16/9
            self.lineEdit_2.setText(str(int(size/ratio)))

    def ensure_diy_phosize(self):
        if self.lineEdit.text() == '' or int(self.lineEdit.text()) < 10:
            QMessageBox.information(self, '提示', '请您确认您的尺寸设置是否合理。', QMessageBox.Ok)
        else:
            self.lineEdit.setEnabled(False)
            self.configure['PhotoDis']['PhotoSize']['TestSize']['PhoSizeDict']['1'] = self.lineEdit.text() + ',' + self.lineEdit_2.text()


    def rechange_diy_phosize(self):
        self.lineEdit.setEnabled(True)

    def closeEvent(self, event):
        if self.lineEdit.isEnabled():
            QMessageBox.information(self, '提示', '请您点击确认更改按钮，确认保存改设置。', QMessageBox.Ok)
            event.ignore()

        else:
            is_save = QMessageBox.information(self, '提示', '是否保存此设置？', QMessageBox.Yes|QMessageBox.No)
            if is_save == QMessageBox.Yes:
                f = open("settings/configure.json", 'w', encoding='UTF-8')
                json.dump(self.configure, f, indent=4, separators=(',', ':'))
                f.close()
                self.refresh_pho_size_in_mainpane_signal.emit()
            else:
                pass
            event.accept()






if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = DIYPhoSizePane()
    window.set_constrain(max_size=1600)
    # window.exit_signal.connect(lambda :print("退出"))
    # window.register_account_pwd_signal.connect(lambda a, p: print(a, p))
    window.show()

    sys.exit(app.exec_())
