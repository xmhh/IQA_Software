import json
import os
from PyQt5.Qt import *
from resource.Settings_dabianyong import Ui_Form
# from resource.style.FontAwesome import FontAwesomes


class Settings_Pane(QWidget, Ui_Form):

    refresh_pho_list_in_mainpane_signal = pyqtSignal()
    goto_diy_pho_size_signal = pyqtSignal()
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)


        # 设置qss样式
        # self.setStyleSheet(open("resource/style/setting_pane.qss", "rb").read().decode("utf-8"))

        # 打开背景图片的设置
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)
        # self.setStyleSheet(open("resource/style/setting_pane.qss", "rb").read().decode("utf-8"))

        # self.setWindowFlag(Qt.FramelessWindowHint)

        # 绑定滚动条和item事件
        self.scrollArea.verticalScrollBar().valueChanged.connect(self.value_changed)
        self.setting_listWidget.itemClicked.connect(self.onItemClicked)

        self._blockSignals = False


        # dis_ratio_list = ["4:3", "16:9"]
        # self.dis_ratio_cbox.addItems(dis_ratio_list)

        # 设置item索引字典 用于选中跳转至对应区域
        self.item_dict = {
            "0": "database_gbox",  # 数据库
            "1": "mos_gbox",  # MOS记录
            "2": "exp_gbox",  # 实验参数
            "3": "photo_dis_gbox",  # 主显示
            "4": "tester_gbox",  # 测试者
            "5": "others_gbox",  # 其他
        }

        self.refresh()

    def exit_to_save(self):
        self.refresh_pho_list_in_mainpane_signal.emit()

    def closeEvent(self, QCloseEvent):
        if self.configure["Database"]["LoadUrl"] == '' or self.configure["MosRecord"]["SaveUrl"] == '':
            QMessageBox.information(self, '提示', '请您确认您选择了数据库和MOS存储地址。', QMessageBox.Ok)
            QCloseEvent.ignore()

        elif self.lineEdit_4.isEnabled() or self.lineEdit_5.isEnabled() or self.lineEdit_7.isEnabled() or self.lineEdit_8.isEnabled() or self.lineEdit_14.isEnabled() or self.lineEdit_15.isEnabled() or self.lineEdit_16.isEnabled() :
            QMessageBox.information(self, "提示", "请您更改时间的设置后，记得保存更改！", QMessageBox.Ok)
            QCloseEvent.ignore()

        else:
            res = QMessageBox.question(self, '提示', '是否保存当前设置？', QMessageBox.Yes | QMessageBox.No,
                                       QMessageBox.No)  # 两个按钮是否， 默认No则关闭这个提示框

            if res == QMessageBox.Yes:
                # 由于在途中会遇到改变pho_size列表的事件，触发槽函数，导致每次都次都是index=0,因此放到最后再改变
                self.configure['PhotoDis']['PhotoSize']['TestSize']['CurrentPhotoSize'] = self.test_size_cbox.currentIndex()
                f = open("settings/configure.json", 'w', encoding='UTF-8')
                json.dump(self.configure, f, indent=4, separators=(',', ':'))
                f.close()
                # 向主面板发射信号，要记得保存并更新这些配置
                self.exit_and_save()

            QCloseEvent.accept()

    def exit_and_save(self):
        self.refresh_pho_list_in_mainpane_signal.emit()

    def refresh(self):
        with open("./settings/configure.json", "r", encoding='UTF-8') as f:
            self.configure = json.load(f)
        f.close()
        print(self.configure)
        #######################################################################################################
        ############################## 对设置中的数据进行UI显示更新  ##############################################
        #######################################################################################################

        ####################################   数据库设置  #####################################################
        leng = len(self.configure['Database']['LoadUrl']) * 10
        if leng == 0:
            leng = 100
        self.lineEdit.setFixedWidth(leng)
        self.lineEdit.setText(self.configure['Database']['LoadUrl'])


        #########################################   MOS设置  ##################################################

        # 当前MOS记录格式
        current_mos_style = self.configure['MosRecord']['Style']['CurrentStyle']
        self.comboBox.setCurrentText(self.configure['MosRecord']['Style']['StyleDict'][current_mos_style])
        # mos记录地址
        leng = len(self.configure['MosRecord']['SaveUrl'])*10
        if leng == 0:
            leng = 100
        self.lineEdit_3.setFixedWidth(leng)
        self.lineEdit_3.setText(self.configure['MosRecord']['SaveUrl'])


        #######################################   实验参数设置  ###############################################

        #dsis t1
        time = self.configure["ExpParameter"]["TimeSettings"]["DSIS_T1"]
        self.horizontalSlider.setValue(int(time))
        self.lineEdit_4.setText(time)
        self.lineEdit_4.setAlignment(Qt.AlignHCenter)
        self.lineEdit_4.setEnabled(False)
        #dsis t2
        time = self.configure["ExpParameter"]["TimeSettings"]["DSIS_T2"]
        self.horizontalSlider_2.setValue(int(time))
        self.lineEdit_5.setText(time)
        self.lineEdit_5.setAlignment(Qt.AlignHCenter)
        self.lineEdit_5.setEnabled(False)

        #dsis t3
        time = self.configure["ExpParameter"]["TimeSettings"]["DSIS_T3"]
        self.horizontalSlider_3.setValue(int(time))
        self.lineEdit_7.setText(time)
        self.lineEdit_7.setAlignment(Qt.AlignHCenter)
        self.lineEdit_7.setEnabled(False)
        #dsis t4
        time = self.configure["ExpParameter"]["TimeSettings"]["DSIS_T4"]
        self.horizontalSlider_4.setValue(int(time))
        self.lineEdit_8.setText(time)
        self.lineEdit_8.setAlignment(Qt.AlignHCenter)
        self.lineEdit_8.setEnabled(False)
        #ss t1
        time = self.configure["ExpParameter"]["TimeSettings"]["SS_T1"]
        self.horizontalSlider_5.setValue(int(time))
        self.lineEdit_14.setText(time)
        self.lineEdit_14.setAlignment(Qt.AlignHCenter)
        self.lineEdit_14.setEnabled(False)
        #ss t2
        time = self.configure["ExpParameter"]["TimeSettings"]["SS_T2"]
        self.horizontalSlider_6.setValue(int(time))
        self.lineEdit_15.setText(time)
        self.lineEdit_15.setAlignment(Qt.AlignHCenter)
        self.lineEdit_15.setEnabled(False)
        #ss t3
        time = self.configure["ExpParameter"]["TimeSettings"]["SS_T3"]
        self.horizontalSlider_7.setValue(int(time))
        self.lineEdit_16.setText(time)
        self.lineEdit_16.setAlignment(Qt.AlignHCenter)
        self.lineEdit_16.setEnabled(False)

        #  评分形式设置
        index =  self.configure['ExpParameter']['MarkSettings']['CurrentShowStyle']
        self.comboBox_2.setCurrentIndex(int(index))

        #######################################   图片显示设置  ###############################################
        # 显示比例
        self.dis_ratio_cbox.setCurrentIndex(int(self.configure['PhotoDis']['DisplayScale']['CurrentDisScale']))
        # 图片大小
        size_item = []
        for value in self.configure['PhotoDis']['PhotoSize']['TestSize']['PhoSizeDict'].values():
            size_item.append(value)
        size_item = [item.replace(',', ' x ') for item in size_item]
        self.test_size_cbox.addItems(size_item)
        self.gt_size_cbox.addItems(size_item)
        print(self.configure['PhotoDis']['PhotoSize']['TestSize']['CurrentPhotoSize'])
        self.test_size_cbox.setCurrentIndex(int(self.configure['PhotoDis']['PhotoSize']['TestSize']['CurrentPhotoSize']))
        self.gt_size_cbox.setCurrentIndex(int(self.configure['PhotoDis']['PhotoSize']['TestSize']['CurrentPhotoSize']))
        # 插值
        self.inter_cbox.setCurrentIndex(int(self.configure['PhotoDis']['Interpolation']['CurrentInter']))
        # 屏幕
        index = self.configure['PhotoDis']['DisForDSIS']['CurrentStyle']
        if index == '0':
            self.radioButton.setChecked(True)
        if index == '1':
            self.radioButton_2.setChecked(True)
        if index == '2':
            self.radioButton_3.setChecked(True)
        if index == '3':
            self.radioButton_4.setChecked(True)
        if index == '4':
            self.radioButton_5.setChecked(True)

        #######################################   受试者设置  ###############################################
        testee_url = self.configure['TesteeInfo']['SaveUrl']
        if not os.path.exists(testee_url):
            testee_url = os.path.join(os.getcwd(), 'testee.txt')
            f = open(testee_url, 'w')
            f.close()
            self.configure['TesteeInfo']['SaveUrl'] = testee_url
            leng = len(testee_url) * 9
        else:
            testee_url =  self.configure['TesteeInfo']['SaveUrl']

        leng = len(testee_url) * 9
        self.lineEdit_9.setFixedWidth(leng)
        self.lineEdit_9.setText(testee_url)
        #######################################   其他设置  ###############################################


    def value_changed(self):
        """滚动条"""
        if self._blockSignals:
            # 防止item改变滚动条会触发这里
            return

        for i in range(6):  # 因为这里右侧有10个选项
            widget = getattr(self, self.item_dict[str(i)])
            # widget不为空且在可视范围内
            if widget and not widget.visibleRegion().isEmpty():
                self.setting_listWidget.setCurrentRow(i)  # 设置item的选中
                return

    def onItemClicked(self, item):
        """左侧item"""
        row = self.setting_listWidget.row(item)  # 获取点击的item的索引
        widget = getattr(self, self.item_dict[str(row)], None)
        if not widget:
            return
        # 定位右侧位置并滚动
        self._blockSignals = True
        self.scrollArea.verticalScrollBar().setSliderPosition(widget.pos().y())
        self._blockSignals = False

    def goto_exact_body(self, item):
        setting_dict = {
            "数据库设置": 0,
            "MOS记录": 1,
            "实验参数": 2,
            "主显示界面": 3,
            "测试者信息": 4,
            "其他设置": 5
        }
        row = 0
        for key, values in setting_dict.items():
            if key == item:
                row = int(values)

        self.setting_listWidget.setCurrentRow(row)
        widget = getattr(self, self.item_dict[str(row)], None)
        if not widget:
            return
        # 定位右侧位置并滚动
        self._blockSignals = True
        self.scrollArea.verticalScrollBar().setSliderPosition(widget.pos().y())
        self._blockSignals = False

    ##########################  有关数据库设置的槽函数  ########################
    def database_path(self):
        database_path = QFileDialog.getExistingDirectory(self,
                                                         "请选择测试数据源的文件夹路径",
                                                         None)

        if not database_path == '':
            # 提示信息
            print("数据库地址重新被设置了：", database_path)
            self.configure["Database"]["LoadUrl"] = str(database_path)

            # 更新UI
            self.lineEdit.setFixedWidth(int(len(database_path)) * 10)
            self.lineEdit.setText(database_path)

        else:
            pass

    ##########################  有关MOS设置的槽函数  ##########################
    # mos记录格式
    def mos_content_conclude(self, index):
        self.configure["MosRecord"]["Style"]["CurrentStyle"] = str(index)
        print("mos记录格式被改变")
    # 改变mos记录地址
    def mos_path(self):
        mos_path_tuple = QFileDialog.getOpenFileNames(self,
                                                      "请选择保存您主观评价得分的文本路径",
                                                      None,
                                                      "Txt Files (*.txt);;Excel Files (*.xls);;All Files (*)")
        if not mos_path_tuple[0] == []:
            # tuple的样式为([], '')
            # 提示信息
            mos_path = mos_path_tuple[0][0]
            print("MOS地址重新被设置了：", mos_path)
            self.configure["MosRecord"]["SaveUrl"] = str(mos_path)

            # 更新UI
            self.lineEdit_3.setFixedWidth(int(len(mos_path)) * 10)
            self.lineEdit_3.setText(mos_path)
        else:
            pass

    ##########################  有关实验参数设置的槽函数  ######################
    # 时间设置
    def dsis_t1(self, times):
        self.lineEdit_4.setEnabled(True)
        self.lineEdit_4.setText(str(times))
    def dsis_t1_ensure(self):
        self.lineEdit_4.setEnabled(False)
        self.configure["ExpParameter"]["TimeSettings"]["DSIS_T1"] = self.lineEdit_4.text()

    def dsis_t2(self, times):
        self.lineEdit_5.setEnabled(True)
        self.lineEdit_5.setText(str(times))
    def dsis_t2_ensure(self):
        self.lineEdit_5.setEnabled(False)
        self.configure["ExpParameter"]["TimeSettings"]["DSIS_T2"] = self.lineEdit_5.text()

    def dsis_t3(self, times):
        self.lineEdit_7.setEnabled(True)
        self.lineEdit_7.setText(str(times))
    def dsis_t3_ensure(self):
        self.lineEdit_7.setEnabled(False)
        self.configure["ExpParameter"]["TimeSettings"]["DSIS_T3"] = self.lineEdit_7.text()

    def dsis_t4(self, times):
        self.lineEdit_8.setEnabled(True)
        self.lineEdit_8.setText(str(times))
    def dsis_t4_ensure(self):
        self.lineEdit_8.setEnabled(False)
        self.configure["ExpParameter"]["TimeSettings"]["DSIS_T4"] = self.lineEdit_8.text()

    def ss_t1(self, times):
        self.lineEdit_14.setEnabled(True)
        self.lineEdit_14.setText(str(times))
    def ss_t1_ensure(self):
        self.lineEdit_14.setEnabled(False)
        self.configure["ExpParameter"]["TimeSettings"]["SS_T1"] = self.lineEdit_14.text()

    def ss_t2(self, times):
        self.lineEdit_15.setEnabled(True)
        self.lineEdit_15.setText(str(times))
    def ss_t2_ensure(self):
        self.lineEdit_15.setEnabled(False)
        self.configure["ExpParameter"]["TimeSettings"]["SS_T2"] = self.lineEdit_15.text()

    def ss_t3(self, times):
        self.lineEdit_16.setEnabled(True)
        self.lineEdit_16.setText(str(times))
    def ss_t3_ensure(self):
        self.lineEdit_16.setEnabled(False)
        self.configure["ExpParameter"]["TimeSettings"]["SS_T3"] = self.lineEdit_16.text()

    # 评分形式设置
    def mark_style_change(self, index):
        self.configure['ExpParameter']['MarkSettings']['CurrentShowStyle'] = str(index)

    ##########################  有关显示参数设置的槽函数  ######################
    # 显示尺寸
    def display_ratio(self, index):
        self.configure['PhotoDis']['DisplayScale']['CurrentDisScale'] = str(index)
    # 图片大小
    def test_pic_size(self, index):
        self.gt_size_cbox.setCurrentIndex(int(index))

    def GT_pic_size(self, index):
        self.test_size_cbox.setCurrentIndex(int(index))

    def diy_pho_size(self): # 暂时没用！！！！
        pass

    def goto_diy_pho_size(self):
        self.goto_diy_pho_size_signal.emit()

    # 插值方式
    def interp_style(self, index):
        self.configure['PhotoDis']['Interpolation']['CurrentInter'] = str(index)

    # 屏幕选择
    def screen1_dis_style(self):
        self.configure['PhotoDis']['DisForDSIS']['CurrentStyle'] = '0'
    def screenlr_dis_style(self):
        self.configure['PhotoDis']['DisForDSIS']['CurrentStyle'] = '1'
    def screenud_dis_style(self):
        self.configure['PhotoDis']['DisForDSIS']['CurrentStyle'] = '2'
    def screen2_dis_style(self):
        self.configure['PhotoDis']['DisForDSIS']['CurrentStyle'] = '3'
    def screen_peid_style(self):
        self.configure['PhotoDis']['DisForDSIS']['CurrentStyle'] = '4'






    ############################## 改变受试者的存储地址   ######################
    def testee_path(self):

        testee_path_tuple = QFileDialog.getOpenFileNames(self,
                                                         "请选择保存受试者信息的文本路径（如果采用本地记录）",
                                                         None,
                                                         "Txt Files (*.txt);;Excel Files (*.xls);;All Files (*)")
        if not testee_path_tuple[0] == []:
            # tuple的样式为([], '')

            # 提示信息
            testee_path = testee_path_tuple[0][0]
            print("测试者信息地址重新被设置了：", testee_path)
            self.configure["TesteeInfo"]["SaveUrl"] = str(testee_path)

            # 更新UI
            self.lineEdit_9.setFixedWidth(int(len(testee_path))*10)
            self.lineEdit_9.setText(testee_path)

        else:
            pass

    ###############################      其他设置       ######################       准备弄一个问卷之类的吧
    def feedback(self):
        project_link = "https://www.wjx.cn/jq/77224175.aspx"
        QDesktopServices.openUrl(QUrl(project_link))


    # 了解更多，打开课题组的主页
    def learn_more(self):
        project_link = "http://gr.xjtu.edu.cn/web/xqmou/iqa"
        QDesktopServices.openUrl(QUrl(project_link))




    






if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = Settings_Pane()
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
