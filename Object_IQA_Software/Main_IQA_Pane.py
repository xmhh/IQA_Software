from PyQt5.Qt import *
from PyQt5 import QtGui
from Object_IQA_Software.resource.main_iqa_ui import Ui_MainWindow   #记得改！！！！！！！！！！！！！！！！
# from Object_IQA_Software.Batch_NR_Pane import BatchNRPane
from Object_IQA_Software.method.NR_IQA_method.NR_IQA_algorithm import *
from Object_IQA_Software.method.FR_IQA_method.FR_IQA_algorithm import FR_IQA_method
# from Mymatlabexe.method.Ours import *
import numpy as np
import matlab.engine



class MainIQAPane(QMainWindow, Ui_MainWindow):

    start_a_batch_nr_pane_signal = pyqtSignal(str)
    # nr_iqa_algorithm_signal = pyqtSignal(str, str)

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        #打开背景图片的设置
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)

        # 默认隐藏第二个照片lb，默认评价tab是NR_IQA
        self.img_show_lb_2.hide()
        self.tool_widget.setCurrentWidget(self.NR_IQA_tab)


        # 初始化参数：默认选图片的地址、图片地址
        self.init_open_addr = r'C:\Users'
        self.nr_iqa_pho_addr = None
        self.fr_iqa_pho_addr_1 = None
        self.fr_iqa_pho_addr_2 = None

        # 定义两类算法，并写入combobox
        nr_algorithm_list = ['BIQI', 'BRISQUE', 'NIQE', 'BLIINDS_2', 'DESIQUE', 'CPBD',
                          'FISH', 'FISH_bb', 'S3', 'LPC', 'DIIVINE', 'Martziliano', 'NJQA']
        self.algorithm_comboBox.addItems(nr_algorithm_list)
        fr_algorithm_list = ['MSE', 'RMSE', 'PSNR', 'SSIM', 'UQI', 'MS-SSIM', 'ERGAS', 'SCC', 'RASE', 'SAM', 'VIF_P']
        self.fr_algorithm_comboBox.addItems(fr_algorithm_list)

        # 图片显示比例ratio_of_photo， 缩放比例数组,pho_show_scale_single _double分别是单张照片和多照片
        self.ratio_of_photo = 4/3
        self.pho_show_scale_single = np.round((np.arange(0.50, 0.76, 0.02)), 2).tolist()
        self.pho_show_scale_double = np.round((np.arange(0.33, 0.47, 0.01)), 2).tolist()
        self.curr_phot_show_scale = [0.70, 0.40]  # 分别代表单照片和两张照片的默认尺寸

        self.current_photo_info = []

        # self.isclear_figure = False
        self.isfist_readimg = True
        # 是否隐藏工具栏
        self.ishidden_tool_wid = False

        # 初始化一个matlab engine
        self.eng = matlab.engine.start_matlab()

        # 初始化一个评分线程
        self.nr_iqa_thread = My_NR_IQA_Thread()
        self.nr_iqa_thread.score_signal.connect(self.nr_iqa_score_callback)

        self.fr_iqa_thread = My_FR_IQA_Thread()
        self.fr_iqa_thread.fr_score_signal.connect(self.fr_iqa_score_callback)

        # 从定义一下右键菜单，用作图片的缩放
        self.img_show_lb.setContextMenuPolicy(Qt.CustomContextMenu)
        self.img_show_lb.customContextMenuRequested.connect(self.quick_change_pho_by_mouse)

        # 定义批处理信号
        self.file_menu.triggered[QAction].connect(self.change_setting_of_file)

        self.is_batch_active = False

    # 定义批处理槽函数
    def change_setting_of_file(self, action_name):
        action_name = str(action_name.text())
        self.start_a_batch_nr_pane_signal.emit(action_name)
        # if action_name in ['BIQI', 'BRISQUE', 'NIQE', 'BLIINDS_2', 'CPBD', 'NJQA']:
        #     if self.batch_nr_pane == 1:
        #         #1 代表目前没有任务
        #         self.batch_nr_pane = BatchNRPane(action_name)
        #         self.batch_nr_pane.show()


    # NR_IQA相关槽函数和线程
    def nr_iqa_score_callback(self, i):
        self.real_mark_lb.setText(i)
        # 重新使能开始评价并改字
        self.start_mark_btn.setEnabled(True)
        self.start_mark_btn.setText('开始评价')



    def choose_pho_from_pc(self):

        save_path_tuple = QFileDialog.getOpenFileNames(self,
                                                       "请选择一张您想要做NR_IQA的图片",
                                                       self.init_open_addr,
                                                       "JPG Files (*.jpg);;PNG Files (*.png);;BMP Files (*.bmp)")
                                                        # 最好还是别用 all file   "All Files (*);;JPG Files (*.jpg);;PNG Files (*.png);;BMP Files (*.bmp)"

        # 防止用户退出，没有选文件，故需判断tuple第一个元素，即文件地址是否为空
        if save_path_tuple[0] == []:
            pass
        else:
            # 更新地址显示文本框
            self.nr_iqa_pho_addr = save_path_tuple[0][0]
            print(self.nr_iqa_pho_addr)
            self.refresh_curr_pho_info(is_from_choose=True, pho_num=0)

            # 更新主显示界面和状态栏
            self.show_nr_iqa_photo()

    def pho_zoom_in(self):
        # nr照片放大
        if self.pho_addr_show_le.text() != '':
            next_index = self.pho_show_scale_single.index(self.curr_phot_show_scale[0])
            print(next_index)
            if self.pho_show_scale_single[next_index] == self.pho_show_scale_single[-1]:
                pass
                print('到顶了')
            else:
                next_index += 1
                self.curr_phot_show_scale[0] = self.pho_show_scale_single[next_index]
                self.show_nr_iqa_photo(curr_scale=self.curr_phot_show_scale)

    def pho_zoom_out(self):
        # nr照片缩小
        if self.pho_addr_show_le.text() != '':

            pre_index = self.pho_show_scale_single.index(self.curr_phot_show_scale[0])
            print(pre_index)
            if self.pho_show_scale_single[pre_index] == self.pho_show_scale_single[0]:
                pass
                print('到底了')
            else:
                pre_index -= 1
                self.curr_phot_show_scale[0] = self.pho_show_scale_single[pre_index]
                self.show_nr_iqa_photo(curr_scale=self.curr_phot_show_scale)

    def pho_zoom_reset(self):

        if  self.pho_addr_show_le.text() != '':
            # 更新当前图片信息 、statusbar、更新面板
            self.refresh_curr_pho_info(is_from_choose=False, pho_num=0)
            self.curr_phot_show_scale = [0.7, 0.4]
            self.show_nr_iqa_photo()

    def start_mark(self):

        if self.pho_addr_show_le.text() != '':
            # 获取当前的算法和图片地址
            algorithm = self.algorithm_comboBox.currentText()
            photo_addr = self.pho_addr_show_le.text()
            print(algorithm, photo_addr)

            # 取消使能 开始评价按键  并提示”正在运行“
            self.start_mark_btn.setEnabled(False)
            self.start_mark_btn.setText('正在评价')

            # 开启线程并运行
            self.nr_iqa_thread.setting(algorithm, photo_addr, eng=self.eng)
            self.nr_iqa_thread.start()
            # self.nr_iqa_algorithm_signal.emit(algorithm, photo_addr)

        else:
            self.you_should_choose_pho_first = QMessageBox.warning(self,
                                                                   '温馨提示',
                                                                   '请先在右上角确认您已选择了图片和算法',
                                                                   QMessageBox.Ok)




    def ishide_toolmenu(self):
        if self.ishidden_tool_wid == False:
            self.tool_widget.hide()
            self.ishidden_tool_wid = True
        else:
            self.tool_widget.show()
            self.ishidden_tool_wid = False

    def show_nr_iqa_photo(self, curr_scale=None):

        # pho_show_scale：用于控制显示比例，这个主要是两个照片同时显示的时候和单张显示的区别
        # 单张一般0.7 两张就0.4

        if self.pho_addr_show_le.text() == '':
            pass
        else:
            if curr_scale == None:
                self.show_iqa_photo(dis_mode=1, algo_mode='nr')
            else:
                self.show_iqa_photo(dis_mode=1, algo_mode='nr', scale_of_pho=curr_scale)



    # FR_IQA的相关槽函数
    def fr_iqa_score_callback(self, i):
        self.real_mark_lb_fr.setText(i)
        # 重新使能开始评价并改字
        self.start_mark_btn_fr.setEnabled(True)
        self.start_mark_btn_fr.setText('开始评价')

    def choose_pho_1_fr(self):
        save_path_tuple = QFileDialog.getOpenFileNames(self,
                                                       "请选择一张您想要做FR_IQA的图片(Ground Truth)",
                                                       self.init_open_addr,
                                                       "JPG Files (*.jpg);;PNG Files (*.png);;BMP Files (*.bmp)")
                                                        # 最好还是别用 all file   "All Files (*);;JPG Files (*.jpg);;PNG Files (*.png);;BMP Files (*.bmp)"

        # 防止用户退出，没有选文件，故需判断tuple第一个元素，即文件地址是否为空
        if save_path_tuple[0] == []:
            pass
        else:

            # 更新地址显示文本框
            self.fr_iqa_pho_addr_1 = save_path_tuple[0][0]
            print(self.fr_iqa_pho_addr_1)
            self.refresh_curr_pho_info(is_from_choose=True, pho_num=1)

            # 更新主显示界面和状态栏
            self.show_fr_iqa_photo(shift_mode=1)

    def choose_pho_2_fr(self):
        save_path_tuple = QFileDialog.getOpenFileNames(self,
                                                       "请选择一张您想要做FR_IQA的图片(Distortion Photo)",
                                                       self.init_open_addr,
                                                       "JPG Files (*.jpg);;PNG Files (*.png);;BMP Files (*.bmp)")
                                                        # 最好还是别用 all file   "All Files (*);;JPG Files (*.jpg);;PNG Files (*.png);;BMP Files (*.bmp)"

        # 防止用户退出，没有选文件，故需判断tuple第一个元素，即文件地址是否为空
        if save_path_tuple[0] == []:
            pass
        else:

            # 更新地址显示文本框
            self.fr_iqa_pho_addr_2 = save_path_tuple[0][0]
            print(self.fr_iqa_pho_addr_2)
            self.refresh_curr_pho_info(is_from_choose=True, pho_num=2)

            # 更新主显示界面和状态栏
            self.show_fr_iqa_photo(shift_mode=2)

    def pho_zoom_in_fr(self):

        curr_mode = None  # 目前的显示模式

        if self.img_show_lb_2.isHidden():
        # 单照片显示
            if self.pho_addr_show_le_fr_1.text() != '' or self.pho_addr_show_le_fr_2.text() != '':
                # 获取当前图片地址信息
                curr_pho_addr = (self.current_photo_info[0].split('  ')[1]).split(';')[0]
                if curr_pho_addr == self.pho_addr_show_le_fr_1.text() :
                    curr_mode = 1
                if curr_pho_addr == self.pho_addr_show_le_fr_2.text() :
                    curr_mode = 2

                next_index = self.pho_show_scale_single.index(self.curr_phot_show_scale[0])
                print(next_index)
                if self.pho_show_scale_single[next_index] == self.pho_show_scale_single[-1]:
                    pass
                    print('到顶了')
                else:
                    next_index +=1
                    self.curr_phot_show_scale[0] = self.pho_show_scale_single[next_index]
                    self.show_fr_iqa_photo(shift_mode=curr_mode, curr_scale=self.curr_phot_show_scale)

        else:
            # 多照片同时显示
            # next_index = self.pho_show_scale_single.index(self.curr_phot_show_scale[0])
            # print(next_index)
            # if self.pho_show_scale_single[next_index] == self.pho_show_scale_single[-1]:
            #     pass
            #     print('到顶了')
            # else:
            #     next_index += 1
            #     self.curr_phot_show_scale[0] = self.pho_show_scale_single[next_index]
            #     self.show_fr_iqa_photo(shift_mode=3, curr_scale=self.curr_phot_show_scale)

            # 算了还是别变化了，两个lb在gbox里面充满了，变不了
            pass

    def pho_zoom_out_fr(self):

        curr_mode = None

        if self.img_show_lb_2.isHidden():
            if self.pho_addr_show_le_fr_1.text() != '' or self.pho_addr_show_le_fr_2.text() != '':

                # 获取当前图片地址信息
                curr_pho_addr = (self.current_photo_info[0].split('  ')[1]).split(';')[0]
                if curr_pho_addr == self.pho_addr_show_le_fr_1.text() :
                    curr_mode = 1
                if curr_pho_addr == self.pho_addr_show_le_fr_2.text() :
                    curr_mode = 2

                pre_index = self.pho_show_scale_single.index(self.curr_phot_show_scale[0])
                print(pre_index)
                if self.pho_show_scale_single[pre_index] == self.pho_show_scale_single[0]:
                    pass
                    print('到底了')
                else:
                    pre_index -= 1
                    self.curr_phot_show_scale[0] = self.pho_show_scale_single[pre_index]
                    self.show_fr_iqa_photo(shift_mode=curr_mode, curr_scale=self.curr_phot_show_scale)

        else:
            pass

    def pho_zoom_reset_fr(self):

        if self.img_show_lb_2.isHidden():
            if self.pho_addr_show_le_fr_1.text() == '' and  self.pho_addr_show_le_fr_2.text() == '':
                # 没选照片
                pass
            else:
                # 选了一张
                curr_pho_addr = (self.current_photo_info[0].split('  ')[1]).split(';')[0]
                self.curr_phot_show_scale = [0.7, 0.4]
                if curr_pho_addr == self.pho_addr_show_le_fr_1.text():
                    self.show_fr_iqa_photo(shift_mode=1)
                elif curr_pho_addr == self.pho_addr_show_le_fr_2.text():
                    self.show_fr_iqa_photo(shift_mode=2)
                else:
                    self.show_fr_iqa_photo(shift_mode=1)
        else:
            pass



    def dis_only_p1_fr(self):

        if self.pho_addr_show_le_fr_1.text() != '':
            # 更新当前图片信息 、statusbar、更新面板
            self.refresh_curr_pho_info(is_from_choose=False, pho_num=1)
            self.curr_phot_show_scale = [0.7, 0.4]
            self.show_fr_iqa_photo(shift_mode=1)

    def dis_only_p2_fr(self):

        if self.pho_addr_show_le_fr_2.text() != '':
            # 更新当前图片信息 、statusbar、更新面板
            self.refresh_curr_pho_info(is_from_choose=False, pho_num=2)
            self.curr_phot_show_scale = [0.7, 0.4]
            self.show_fr_iqa_photo(shift_mode=2)

    def dis_all_fr(self):
        # 更新statusbar、更新面板
        if self.pho_addr_show_le_fr_2.text() != '' and self.pho_addr_show_le_fr_2.text() != '':
            self.show_fr_iqa_photo(shift_mode=3)

    def start_score_fr(self):
        if self.pho_addr_show_le_fr_1.text() !='' and  self.pho_addr_show_le_fr_2.text() !='':

            img1 = QImage(self.pho_addr_show_le_fr_1.text())
            img2 = QImage(self.pho_addr_show_le_fr_2.text())
            if img1.height() == img2.height()  and img1.width() == img2.width():
                # 获取当前的算法和图片地址
                algorithm = self.fr_algorithm_comboBox.currentText()
                photo_addr_1 = self.pho_addr_show_le_fr_1.text()
                photo_addr_2 = self.pho_addr_show_le_fr_2.text()
                print(algorithm, photo_addr_1, photo_addr_2)

                # 取消使能 开始评价按键  并提示”正在运行“
                self.start_mark_btn_fr.setEnabled(False)
                self.start_mark_btn.setText('正在评价')

                # 开启线程并运行
                self.fr_iqa_thread.setting(algorithm, photo_addr_1, photo_addr_2)
                self.fr_iqa_thread.start()

            else:
                you_should_choose_same_pho = QMessageBox.warning(self,
                                                                      '温馨提示',
                                                                      '\t请您确认两照片的尺寸，应保证两者相同。',
                                                                      QMessageBox.Ok)
        else:
            you_should_choose_pho_first = QMessageBox.warning(self,
                                                                   '温馨提示',
                                                                   '\t请您确保：在右上角确认您已选择了算法和两张相同尺寸的图片。',
                                                                   QMessageBox.Ok)

    def show_fr_iqa_photo(self, shift_mode, curr_scale=None):

        # 用于显示fr_iqa图片
        # 输入 curr_fr_pho：  1代表为pho1， 2代表pho2
        # shift_mode： 1代表只展示pho1 2只展示pho2， 3代表一起展示

        # 判断他们有没有选图片
        if self.pho_addr_show_le_fr_1.text() == '' and self.pho_addr_show_le_fr_2.text() == '':
            pass

        else:
            if shift_mode == 1:
                if curr_scale == None:
                    self.show_iqa_photo(dis_mode=1, algo_mode='fr_1')
                else:
                    self.show_iqa_photo(dis_mode=1, algo_mode='fr_1', scale_of_pho=curr_scale)


            if shift_mode == 2:
                if curr_scale == None:
                    self.show_iqa_photo(dis_mode=1, algo_mode='fr_2')
                else:
                    self.show_iqa_photo(dis_mode=1, algo_mode='fr_2', scale_of_pho=curr_scale)


            if shift_mode == 3:
                if curr_scale == None:
                    self.show_iqa_photo(dis_mode=2, algo_mode='fr_all')
                else:
                    self.show_iqa_photo(dis_mode=2, algo_mode='fr_all', scale_of_pho=curr_scale)

    # 公共函数
    def resizeEvent(self, evt):
        curr_pho_addr = None
        if self.img_show_lb_2.isHidden():
            if self.current_photo_info !=  []:
                curr_pho_addr = (self.current_photo_info[0].split('  ')[1]).split(';')[0]

            # 判断是哪里的照片  NR OR FR
            if curr_pho_addr == self.pho_addr_show_le.text():
                self.show_nr_iqa_photo()
            elif curr_pho_addr == self.pho_addr_show_le_fr_1.text():
                self.show_fr_iqa_photo(shift_mode=1, curr_scale=self.curr_phot_show_scale)
            else:
                self.show_fr_iqa_photo(shift_mode=2, curr_scale=self.curr_phot_show_scale)

        else:
            self.show_fr_iqa_photo(shift_mode=3, curr_scale=self.curr_phot_show_scale)

    def refresh_curr_pho_info(self, is_from_choose, pho_num):
        # 根据NR FR IQA选择到到底去更新哪个
        # is_choose 用于判断是否为通过选择图片来更新的; 他如果是从选择而来，那么需要更新lineedit组件
        # pho_num: 0： nr_iqa的图片； 1：fr_iqa的图片1； 2：fr_iqa的图片2；
        # 更新地址显示文本框
        if pho_num == 0:
            self.iqa_pho_addr = self.nr_iqa_pho_addr
            if is_from_choose:
                self.pho_addr_show_le.setText(str(self.nr_iqa_pho_addr))
        elif pho_num == 1:
            self.iqa_pho_addr = self.fr_iqa_pho_addr_1
            if is_from_choose:
                self.pho_addr_show_le_fr_1.setText(str(self.fr_iqa_pho_addr_1))
        else:
            self.iqa_pho_addr = self.fr_iqa_pho_addr_2
            if is_from_choose:
                self.pho_addr_show_le_fr_2.setText(str(self.fr_iqa_pho_addr_2))

        # print(self.iqa_pho_addr)


        if self.current_photo_info == []:
            self.current_photo_info.append("当前的照片为:  " + str(self.iqa_pho_addr) + ";    ")
        else:
            self.current_photo_info[0] = "当前的照片为:  " + str(self.iqa_pho_addr) + ";    "
        print('【refresh_curr_pho_info】当前图片地址信息为：', self.current_photo_info)

    def show_iqa_photo(self, dis_mode, algo_mode, scale_of_pho=None):
        # dis_mode 表示到底是要显示一张还是显示两张
        # 1 一张  2 两张
        # algo_mode 代表不同算法
        # ‘nr’ 无参考  ‘fr_1’ 全参考1,  'fr_2' 全参考2
        img = None
        curr_pho_addr = None

        # 如果是未指定scale就用默认的，否则从self.curr_phot_show_scale找
        if scale_of_pho == None:
            scale_of_pho = [0.7, 0.4]
        else:
            scale_of_pho = self.curr_phot_show_scale

        # 判断是哪张图
        if algo_mode == 'nr':
            img = QImage(self.nr_iqa_pho_addr)
            curr_pho_addr = self.nr_iqa_pho_addr
        if algo_mode == 'fr_1':
            img = QImage(self.fr_iqa_pho_addr_1)
            curr_pho_addr = self.fr_iqa_pho_addr_1
        if algo_mode == 'fr_2':
            img = QImage(self.fr_iqa_pho_addr_2)
            curr_pho_addr = self.fr_iqa_pho_addr_2
        if algo_mode == 'fr_all':
            pass


        # 判断是哪种模式
        if dis_mode == 1:
            # 先把第二个lb关掉
            self.img_show_lb_2.hide()
            # scale定义为single的scale， 默认0.7
            pho_show_scale = scale_of_pho[0]
            # 更新状态栏
            if len(self.current_photo_info) <= 1:
                self.current_photo_info.append("图片实际大小为:  " + str(img.width()) + " ✖ " + str(img.height()) + ";    ")
            else:
                self.current_photo_info[1] = "图片实际大小为:  " + str(img.width()) + " ✖ " + str(img.height()) + ";    "
            print(self.current_photo_info)
            self.statusbar.showMessage(''.join(self.current_photo_info))

            # 根据图片长宽比来调整label的尺寸
            if img.height() > img.width():
                # 设置4：3尺寸，如果宽高比是3：4 那么吧label也变一下再展示
                self.img_show_lb.setFixedSize((self.main_show_gbox.height() * pho_show_scale) / self.ratio_of_photo,
                                              self.main_show_gbox.height() * pho_show_scale)

                jpg = QtGui.QPixmap(curr_pho_addr).scaled(self.img_show_lb.width(),
                                                                 self.img_show_lb.height(),
                                                                 Qt.KeepAspectRatio,
                                                                 # 保持宽长比，然后缩放后不超过最长边   另外两种为IgnoreAspectRatio  KeepAspectRatioByExpanding
                                                                 Qt.SmoothTransformation)  # 双线性插值  另一种为FastTransformation 不使用插值  详见https://www.cnblogs.com/qixianyu/p/6891054.html
                self.img_show_lb.setPixmap(jpg)
            else:

                self.img_show_lb.setFixedSize(self.main_show_gbox.width() * pho_show_scale,
                                              (self.main_show_gbox.width() * pho_show_scale) / self.ratio_of_photo)

                jpg = QtGui.QPixmap(curr_pho_addr).scaled(self.img_show_lb.width(),
                                                                 self.img_show_lb.height(),
                                                                 Qt.KeepAspectRatio,
                                                                 Qt.SmoothTransformation)
                self.img_show_lb.setPixmap(jpg)
        if dis_mode == 2:
            # 先把第二个lb打开
            self.img_show_lb_2.show()
            # scale定义为double的scale， 默认0.4
            pho_show_scale = scale_of_pho[1]

            img = QImage(self.fr_iqa_pho_addr_1)
            img_2 = QImage(self.fr_iqa_pho_addr_2)
            # 更新状态栏

            self.statusbar.showMessage('两张照片做对比：左图为：图片1； 右图为：图片2。')

            # 根据图片长宽比来调整label的尺寸
            if img.height() > img.width():
                # 设置4：3尺寸，如果宽高比是3：4 那么吧label也变一下再展示
                self.img_show_lb.setFixedSize((self.main_show_gbox.height() * pho_show_scale) / self.ratio_of_photo,
                                              self.main_show_gbox.height() * pho_show_scale)

                jpg = QtGui.QPixmap(self.fr_iqa_pho_addr_1).scaled(self.img_show_lb.width(),
                                                                 self.img_show_lb.height(),
                                                                 Qt.KeepAspectRatio,
                                                                 # 保持宽长比，然后缩放后不超过最长边   另外两种为IgnoreAspectRatio  KeepAspectRatioByExpanding
                                                                 Qt.SmoothTransformation)  # 双线性插值  另一种为FastTransformation 不使用插值  详见https://www.cnblogs.com/qixianyu/p/6891054.html
                self.img_show_lb.setPixmap(jpg)
            else:

                self.img_show_lb.setFixedSize(self.main_show_gbox.width() * pho_show_scale,
                                              (self.main_show_gbox.width() * pho_show_scale) / self.ratio_of_photo)

                jpg = QtGui.QPixmap(self.fr_iqa_pho_addr_1).scaled(self.img_show_lb.width(),
                                                                 self.img_show_lb.height(),
                                                                 Qt.KeepAspectRatio,
                                                                 Qt.SmoothTransformation)
                self.img_show_lb.setPixmap(jpg)

            if img_2.height() > img_2.width():
                # 设置4：3尺寸，如果宽高比是3：4 那么吧label也变一下再展示
                self.img_show_lb_2.setFixedSize((self.main_show_gbox.height() * pho_show_scale) / self.ratio_of_photo,
                                              self.main_show_gbox.height() * pho_show_scale)

                jpg2 = QtGui.QPixmap(self.fr_iqa_pho_addr_2).scaled(self.img_show_lb_2.width(),
                                                                 self.img_show_lb_2.height(),
                                                                 Qt.KeepAspectRatio,
                                                                 # 保持宽长比，然后缩放后不超过最长边   另外两种为IgnoreAspectRatio  KeepAspectRatioByExpanding
                                                                 Qt.SmoothTransformation)  # 双线性插值  另一种为FastTransformation 不使用插值  详见https://www.cnblogs.com/qixianyu/p/6891054.html
                self.img_show_lb_2.setPixmap(jpg2)
            else:

                self.img_show_lb_2.setFixedSize(self.main_show_gbox.width() * pho_show_scale,
                                              (self.main_show_gbox.width() * pho_show_scale) / self.ratio_of_photo)

                jpg2 = QtGui.QPixmap(self.fr_iqa_pho_addr_2).scaled(self.img_show_lb_2.width(),
                                                                 self.img_show_lb_2.height(),
                                                                 Qt.KeepAspectRatio,
                                                                 Qt.SmoothTransformation)
                self.img_show_lb_2.setPixmap(jpg2)

    def quick_change_pho_by_mouse(self):
        if not (self.pho_addr_show_le.text() =='' and self.pho_addr_show_le_fr_1.text() == '' and self.pho_addr_show_le_fr_2.text() == ''):
            quick_opt_Menu = QMenu()
            quick_opt_Menu.addAction(QAction(u'放大', self))
            quick_opt_Menu.addAction(QAction(u'缩小', self))
            quick_opt_Menu.triggered[QAction].connect(self.processtrigger)
            quick_opt_Menu.exec_(QCursor.pos())

        # 右键按钮事件

    def processtrigger(self, q):
        # 输出那个Qmenu对象被点击
        if q.text() == "放大":
            if self.img_show_lb_2.isHidden():
                curr_pho_addr = (self.current_photo_info[0].split('  ')[1]).split(';')[0]
                if curr_pho_addr == self.pho_addr_show_le.text():
                    self.pho_zoom_in()
                else:
                    self.pho_zoom_in_fr()
            else:
                pass
        elif q.text() == "缩小":
            if self.img_show_lb_2.isHidden():
                curr_pho_addr = (self.current_photo_info[0].split('  ')[1]).split(';')[0]
                if curr_pho_addr == self.pho_addr_show_le.text():
                    self.pho_zoom_out()
                else:
                    self.pho_zoom_out_fr()
            else:
                pass



    # def mousePressEvent(self, event):
    #     if event.button() == Qt.LeftButton:
    #         # 判断是否鼠标在控件上 后来发现其实不需要，只需要把m_flag初始化！
    #         # if not (self.start_button.underMouse() or self.exit_button.underMouse() or self.change_skin_button.underMouse() or self.get_info_button.underMouse() ):
    #         self.m_flag = True
    #         self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
    #         event.accept()
    #         self.setCursor(QCursor(Qt.ClosedHandCursor))  # 更改鼠标图标
    #
    # def mouseMoveEvent(self, QMouseEvent):
    #     if Qt.LeftButton and self.m_flag:
    #         self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
    #         QMouseEvent.accept()
    #
    # def mouseReleaseEvent(self, QMouseEvent):
    #     self.m_flag = False
    #     self.setCursor(QCursor(Qt.ArrowCursor))


# NR_IQA评分线程
class My_NR_IQA_Thread(QThread): # 建立一个任务线程类

    score_signal = pyqtSignal(str) #设置触发信号传递的参数数据类型,这里是字符串

    def __init__(self):
        super(My_NR_IQA_Thread, self).__init__()

    def setting(self, algorithm, pho_path, eng):
        self.algo = algorithm
        self.pho_path = pho_path
        self.eng = eng

    def run(self): # 在启动线程后任务从这个函数里面开始执行

        algo = goto_nriqa()
        score = algo.run(algorithm_name=self.algo, photo_path=self.pho_path, eng=self.eng)
        score = np.round(float(str(score)), 4)
        print(score)
        # main_iqa_pane.real_mark_lb.setText(str(score).split('.')[0])
        self.score_signal.emit(str(score))

# FR_IQA评分线程
class My_FR_IQA_Thread(QThread): # 建立一个任务线程类

    fr_score_signal = pyqtSignal(str) #设置触发信号传递的参数数据类型,这里是字符串

    def __init__(self):
        super(My_FR_IQA_Thread, self).__init__()

    def setting(self, algorithm, pho_path_1, pho_path_2):
        self.algo = algorithm
        self.pho_path_1 = pho_path_1
        self.pho_path_2 = pho_path_2

    def run(self): # 在启动线程后任务从这个函数里面开始执行

        algo = FR_IQA_method()
        score = algo.get_score(self.algo, self.pho_path_1, self.pho_path_2)
        if self.algo == 'SSIM':
            score = str(np.round(float(str(score[0])), 3)) + ',' +  str(np.round(float(str(score[1])), 3))
        else:
            score = np.round(float(str(np.real(score))), 4)
        print(score)
        # main_iqa_pane.real_mark_lb.setText(str(score).split('.')[0])
        self.fr_score_signal.emit(str(score))

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = MainIQAPane()

    # # 窗口最大话
    # window.showMaximized()

    # window.exit_signal.connect(lambda :print("退出"))
    # window.register_account_pwd_signal.connect(lambda a, p: print(a, p))
    window.show()


    sys.exit(app.exec_())