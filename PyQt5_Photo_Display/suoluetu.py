# 2020-03-01
# 网上看到了些 关于 QListWidget 有显示图标的功能
# 通过和piexif 结合 把图片的缩略图给显示出来
import sys

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QWidget, QApplication, QListWidget, QListView, QHBoxLayout, QListWidgetItem
import os
import piexif


class IconListWidget(QWidget):
    def __init__(self, parent=None):
        super(IconListWidget, self).__init__(parent)
        self.resize(1024, 768)
        self.setupUi()

    def setupUi(self):
        self.iconlist = QListWidget()
        self.iconlist.setViewMode(QListView.IconMode)
        self.iconlist.setSpacing(10)
        self.iconlist.setIconSize(QSize(100, 100))
        self.iconlist.setMovement(False)
        self.iconlist.setResizeMode(QListView.Adjust)
        hlayout = QHBoxLayout()
        hlayout.addWidget(self.iconlist)

        self.setLayout(hlayout)

        self.additems()

    def additems(self):
        # 读取缩略图
        path = r'C:\Users\xmhh\Desktop\data'
        files = os.listdir(path)
        for f1 in files:
            exif_dict = piexif.load(path + f1)
            thumbnail = exif_dict.pop("thumbnail")
            if thumbnail is not None:
                pix1 = QPixmap()
                pix1.loadFromData(thumbnail, "JPG")

            item1 = QListWidgetItem(QIcon(pix1.scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation)),
                                    os.path.split(f1)[-1])
            self.iconlist.addItem(item1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwin = IconListWidget()
    mainwin.show()
    sys.exit(app.exec_())
