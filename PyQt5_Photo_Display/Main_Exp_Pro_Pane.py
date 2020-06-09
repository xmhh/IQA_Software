from PyQt5.Qt import *
from PyQt5 import QtGui
import os
import time
from resource.Main_Experiment_Pro_2 import Ui_MainWindow
from GT_Pho_EasyPane import GTPhoEasyPane
from Help_and_Tips_Pane import HelpAndTipsPane
from Test_Thumbnail import Thumbnail_Pane

import json


class MainExpProPane(QMainWindow, Ui_MainWindow):
    jump_to_settingpane_signal = pyqtSignal(str)

    # jumpfrom_getinfo_to_start_signal = pyqtSignal()

    # register_account_pwd_signal = pyqtSignal(str, str)

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        # 打开背景图片的设置
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)
        # self.display_widget.hide()
        self.slider_mark_widget.hide()

        self.is_continue = False

        with open("./settings/configure.json", "r", encoding='utf-8') as f:
            self.configure = json.load(f)
        f.close()

        # 设置进度条的样式
        self.progressBar.setStyleSheet(
            "QProgressBar::chunk{background:qlineargradient(spread:pad,x1:0,y1:0,x2:1,y2:0,stop:0 #7474BF,stop:1 #348AC7);}")
        self.progressBar_2.setStyleSheet(
            "QProgressBar::chunk{background:qlineargradient(spread:pad,x1:0,y1:0,x2:1,y2:0,stop:0 #7474BF,stop:1 #348AC7);}")

        self.ratio_of_photo = 4.0 / 3
        self.show_pic_lb.setFixedSize(1080, 810)
        self.w_h_control = 1 #1代表 w>h  0代表h>w  因为三星和lg可能会导致宽高和其他的不一样，因此需要特别去考虑，使得他们与同组的照片宽高在显示的时候一致

        # 初始化一个控制播放时间的定时器
        self.control_timer = QTimer()
        self.timerflag = 0  # 用于判断是评分结束  还是播放结束  10s为一播放周期，然后10s为一评分周期，评分周期在期间使用中灰度图像
        self.time_gap = 500
        self.control_timer.timeout.connect(self.timer_handle)

        # 初始化设置所需参数 包括 数据库源地址\ 保存MOS值的地址 \两个进度条
        """
        初始化不能进行参数计算，因为数据库源地址和MOS地址不一定他环境有！！！！！！1
        """

        self.database_path = ''
        self.save_MOS_path = ''
        self.current_progress_num = 0
        self.all_progress_num = 0

        # 初始化当前测试组和测试组内的图片数,以及所有的图片总数和图片组
        self.photonum_of_current_file = 0
        self.all_photo_num = 0
        self.current_group_name = ''
        self.file_group_list = []
        self.file_group_dict = {}

        # 设置一下菜单栏的信号监听
        self.settings_menu.triggered[QAction].connect(self.change_setting_of_SettingMenu)
        self.more_info_menu.triggered[QAction].connect(self.get_help_or_info)


        self.setting_action_dict = {
            "数据库设置": "0",
            "MOS记录": "1",
            "实验参数": "2",
            "主显示界面": "3",
            "测试者信息": "4",
            "其他设置": "5",
        }

        self.GT_pho_pane = GTPhoEasyPane()

        # self.refresh_settings(is_init=True)

        self.time_control = []

        self.help_tips_pane = HelpAndTipsPane()


        # 设置一下缩略图面板的可拖拽以及多选功能
        # 有问题可以参考一下https://blog.csdn.net/weixin_30252709/article/details/96794583
        # self.listWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)#开启多选模式
        self.listWidget.setDragDropMode(self.listWidget.InternalMove)  #内部可选
        # 定义选中后的查看
        self.listWidget.itemClicked.connect(self.thumbnail_to_show_lr)

        # 判断是否是PEID时刻
        self.peid_sort_time = False
        self.is_peid_warmup = True

        # 由于不能用pop，所以就老老实实用下表记录吧
        self.curr_warmup_pho_num = 0

        # 判断当前需要显示在哪里  left  right
        self.thumbnail_show_where = 'left'

        # 最后时刻
        self.end_time = False

        

    # def mousePressEvent(self, event):
    #     if event.button() == Qt.LeftButton:
    #         self.m_flag = True
    #         self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
    #         event.accept()
    #         # self.setCursor(QCursor(Qt.OpenHandCursor))  # 更改鼠标图标
    #
    # def mouseMoveEvent(self, QMouseEvent):
    #     if Qt.LeftButton and self.m_flag:
    #         self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
    #         QMouseEvent.accept()
    #
    # def mouseReleaseEvent(self, QMouseEvent):
    #     self.m_flag = False
    #     # self.setCursor(QCursor(Qt.ArrowCursor))







    def closeEvent(self, CloseEvent):
        self.GT_pho_pane.close()
        self.help_tips_pane.wizard.close()
        CloseEvent.accept()

    def keyPressEvent(self, QKeyEvent):
        # 评分加减的两个快捷键
        if QKeyEvent.modifiers() == Qt.AltModifier and QKeyEvent.key() == Qt.Key_Up:
            if self.slider_mark_widget.isHidden():
                MOS = min(int(self.show_score_lcd.value()) + 1, int(self.show_score_dial.maximum()))
                self.show_score_dial.setValue(MOS)
                self.show_score_lcd.display(MOS)
            else:
                print(self.horizontalSlider.maximum())
                MOS = min(int(self.show_score_lcd_2.value()) + 1, int(self.horizontalSlider.maximum()))
                self.horizontalSlider.setValue(MOS)
                self.show_score_lcd_2.display(MOS)

        if QKeyEvent.modifiers() == Qt.AltModifier and QKeyEvent.key() == Qt.Key_Down:
            if self.slider_mark_widget.isHidden():
                MOS = max(int(self.show_score_lcd.value()) - 1, int(self.show_score_dial.minimum()))
                self.show_score_dial.setValue(MOS)
                self.show_score_lcd.display(MOS)
            else:
                print(self.horizontalSlider.maximum())
                MOS = max(int(self.show_score_lcd_2.value()) - 1, int(self.horizontalSlider.minimum()))
                self.horizontalSlider.setValue(MOS)
                self.show_score_lcd_2.display(MOS)

    # 设置槽函数
    def thumbnail_to_show_lr(self, item):
        # 获取图片名称 之后在左边显示
        name = item.text().split('\n')[-1]
        path = os.path.join(self.database_path, self.current_group_name, name).replace('\\', "/")
        print(path)
        if self.thumbnail_show_where == 'left':
            self.main_display(is_next=0, special_path=path)
            self.thumbnail_show_where = 'right'
        else:
            self.main_display(is_next=0, special_path=path)
            self.thumbnail_show_where = 'left'


    def change_setting_of_SettingMenu(self, action_name):
        print(action_name.text())
        self.jump_to_settingpane_signal.emit(action_name.text())

    def get_help_or_info(self, action_name):
        if action_name.text() == '实验帮助':
            self.help_tips_pane = HelpAndTipsPane()
            self.help_tips_pane.wizard.show()

        if action_name.text() == '有关我们':
            project_link = "http://gr.xjtu.edu.cn/web/xqmou/iqa"
            QDesktopServices.openUrl(QUrl(project_link))



    def refresh_settings(self, is_init=False):

        with open("./settings/configure.json", "r", encoding='UTF-8') as f:
            self.configure = json.load(f)
        f.close()
        #######################################################################################################
        ############################## 将设置中的数据与实验面板数据进行同步  #######################################
        #######################################################################################################

        ####################################   数据库设置  #####################################################
        self.database_path = self.configure['Database']['LoadUrl']

        # 屏幕选择 放在这里，是因为更新数据的时候，需要看是SS实验还是DSIS实验
        index = self.configure['PhotoDis']['DisForDSIS']['CurrentStyle']
        if index == '0':
            self.dis_tabWidget.setCurrentIndex(0)
            self.dis_mode = 0 #mode 0  ss 缩略图
        if index == '1':
            self.dis_tabWidget.setCurrentIndex(1)
            self.dis_mode = 1  #mode 1  dsis lr
        if index == '2':
            self.dis_tabWidget.setCurrentIndex(2)
            self.dis_mode = 2  #mode 2  dsid ud
        if index == '3':
            self.dis_tabWidget.setCurrentIndex(0)
            self.dis_mode = 3  # mode 3  ss 双屏
        if index == '4':
            self.dis_tabWidget.setCurrentIndex(0)
            self.dis_mode = 4  #mode 4  peid

        if self.dis_mode == 0  or self.dis_mode == 4:
            self.central_layout.setStretchFactor(self.dis_tabWidget, 7)
            self.central_layout.setStretchFactor(self.tool_widget, 3)
        else:
            self.central_layout.setStretchFactor(self.dis_tabWidget, 1)
            self.central_layout.setStretchFactor(self.tool_widget, 0)

        # 重新初始化并计算之前初始化的值
        self.progressBar.setValue(0)
        self.progressBar_2.setValue(0)
        self.current_progress_num = 0
        self.all_progress_num = 0
        self.photonum_of_current_file = 0
        self.all_photo_num = 0
        self.current_group_name = ''
        self.file_group_list = []
        self.file_group_dict = {}

        if self.dis_mode == 0 or self.dis_mode == 3 or self.dis_mode == 4:
            self.database_path_test = self.database_path
        else:
            self.database_path_test = os.path.join(self.database_path, 'DistortedImage')
            self.database_path_real = os.path.join(self.database_path, 'GroundTruth')
        try:
            for files_group_name in os.listdir(self.database_path_test):
                self.file_group_dict[files_group_name] = 0
                self.file_group_list.append(files_group_name)

            for i in range(len(self.file_group_list)):
                for photo in os.listdir(os.path.join(self.database_path_test, self.file_group_list[i])):
                    self.file_group_dict[self.file_group_list[i]] = str(
                        int(self.file_group_dict[self.file_group_list[i]]) + 1)

            for value in self.file_group_dict.values():
                self.all_photo_num += int(value)

            # 为了播放动画，必须初始化一个包含所有图片名的list
            self.allphotoname_in_diff_group_dict = {}
            self.current_photo = None
            self.current_photo_list = []

            for i in range(len(self.file_group_list)):
                # print(i)
                photolist_in_current_group = []
                for photoname in os.listdir(os.path.join(self.database_path_test, self.file_group_list[i])):
                    photolist_in_current_group.append(photoname)
                    # print(photolist_in_current_group)
                self.allphotoname_in_diff_group_dict[str(self.file_group_list[i])] = photolist_in_current_group

                # 接着弹出当前的组内图片列表，以及一张图片
                self.current_photo_list = list(self.allphotoname_in_diff_group_dict[self.file_group_list[0]])
                # print("当前图片组包括的图片、所有图片组的字典为：", self.current_photo_list, self.allphotoname_in_diff_group_dict)

                # 初始化目前的组名和照片数
                self.current_group_name = self.file_group_list[0]
                self.photonum_of_current_file = int(self.file_group_dict[self.current_group_name])

            # # 如果PEID的话，就先生成当前列表的缩略图，为后面的icon减轻压力
            # if self.dis_mode == 4:
            #     self.thumbnail_cache_path = os.path.join(os.getcwd(), 'cache', 'thumbnail_for_peid')
            #
            #     if not os.path.exists( self.thumbnail_cache_path ):
            #         os.makedirs(self.thumbnail_cache_path)
            #
            #     # 先清空cache
            #     for pho in os.listdir(self.thumbnail_cache_path):
            #         os.remove(os.path.join(self.thumbnail_cache_path, pho))

            # for i in range(self.photonum_of_current_file):
            #     thumbnail_part = Thumbnail_Pane(img_path=os.path.join(self.database_path, self.current_group_name, self.current_photo_list[i]), mos_score=88, pho_ratio=4 / 3)
            #     item = QListWidgetItem(self.listWidget)
            #     item.setSizeHint(thumbnail_part.sizeHint())
            #     self.listWidget.setItemWidget(item, thumbnail_part)



            print("图片组、图片组字典、所有图片数量为：", self.file_group_list, self.file_group_dict, self.all_photo_num)
            print("当前图片组名和图片数量为：", self.photonum_of_current_file, self.current_group_name)
            print("所有图片：", self.allphotoname_in_diff_group_dict)


        except NotADirectoryError:
            QMessageBox.information(self, "提示", "您的数据库地址有误！请您在左上角设置面板进行设置，如果对文件夹结构有疑问，请在帮助面板查看数据库对应文件结构或咨询实验研究人员。", QMessageBox.Ok)
            self.goto_pre_photo_btn.setEnabled(False)
            self.goto_pre_photo_btn.setText('数据库地址有误，无法开始')

        except FileNotFoundError:
            QMessageBox.information(self, "提示", "您的数据库地址未指定或结构有误！请您在实验开始前在左上角设置面板进行设置，如果对文件夹结构有疑问，请在帮助面板查看数据库对应文件结构或咨询实验研究人员。", QMessageBox.Ok)
            self.goto_pre_photo_btn.setEnabled(False)
            self.goto_pre_photo_btn.setText('数据库地址有误，无法开始')
        else:
            print("数据库加载成功！")
            self.goto_pre_photo_btn.setEnabled(True)
            self.goto_pre_photo_btn.setText('开始测评')

        #########################################   MOS设置  ##################################################
        # 当前MOS记录格式
        self.save_MOS_path = self.configure['MosRecord']['SaveUrl']
        if not os.path.exists(self.save_MOS_path):
            # 新创一个mos地址
            print("新创一个mos地址")
            now = time.localtime()
            nowt = time.strftime("%Y_%m_%d_%H_%M_%S_", now)
            path = os.path.join(os.getcwd(), nowt + 'mos.txt')
            f = open(path, 'w')
            f.close()
            self.save_MOS_path = path

        print(self.save_MOS_path)
        # #######################################   实验参数设置  ###############################################
        #
        self.dsis_time_set = {'t1': 10,
                              't2': 3,
                              't3': 10,
                              't4': 8
                              }

        self.ss_time_set = {'t1': 3, 't2': 10, 't3': 10}

        # dsis t1
        self.dsis_time_set['t1'] = self.configure["ExpParameter"]["TimeSettings"]["DSIS_T1"]
        # dsis t2
        self.dsis_time_set['t2'] = self.configure["ExpParameter"]["TimeSettings"]["DSIS_T2"]
        # dsis t3
        self.dsis_time_set['t3'] = self.configure["ExpParameter"]["TimeSettings"]["DSIS_T3"]
        # dsis t4
        self.dsis_time_set['t4'] = self.configure["ExpParameter"]["TimeSettings"]["DSIS_T4"]
        # ss t1
        self.ss_time_set['t1'] = self.configure["ExpParameter"]["TimeSettings"]["SS_T1"]
        # ss t2
        self.ss_time_set['t2'] = self.configure["ExpParameter"]["TimeSettings"]["SS_T2"]
        # ss t3
        self.ss_time_set['t3'] = self.configure["ExpParameter"]["TimeSettings"]["SS_T3"]

        #
        #  评分形式设置
        index = self.configure['ExpParameter']['MarkSettings']['CurrentShowStyle']
        if index == '0':  # 滑轮 1-5
            self.slider_mark_widget.hide()
            self.dial_mark_widget.show()
            self.show_score_dial.setMaximum(5)
            self.show_score_dial.setMinimum(1)
        elif index == '1':  # 滑轮0-100
            self.slider_mark_widget.hide()
            self.dial_mark_widget.show()
            self.show_score_dial.setMaximum(100)
            self.show_score_dial.setMinimum(0)
        elif index == '2':  # 滑块 1-5
            self.dial_mark_widget.hide()
            self.slider_mark_widget.show()
            self.horizontalSlider.setMaximum(5)
            self.horizontalSlider.setMinimum(1)
        else:  # 滑块0-100
            self.dial_mark_widget.hide()
            self.slider_mark_widget.show()
            self.horizontalSlider.setMaximum(100)
            self.horizontalSlider.setMinimum(0)

        #
        # #######################################   图片显示设置  ###############################################
        # 显示比例 目前两种 一种4：3 ， 一种16：9  index分别是0， 1
        scale_index = int(self.configure['PhotoDis']['DisplayScale']['CurrentDisScale'])
        if scale_index == 0:
            self.ratio_of_photo = 4.0 / 3
        else:
            self.ratio_of_photo = 16.0 / 9
        # # 图片大小
        if self.configure['PhotoDis']['PhotoSize']['TestSize']['CurrentPhotoSize'] == 0:
            pass
        else:
            print("采用自定义哦")
            pho_size = (self.configure['PhotoDis']['PhotoSize']['TestSize']['PhoSizeDict']['1'])
            self.show_pho_size_width = int(pho_size.split(',')[0])
            self.show_pho_size_height = int(pho_size.split(',')[1])
        # # 插值
        # self.inter_cbox.setCurrentIndex(int(self.configure['PhotoDis']['Interpolation']['CurrentInter']))

        # 屏幕  在数据库地址那里设置，因为涉及到时SS实验还是DSIS实验的问题


        # #######################################   受试者设置  ###############################################
        # testee_url = self.configure['TesteeInfo']['SaveUrl']
        # if not os.path.exists(testee_url):
        #     testee_url = os.path.join(os.getcwd(), 'testee.txt')
        #     f = open(testee_url, 'w')
        #     f.close()
        #     self.configure['TesteeInfo']['SaveUrl'] = testee_url
        #     leng = len(testee_url) * 9
        # else:
        #     testee_url =  self.configure['TesteeInfo']['SaveUrl']
        #
        # leng = len(testee_url) * 9
        # self.lineEdit_9.setFixedWidth(leng)
        # self.lineEdit_9.setText(testee_url)
        # #######################################   其他设置  ###############################################

    def get_user_MOS(self):
        if int(self.configure['ExpParameter']['MarkSettings']['CurrentShowStyle']) < 2:  # 滑轮
            # 显示MOS值
            MOS = int(self.show_score_dial.value())
            self.show_score_lcd.display(MOS)
        else:  # 滑块
            MOS = int(self.horizontalSlider.value())
            self.show_score_lcd_2.display(MOS)

    def second_showpane_show(self):
        if self.GT_pho_pane.isHidden():
            self.GT_pho_pane.show()
        else:
            self.GT_pho_pane.hide()

    def ensure_this_MOS(self):

        if self.is_continue is True: # 防止一开始点击ensure btn会导致定时出错

            self.control_timer.stop()
            self.timerflag = 0

            # self.ensure_score_of_this_picture_btn.setEnabled(False)
            # self.ensure_score_of_this_picture_btn.setText("您已确认，请点击下一张")

            # 设置写入某个txt中
            MOS = self.show_score_lcd.value()

            # count = len(open(self.mos_path, 'rU').readlines()) #计算文本行数
            # print(count)

            fp = open(self.save_MOS_path, mode="a")  # a会在最后一行追加
            if self.configure['MosRecord']['Style']['CurrentStyle'] == '0':
                fp.write(str(self.current_photo_path) + ', ' + str(MOS) + '\n')
            else:
                now = time.localtime()
                nowt = time.strftime("%Y-%m-%d-%H:%M:%S", now)
                fp.write(str(nowt + ', ' + self.current_photo_path) + ', ' + str(MOS) + '\n')
            fp.close()

            # 进度调整
            self.all_progress_num += 1
            progress_ratio = int(self.all_progress_num / self.all_photo_num * 100)
            # print(progress_ratio)
            self.progressBar.setValue(progress_ratio)

            self.current_progress_num += 1
            progress_ratio = int(self.current_progress_num / self.photonum_of_current_file * 100)
            # print(progress_ratio)
            self.progressBar_2.setValue(progress_ratio)

            # 如果是PEID的预备时刻
            if self.dis_mode == 4 and self.peid_sort_time == False:

                # 缩略图面板根据MOS 从高到低往里面插入

                # num = self.listWidget.count()

                # 图片名和分数信息  统一划归到5分制 好排序
                # info = "图片名: " + self.current_photo + ' \n' + "得分: " + str(MOS)
                if self.configure['ExpParameter']['MarkSettings']['CurrentShowStyle'] == '1' or \
                        self.configure['ExpParameter']['MarkSettings']['CurrentShowStyle'] == '3':
                    MOS = MOS / 20.0

                info = str(MOS) + '( 统一划归到5分 )' + '\n \n' + self.current_photo

                # 设置一下缩略图
                this_item = QListWidgetItem()
                icon = QIcon()
                icon.addPixmap(QPixmap(self.current_photo_path).scaled(144, 108), QtGui.QIcon.Normal,
                                QtGui.QIcon.Off)

                this_item.setIcon(icon)
                this_item.setText(info)

                # 添加并排序
                self.listWidget.addItem(this_item)
                self.listWidget.sortItems(order=Qt.DescendingOrder)


            # 换下一张幻灯片
            self.go_to_next_photo()

    def ensure_this_sort(self):
        print("成功sort")

        #关掉定时器
        self.control_timer.stop()

        # 记录一下排序
        num = self.listWidget.count()
        fp = open(self.save_MOS_path, mode="a")  # a会在最后一行追加
        fp.write(str('——————————————      上面是评分，下面是排序     ————————————' + '\n'))
        if self.configure['MosRecord']['Style']['CurrentStyle'] == '0':
            nowt = ''
        else:
            now = time.localtime()
            nowt = time.strftime("%Y-%m-%d-%H:%M:%S", now)

        for i in range(num):
            pho = self.listWidget.item(i).text().split('\n')[-1]
            path = os.path.join(self.database_path, self.current_group_name, pho).replace('\\', '/')
            fp.write(str(nowt + ', ' + path + ', 排序：' + str(i+1) + '\n'))
        fp.write(str('*************************************************************************************************' + '\n'))

        fp.close()

        # 清空缩略图
        self.listWidget.clear()

        # flag 置True
        # 最后一个数据不能变sort 要在next做判断，防止最后一个数据没有排序

        self.peid_sort_time = False
        self.is_peid_warmup = True

        # 当前warmup照片置0
        self.curr_warmup_pho_num = 0

        #flag清零
        self.timerflag = 0

        # print("我设置了缩略图灰度")
        self.Thumbnail_pic_lb.setPixmap(QPixmap(""))
        self.show_pic_lb.setPixmap(QPixmap(""))

        print("1111111111111111", self.progressBar.value())

        if not self.progressBar.value() == 100:
            # 重新获取照片列表和当前照片
            del self.allphotoname_in_diff_group_dict[self.file_group_list[0]]
            del self.file_group_list[0]
            self.current_photo_list = list(self.allphotoname_in_diff_group_dict[self.file_group_list[0]])

            # 删除之前的文件组字典值， 重新获取当前的文件组名和文件数
            del self.file_group_dict[self.current_group_name]
            self.current_group_name = self.file_group_list[0]
            self.photonum_of_current_file = int(self.file_group_dict[self.current_group_name])




            # 返回原来的面板和对应比例
            self.tool_widget.setCurrentIndex(0)
            self.dis_tabWidget.setCurrentIndex(0)

            # 设置一下主面板和缩略图的比例
            self.central_layout.setStretchFactor(self.dis_tabWidget, 7)
            self.central_layout.setStretchFactor(self.tool_widget, 3)

            print("@@@@@@@@@", self.allphotoname_in_diff_group_dict)
            print("@@@@@@@@@@@@@@@", self.file_group_list[0])

            # 重开定时器
            self.control_timer.start(self.time_gap)

        else:
            self.end_time = True
            self.go_to_next_photo()


        # self.main_display()




    # 实际上是开始按钮  评测开始！！！！！！！！！
    def go_to_pre_photo(self):

        # print("!!!!!!!!!!!!!!!!!!!!!!!!我在pre里面")

        try:
            # 指示实验正在进行
            self.is_continue = True

            self.goto_pre_photo_btn.setEnabled(False)
            self.goto_pre_photo_btn.setText("正在评测~")
            if self.dis_mode == 1 or self.dis_mode == 2:
                self.ensure_score_of_this_picture_btn.setEnabled(False)

            # 打开定时器 每1s进行一次监听，更新面板和缩略图，以及剩余时间
            self.control_timer.start(self.time_gap)

            if self.is_peid_warmup:
                # 弹出当前的图片，并读取当前的图片路径
                self.current_photo = self.current_photo_list[0]
                self.current_photo_path = os.path.join(self.database_path_test,
                                                       self.current_group_name,
                                                       self.current_photo)
                # 为了适应pyqt5，必须把地址中的 \ 变为 /
                self.current_photo_path = str(self.current_photo_path).replace('\\', "/")
                # print("当前照片路径是", self.current_photo_path)

            if not (self.is_peid_warmup and self.dis_mode == 4):
                # 根据图片长宽比来调整label的尺寸
                self.main_display()

                # 在lb上显示当前照片
                self.label_11.setText("当前照片为：" + str(self.current_photo))

        except AttributeError:
            QMessageBox.information(self, "提示", "您未指定数据库地址！请您在左上角设置面板进行设置，如果对文件夹结构有疑问，请在帮助面板查看数据库对应文件结构或咨询实验研究人员。", QMessageBox.Ok)





    def go_to_next_photo(self):
        # 打开定时器 每1s进行一次监听，更新面板和缩略图，以及剩余时间
        if not self.end_time:
            self.control_timer.start(self.time_gap)

        # print("下一张")
        # print(self.current_group_name)
        # print(self.display_widget.height())
        # print(self.desktop_width, self.desktop_height)

        # 总进度条满了
        if self.progressBar.value() == 100 and self.configure['PhotoDis']['DisForDSIS']['CurrentStyle'] != '4':

            self.finish_mess_box = QMessageBox.information(self,
                                                           "测试完成提示框",
                                                           "您的测试已完成！感谢您的参与！请按""Yes""键关闭测试窗口",
                                                           QMessageBox.Yes)
            self.close()

        else:
            if self.end_time and self.configure['PhotoDis']['DisForDSIS']['CurrentStyle'] == '4':
                self.finish_mess_box = QMessageBox.information(self,
                                                               "测试完成提示框",
                                                               "您的测试已完成！感谢您的参与！请按""Yes""键关闭测试窗口",
                                                               QMessageBox.Yes)
                self.close()

            else:

                # 还原确认键
                # self.ensure_score_of_this_picture_btn.setEnabled(True)
                # self.ensure_score_of_this_picture_btn.setText("确认")

                # 如果组内的进度条满了，就换一下组、重置进度条， 进度数，重新展示照片， 接着继续测试
                # 但是需要判断是不是要进行peid数据库的排序
                if self.progressBar_2.value() == 100:

                    # 重置进度条和进度数
                    self.progressBar_2.setValue(0)
                    self.current_progress_num = 0

                    # PEID数据库模式， 进行排序  flag 置True
                    if self.configure['PhotoDis']['DisForDSIS']['CurrentStyle'] == '4':
                        self.peid_sort_time = True

                    if not self.peid_sort_time:
                        # 如果不需要进行peid数据库的排序 那么就继续下一个列表


                        # 重新获取照片列表和当前照片
                        del self.allphotoname_in_diff_group_dict[self.file_group_list[0]]
                        del self.file_group_list[0]
                        self.current_photo_list = list(self.allphotoname_in_diff_group_dict[self.file_group_list[0]])

                        # 删除之前的文件组字典值， 重新获取当前的文件组名和文件数
                        del self.file_group_dict[self.current_group_name]
                        self.current_group_name = self.file_group_list[0]
                        self.photonum_of_current_file = int(self.file_group_dict[self.current_group_name])

                        self.main_display()
                        # print(self.current_group_name, self.photonum_of_current_file)
                        # print(self.file_group_dict, self.file_group_list)

                    else:
                        # 否则就开始peid 缩略图排序阶段

                        # 开始切换到 缩略图面板
                        self.tool_widget.setCurrentIndex(1)

                        # 切换到左右显示的面板  左右显示
                        self.dis_tabWidget.setCurrentIndex(1)

                        # 设置一下主面板和缩略图的比例
                        self.central_layout.setStretchFactor(self.dis_tabWidget, 1)
                        self.central_layout.setStretchFactor(self.tool_widget, 0)



                else:
                    self.main_display()

    def timer_handle(self):
        self.timerflag += 1
        # print("Timerflag = ",self.timerflag)

        # 如果要进行预热实验
        if self.is_peid_warmup == True and self.dis_mode == 4:
            # print("%%%%%%%%%%%%%%%%%weishane     ", self.current_photo_list)
            # print("%%%%%%%%%%%%%%%%第几张图", self.curr_warmup_pho_num)
            self.ensure_score_of_this_picture_btn.setEnabled(False)
            self.ensure_score_of_this_picture_btn.setText("现在是实验预热阶段~ 无需进行评价")
            self.label_11.setText("")


            # print(self.timerflag)
            if len(self.current_photo_list) == self.curr_warmup_pho_num :
                self.is_peid_warmup = False
                # self.refresh_settings()
                self.timerflag = 0
                self.control_timer.stop()


                self.go_to_pre_photo()

                # 开始切换到 主面板
                self.tool_widget.setCurrentIndex(0)



                # 切换到左右显示的面板  左右显示
                self.dis_tabWidget.setCurrentIndex(0)

                self.ensure_score_of_this_picture_btn.setEnabled(True)
                self.ensure_score_of_this_picture_btn.setText("确认评分")

                self.curr_warmup_pho_num = 0

            if self.timerflag == 1:
                pho = self.current_photo_list[self.curr_warmup_pho_num]
                self.curr_warmup_pho_num +=1

                if self.configure['PhotoDis']['PhotoSize']['TestSize']['CurrentPhotoSize'] == 0 or (
                        self.show_pho_size_width > self.display_widget.width() * 0.85 or self.show_pho_size_width < 10):
                    self.show_pho_size_width = self.display_widget.width() * 0.85
                    self.show_pho_size_height = self.display_widget.height() * 0.85
                else:
                    pass

                path = os.path.join(self.database_path, self.current_group_name, pho)
                # 根据图片长宽比来调整label的尺寸
                img = QImage(path)
                # transform = QTransform()
                # transform.rotate(90)
                # img = img.transformed(transform)
                # print("当前手机的尺寸", img.height(), img.width(), self.current_photo_path)
                if img.height() > img.width():
                    # 设置4：3尺寸，如果宽高比是3：4 那么吧label也变一下再展示
                    self.show_pic_lb.setFixedSize(self.show_pho_size_height / self.ratio_of_photo,
                                                  self.show_pho_size_height)

                    jpg = QtGui.QPixmap(path).scaled(self.show_pic_lb.width(),
                                                                        self.show_pic_lb.height())
                    self.show_pic_lb.setPixmap(jpg)
                else:

                    self.show_pic_lb.setFixedSize(self.show_pho_size_width,
                                                  self.show_pho_size_width / self.ratio_of_photo)

                    jpg = QtGui.QPixmap(path).scaled(self.show_pic_lb.width(),
                                                                        self.show_pic_lb.height())
                    self.show_pic_lb.setPixmap(jpg)

            if self.timerflag ==6:
                self.show_pic_lb.setPixmap(QPixmap(""))
                self.show_pic_lb.setStyleSheet("background-color:#808080")


            if self.timerflag == 8:
                self.control_timer.stop()
                self.timerflag = 0
                self.control_timer.start(self.time_gap)


        # 否则就正常流程
        else:
            if self.timerflag % 2 == 0:
            # 1s检测一次
                if self.peid_sort_time == False:
                # 如果不是peid时刻
                    if self.dis_mode == 0 or self.dis_mode == 3 or self.dis_mode == 4:
                        cycle_time = int(self.ss_time_set['t1']) + int(self.ss_time_set['t2']) + int(self.ss_time_set['t3'])
                    else:
                        cycle_time = int(self.dsis_time_set['t1']) + int(self.dsis_time_set['t2']) + int(
                            self.dsis_time_set['t3']) + int(self.dsis_time_set['t4'])

                    cycle_time = cycle_time * 1000 / self.time_gap
                    self.goto_next_photo_btn.setText("剩余评分时间： " + str((cycle_time - self.timerflag) / 2) + " s")
                else:
                # peid时刻就在缩略图面板显示时间
                    cycle_time = 30 * 1000 / self.time_gap
                    self.lineEdit.setText( str((cycle_time - self.timerflag) / 2) + " s")

            # 判断是SS还是DSIS还是PEID数据库
            # SSqueren
            ##############################################################################
            # t1，t3时间灰度，t2时间显示图片
            ##############################################################################
            if self.configure['PhotoDis']['DisForDSIS']['CurrentStyle'] == '0' or \
                    self.configure['PhotoDis']['DisForDSIS']['CurrentStyle'] == '3' or \
                    (self.configure['PhotoDis']['DisForDSIS']['CurrentStyle'] == '4' and self.peid_sort_time == False): #SS 和PEID非排序阶段
                # t1和t3算在一起！！！

                # 如果到了演示时间10s，
                # 1.那么就打开提示框，
                # 2.进入中灰度模式
                if self.timerflag == int(self.ss_time_set['t2'])*1000/self.time_gap:  #gap=500ms刷新一次  因此要/1000×gap
                    QMessageBox.warning(self,
                                        "评分开始",
                                        "请您在右下角时间内完成评分！否则此次评分无效,系统将自动跳转至下一张图片",
                                        QMessageBox.Yes)
                    ########################################################################################################################

                    self.show_pic_lb.setPixmap(QPixmap(""))
                    self.show_pic_lb.setStyleSheet("background-color:#808080")

                # 一个测试周期结束了
                # 1.flag清零，关掉定时器，
                # 2.完成相应记录操作，
                # 3.再重新开启定时器，
                # 4.进入下一个测试周期
                elif self.timerflag == (int(self.ss_time_set['t1']) + int(self.ss_time_set['t2']) + int(self.ss_time_set['t3']) )*1000/self.time_gap:

                    self.timerflag = 0
                    self.control_timer.stop()
                    self.ensure_this_MOS()

                # 演示时间t2s内，幻灯片正常一轮时间内， 1.两个都展示
                elif (self.timerflag <= 3 * self.photonum_of_current_file) and (self.timerflag < int(self.ss_time_set['t2'])*1000/self.time_gap):
                    #3的意思是幻灯片播放一秒，中灰度常0.5s，刷新率为0.5s，故一周期为1.5s=3*gap
                    # print("此处缩略图需要gap数为：", 3*self.photonum_of_current_file)
                    is_ppt_show_num = int(self.timerflag / 3)
                    is_ppt_close_num = self.timerflag % 3
                    self.ppt_of_current_group(is_ppt_show_num, is_ppt_close_num)


                # # 演示时间10s内，幻灯片正常一轮时间外， 1.只展示主界面  2.屏蔽缩略图
                # elif self.timerflag > 3*self.photonum_of_current_file and self.timerflag < 20:
                #
                #     self.Thumbnail_pic_lb.setPixmap(QPixmap(""))
                #     self.Thumbnail_pic_lb.setStyleSheet("background-color:#808080")

                else:
                    if self.dis_mode == 0:
                        self.Thumbnail_pic_lb.setPixmap(QPixmap(""))
                        self.Thumbnail_pic_lb.setStyleSheet("background-color:#808080")
                    if self.dis_mode == 3:
                        self.GT_pho_pane.dis_lb.setPixmap(QPixmap(""))
                        self.GT_pho_pane.dis_lb.setStyleSheet("background-color:#808080")

            # DSIS
            ##############################################################################
            # t1时间显示失真图片，t2灰度场，t3同时显示失真和原始照片，t4同时灰度（唯一评测时间）
            ##############################################################################
            elif self.configure['PhotoDis']['DisForDSIS']['CurrentStyle'] == '1' or \
                    self.configure['PhotoDis']['DisForDSIS']['CurrentStyle'] == '2':
                #设置DSIS显示面板
                if self.dis_mode == 1:
                    distort_pane = self.show_pic_lb_2
                    real_pane = self.show_pic_lb_4
                else:
                    distort_pane = self.show_pic_lb_3
                    real_pane = self.show_pic_lb_5


                # 如果失真照片演示时间结束了，
                # 2.进入中灰度模式
                if self.timerflag == int(self.dsis_time_set['t1']) * 1000 / self.time_gap:  # gap=500ms刷新一次  因此要/1000×gap
                    distort_pane.setPixmap(QPixmap(""))
                    distort_pane.setStyleSheet("background-color:#808080")


                # 演示时间t3s内.两个都展示
                elif self.timerflag == ( int(self.dsis_time_set['t1']) + int(self.dsis_time_set['t2']) ) *1000 / self.time_gap:

                    self.main_display(is_next=0)
                    self.ppt_of_current_group(show_pic_num = None, is_show_or_close=1)

                # 评分时间到了
                elif self.timerflag == ( int(self.dsis_time_set['t1']) + int(self.dsis_time_set['t2']) + int(self.dsis_time_set['t3']) ) * 1000 / self.time_gap:
                    self.ensure_score_of_this_picture_btn.setEnabled(True)
                    distort_pane.setPixmap(QPixmap(""))
                    distort_pane.setStyleSheet("background-color:#808080")
                    self.ppt_of_current_group(show_pic_num=None, is_show_or_close=0)

                # 一个测试周期结束了
                # 1.flag清零，关掉定时器，
                # 2.完成相应记录操作，
                # 3.再重新开启定时器，
                # 4.进入下一个测试周期
                elif self.timerflag == ( int(self.dsis_time_set['t1']) + int(self.dsis_time_set['t2']) + int(self.dsis_time_set['t3']) + int(self.dsis_time_set['t4']) ) * 1000 / self.time_gap:
                    self.timerflag = 0
                    self.control_timer.stop()
                    self.ensure_this_MOS()
                    self.ensure_score_of_this_picture_btn.setEnabled(False)
                else:
                    pass

            else:
                # PEID数据库排序阶段  如果到了30s那么就自动结束这个排序，否则就啥也不做
                if self.timerflag == 60:
                    self.ensure_this_sort()
                else:
                    pass




    def main_display(self, is_next=1, special_path=None):
        # print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!我进入mainshow了")
        if is_next == 0:
            pass
        else:
            # 弹出照片，在面板上显示图片
            self.current_photo = self.current_photo_list.pop(0)
            # print("*********", self.current_photo_list)
            self.current_photo_path = os.path.join(self.database_path_test,
                                                   self.current_group_name,
                                                   self.current_photo)
            # 为了适应pyqt5，必须把地址中的 \ 变为 /
            self.current_photo_path = str(self.current_photo_path).replace('\\', "/")
            # print("当前照片路径是", self.current_photo_path)

        # ！！！判断是SS还是DSIS，DSIS分为两种
        #  1.SS:
        if self.dis_mode == 0 or self.dis_mode == 3 or (self.dis_mode == 4 and self.peid_sort_time == False):
            # 判断一下自定义的图片大小，对于自适应和图片太大或者太小的进行默认设置，防止系统崩溃
            if self.configure['PhotoDis']['PhotoSize']['TestSize']['CurrentPhotoSize'] == 0 or (
                    self.show_pho_size_width > self.display_widget.width()*0.85 or self.show_pho_size_width < 10):
                self.show_pho_size_width = self.display_widget.width()*0.85
                self.show_pho_size_height = self.display_widget.height()*0.85
            else:
                pass

            # 根据图片长宽比来调整label的尺寸
            img = QImage(self.current_photo_path)
            # transform = QTransform()
            # transform.rotate(90)
            # img = img.transformed(transform)
            # print("当前手机的尺寸", img.height(), img.width(), self.current_photo_path)
            if img.height() > img.width():
                # 设置4：3尺寸，如果宽高比是3：4 那么吧label也变一下再展示
                self.show_pic_lb.setFixedSize(self.show_pho_size_height / self.ratio_of_photo,
                                              self.show_pho_size_height)

                jpg = QtGui.QPixmap(self.current_photo_path).scaled(self.show_pic_lb.width(),
                                                                    self.show_pic_lb.height())
                self.show_pic_lb.setPixmap(jpg)
            else:

                self.show_pic_lb.setFixedSize(self.show_pho_size_width,
                                              self.show_pho_size_width / self.ratio_of_photo)

                jpg = QtGui.QPixmap(self.current_photo_path).scaled(self.show_pic_lb.width(),
                                                                    self.show_pic_lb.height())
                self.show_pic_lb.setPixmap(jpg)
        #  2.DSIS 左右
        elif self.dis_mode == 1:
            # 判断一下自定义的图片大小，对于自适应和图片太大或者太小的进行默认设置，防止系统崩溃
            if self.configure['PhotoDis']['PhotoSize']['TestSize']['CurrentPhotoSize'] == 0 or (
                    self.show_pho_size_width > self.display_widget_lr.width() * 0.45 or self.show_pho_size_width < 10):
                self.show_pho_size_width = self.display_widget_lr.width() * 0.47
                self.show_pho_size_height = self.display_widget_lr.height() * 0.90
            else:
                pass

            # 根据图片长宽比来调整label的尺寸
            img = QImage(self.current_photo_path)
            if img.height() > img.width():
                # 设置4：3尺寸，如果宽高比是3：4 那么吧label也变一下再展示
                self.show_pic_lb_2.setFixedSize(self.show_pho_size_height / self.ratio_of_photo,
                                              self.show_pho_size_height)

                jpg = QtGui.QPixmap(self.current_photo_path).scaled(self.show_pic_lb_2.width(),
                                                                    self.show_pic_lb_2.height())
                self.show_pic_lb_2.setPixmap(jpg)
            else:

                self.show_pic_lb_2.setFixedSize(self.show_pho_size_width,
                                              self.show_pho_size_width / self.ratio_of_photo)

                jpg = QtGui.QPixmap(self.current_photo_path).scaled(self.show_pic_lb_2.width(),
                                                                    self.show_pic_lb_2.height())
                self.show_pic_lb_2.setPixmap(jpg)
        #  3.DSIS 上下
        elif self.dis_mode == 2:
            # 判断一下自定义的图片大小，对于自适应和图片太大或者太小的进行默认设置，防止系统崩溃
            if self.configure['PhotoDis']['PhotoSize']['TestSize']['CurrentPhotoSize'] == 0 or (
                    self.show_pho_size_width > self.display_widget_ud.width() * 0.45 or self.show_pho_size_width < 10):
                self.show_pho_size_width = self.display_widget_ud.width() * 0.90
                self.show_pho_size_height = self.display_widget_ud.height() * 0.48
            else:
                pass

            # 根据图片长宽比来调整label的尺寸
            img = QImage(self.current_photo_path)
            if img.height() > img.width():
                # 设置4：3尺寸，如果宽高比是3：4 那么吧label也变一下再展示
                self.show_pic_lb_3.setFixedSize(self.show_pho_size_height / self.ratio_of_photo,
                                                self.show_pho_size_height)

                jpg = QtGui.QPixmap(self.current_photo_path).scaled(self.show_pic_lb_3.width(),
                                                                    self.show_pic_lb_3.height())
                self.show_pic_lb_3.setPixmap(jpg)
            else:

                self.show_pic_lb_3.setFixedSize(self.show_pho_size_height * self.ratio_of_photo,
                                                self.show_pho_size_height)

                jpg = QtGui.QPixmap(self.current_photo_path).scaled(self.show_pic_lb_3.width(),
                                                                    self.show_pic_lb_3.height())
                self.show_pic_lb_3.setPixmap(jpg)
        else:
            if self.thumbnail_show_where == 'left':
                show_pane = self.show_pic_lb_2
            else:
                show_pane = self.show_pic_lb_4

            # 判断一下自定义的图片大小，对于自适应和图片太大或者太小的进行默认设置，防止系统崩溃
            if self.configure['PhotoDis']['PhotoSize']['TestSize']['CurrentPhotoSize'] == 0 or (
                    self.show_pho_size_width > self.display_widget_lr.width() * 0.45 or self.show_pho_size_width < 10):
                self.show_pho_size_width = self.display_widget_lr.width() * 0.47
                self.show_pho_size_height = self.display_widget_lr.height() * 0.90
            else:
                pass

            # 根据图片长宽比来调整label的尺寸
            img = QImage(special_path)
            if img.height() > img.width():
                # 设置4：3尺寸，如果宽高比是3：4 那么吧label也变一下再展示
                show_pane.setFixedSize(self.show_pho_size_height / self.ratio_of_photo,
                                                self.show_pho_size_height)

                jpg = QtGui.QPixmap(special_path).scaled(show_pane.width(),
                                                                    show_pane.height())
                show_pane.setPixmap(jpg)
            else:

                show_pane.setFixedSize(self.show_pho_size_width,
                                                self.show_pho_size_width / self.ratio_of_photo)

                jpg = QtGui.QPixmap(special_path).scaled(show_pane.width(),
                                                                    show_pane.height())
                show_pane.setPixmap(jpg)

        if not (self.dis_mode == 4 and self.peid_sort_time == True):
            # 在lb上显示当前照片名字
            self.label_11.setText("当前照片为：" + str(self.current_photo))

    def ppt_of_current_group(self, show_pic_num, is_show_or_close):
        # 暂时只做ss实验 mode 0  缩略图   mode 3 双屏
        # 513 加一下DSIS实验  mode 1 左右   mode 2 上下
        if self.dis_mode == 0 or self.dis_mode == 4: # ss 缩略图
            current_ppt_pane = self.Thumbnail_pic_lb
            # 灰度场时间
            if is_show_or_close == 0:
                current_ppt_pane.setPixmap(QPixmap(""))
                current_ppt_pane.setStyleSheet("background-color:#808080")

            # 演示场时间
            else:
                # 在缩略图上显示图片
                ppt_photo = self.allphotoname_in_diff_group_dict[str(self.current_group_name)][show_pic_num]
                ppt_photo_path = os.path.join(self.database_path_test,
                                              self.current_group_name,
                                              ppt_photo)
                # 为了适应pyqt5，必须把地址中的 \ 变为 /
                ppt_photo_path = str(ppt_photo_path).replace('\\', "/")
                # print("当前照片路径是", ppt_photo_path)

                # 根据图片长宽比来调整label的尺寸
                img = QImage(ppt_photo_path)
                if img.height() > img.width():
                    # 设置4：3尺寸，如果宽高比是3：4 那么吧label也变一下再展示
                    current_ppt_pane.setFixedSize((self.display_widget.height() / 3 * 0.85) / self.ratio_of_photo,
                                                  self.display_widget.height() / 3 * 0.85)
                else:
                    current_ppt_pane.setFixedSize(self.display_widget.width() / 3 * 0.85,
                                                  (self.display_widget.width() / 3 * 0.85) / self.ratio_of_photo)
                jpg = QtGui.QPixmap(ppt_photo_path).scaled(current_ppt_pane.width(),
                                                               current_ppt_pane.height())
                current_ppt_pane.setPixmap(jpg)

        elif self.dis_mode == 3:
            current_ppt_pane = self.GT_pho_pane.dis_lb
            # 灰度场时间
            if is_show_or_close == 0:
                current_ppt_pane.setPixmap(QPixmap(""))
                current_ppt_pane.setStyleSheet("background-color:#808080")

            # 演示场时间
            else:
                # 在缩略图上显示图片
                ppt_photo = self.allphotoname_in_diff_group_dict[str(self.current_group_name)][show_pic_num]
                ppt_photo_path = os.path.join(self.database_path_test,
                                              self.current_group_name,
                                              ppt_photo)
                # 为了适应pyqt5，必须把地址中的 \ 变为 /
                ppt_photo_path = str(ppt_photo_path).replace('\\', "/")
                # print("当前照片路径是", ppt_photo_path)

                # 根据图片长宽比来调整label的尺寸
                img = QImage(ppt_photo_path)
                if img.height() > img.width():
                    # 设置4：3尺寸，如果宽高比是3：4 那么吧label也变一下再展示
                    current_ppt_pane.setFixedSize(self.show_pic_lb.height() / self.ratio_of_photo,
                                                  self.show_pic_lb.height() )
                else:
                    current_ppt_pane.setFixedSize(self.show_pic_lb.width() ,
                                                  self.show_pic_lb.width() / self.ratio_of_photo )
                jpg = QtGui.QPixmap(ppt_photo_path).scaled(current_ppt_pane.width(),
                                                           current_ppt_pane.height())
                current_ppt_pane.setPixmap(jpg)

        else:
            if self.dis_mode == 1:
                current_ppt_pane = self.show_pic_lb_4
                distort_pane = self.show_pic_lb_2
            else:
                current_ppt_pane = self.show_pic_lb_5
                distort_pane = self.show_pic_lb_3
            # 灰度场时间
            if is_show_or_close == 0:
                current_ppt_pane.setPixmap(QPixmap(""))
                current_ppt_pane.setStyleSheet("background-color:#808080")

            # 演示场时间
            else:
                #在右边显示图片
                ppt_photo_path = ''
                for pho in os.listdir(self.database_path_real):
                    name, _ = os.path.splitext(pho)
                    if name == self.current_group_name:
                        ppt_photo_path = os.path.join(self.database_path_real, pho)
                        break

                # 设置参考和测试图片两个大小相同
                current_ppt_pane.setFixedSize(distort_pane.height() / self.ratio_of_photo,
                                                  distort_pane.height())

                jpg = QtGui.QPixmap(ppt_photo_path).scaled(current_ppt_pane.width(),
                                                           current_ppt_pane.height())
                current_ppt_pane.setPixmap(jpg)



    def hide_tool(self):
        if not self.tool_widget.isHidden():
            self.tool_widget.hide()
        else:
            self.tool_widget.show()




if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    window = MainExpProPane()
    # window.exit_signal.connect(lambda :print("退出"))
    # window.register_account_pwd_signal.connect(lambda a, p: print(a, p))
    window.show()

    sys.exit(app.exec_())
