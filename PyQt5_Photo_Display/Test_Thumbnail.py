import json
import os
from PyQt5.Qt import *
from PyQt5 import QtGui
# from resource.test_thumbnail import Ui_Form
from resource.Pho_Thumbnail_widget import Ui_Form as thumbnail


class Thumbnail_Pane(QWidget, thumbnail, QListWidgetItem):

    def __init__(self, img_path, mos_score, pho_ratio, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)


        self.img_path = img_path
        self.mos_score = mos_score
        self.ratio_of_photo = pho_ratio
        img = QImage(self.img_path)
        # transform = QTransform()
        # transform.rotate(90)
        # img = img.transformed(transform)
        print("当前手机的尺寸", img.height(), img.width(), self.img_path)
        # if img.height() > img.width():
            # 设置4：3尺寸，如果宽高比是3：4 那么吧label也变一下再展示
        self.show_pic.setFixedSize(280, 210)

        jpg = QtGui.QPixmap(self.img_path).scaled(self.show_pic.width(),
                                                            self.show_pic.height())
        self.show_pic.setPixmap(jpg)
        # else:
        #
        #     self.show_pic.setFixedSize(288,
        #                                288 / self.ratio_of_photo)
        #
        #     jpg = QtGui.QPixmap(self.img_path).scaled(self.show_pic.width(),
        #                                                         self.show_pic.height())
        #     self.show_pic.setPixmap(jpg)


        self.lineEdit.setText(str(self.img_path).split('\\')[-1])
        self.lineEdit_3.setText('当前分数为：' + str(self.mos_score))









class thumbnail_Window(QListWidget):

    def __init__(self, *args, **kwargs):
        super(thumbnail_Window, self).__init__(*args, **kwargs)
        self.resize(350, 500)
        self.setFrameShape(self.NoFrame)  # 无边框
        self.setFlow(self.LeftToRight)  # 从左到右
        self.setWrapping(True)  # 这三个组合可以达到和FlowLayout一样的效果
        self.setResizeMode(self.Adjust)

        self._loadStart = False
        # 连接竖着的滚动条滚动事件
        self.verticalScrollBar().actionTriggered.connect(self.onActionTriggered)


        for i in range(6):
            iwidget = Thumbnail_Pane(img_path='lena256.jpg', mos_score=88, pho_ratio=4/3)
            item = QListWidgetItem(self)
            item.setSizeHint(iwidget.sizeHint())
            self.setItemWidget(item, iwidget)

        self.setSelectionMode(QAbstractItemView.ExtendedSelection)#开启多选模式
        self.setDragDropMode(self.InternalMove)  #内部可选



    def onActionTriggered(self, action):
        pass

    def currentItemChanged(self, item):
        print('item')









if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = thumbnail_Window()
    # window.exit_signal.connect(lambda :print("退出"))
    # window.register_account_pwd_signal.connect(lambda a, p: print(a, p))
    window.show()

    sys.exit(app.exec_())

# with open("./settings/configure.json", "r", encoding='utf-8') as f:
#     configure = json.load(f)
#
#     # with open("./settings/configure.json", "w") as f:
#     #     configure['model_algorithm'] = 'image'
#     #     json.dump(configure, f)
#     print(configure['Ours_IQA_Exp_Pane']['Database']['LoadUrl'])
# #
# f.close()
