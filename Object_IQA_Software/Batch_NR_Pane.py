from PyQt5.Qt import *
import os
import matlab.engine
import numpy as np

from Object_IQA_Software.resource.batch_nr_choice import Ui_Form  #如果打包记得改！
from Object_IQA_Software.method.NR_IQA_method.NR_IQA_algorithm import goto_nriqa

class BatchNRPane(QWidget, Ui_Form):

    finish_this_batch_signal = pyqtSignal()

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        #打开背景图片的设置
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.m_flag = False


        self.progressBar_2.setValue(0)
        self.all_pho_num = 0
        self.curr_pho_num = 1


        data = r'C:/Users/xmhh/Desktop/data'
        mos = r'C:/Users/xmhh/Desktop/mos.txt'
        self.pho_addr_show_le.setText(data)
        self.mos_addr_show_le_2.setText(mos)

        # 初始化一个评分线程
        self.nr_iqa_thread = My_NR_IQA_Thread()
        self.nr_iqa_thread.score_signal.connect(self.nr_iqa_score_callback)
        self.record = []

    def choose_pho(self):
        save_path_tuple = QFileDialog.getExistingDirectory(self,
                                                           "请选择一张您想要做NR_IQA的图片",
                                                            )

        # 防止用户退出，没有选文件，故需判断tuple第一个元素，即文件地址是否为空
        if save_path_tuple == []:
            pass
        else:
            # 更新地址显示文本框 清空进度
            print(save_path_tuple)
            self.pho_addr_show_le.setFixedWidth(len(save_path_tuple) * 8)
            self.pho_addr_show_le.setText(str(save_path_tuple))
            self.progressBar_2.setValue(0)

    def choose_mos(self):
        save_path_tuple = QFileDialog.getOpenFileName(self,
                                                       "请选择一张您想要做NR_IQA的图片",
                                                      None,
                                                      "TXT Files (*.txt)")

        # 防止用户退出，没有选文件，故需判断tuple第一个元素，即文件地址是否为空
        if save_path_tuple[0] == []:
            pass
        else:
            # 更新地址显示文本框 清空进度
            print(save_path_tuple[0])
            self.mos_addr_show_le_2.setFixedWidth(len(save_path_tuple[0])*8)
            self.mos_addr_show_le_2.setText(str(save_path_tuple[0]))

    def set(self,algo):
        self.algo_le.setText(algo)


    def start(self):
        if not (self.pho_addr_show_le.text() =='' or self.mos_addr_show_le_2.text()==''):
            # 首先计算所有图片的地址
            pho_list = []
            for root, directory, files in os.walk(self.pho_addr_show_le.text()):
                for filename in files:
                    name, suf = os.path.splitext(filename)
                    if suf in ['.bmp', '.jpg', '.png']:
                        pho_list.append(os.path.join(root, filename))

            print(pho_list)
            if pho_list==[]:
                QMessageBox.warning(self,
                                    '温馨提示',
                                    '文件夹没有有效的照片，请您检查',
                                    QMessageBox.Ok)
            else:
                # 初始化参数
                self.all_pho_num = len(pho_list)
                self.curr_pho_num = 1

                eng = matlab.engine.start_matlab()

                self.start_mark_btn.setEnabled(False)
                self.start_mark_btn.setText('正在评价')

                # 开启线程并运行
                self.nr_iqa_thread.setting(algorithm=self.algo_le.text(), pho_path=pho_list, eng=eng)
                self.nr_iqa_thread.start()



        else:
            QMessageBox.warning(self,
                                '温馨提示',
                                '请先在确认您已选择了图片和MOS记录地址',
                                QMessageBox.Ok)

    def bye(self):
        self.close()
        self.finish_this_batch_signal.emit()

    def exit_this_exe(self):
        self.close()

    def nr_iqa_score_callback(self, pho, score):
        if self.curr_pho_num == 1:
            with open(self.mos_addr_show_le_2.text(), 'a') as f:
                f.write('\n' + '##############################   这是' + self.algo_le.text() +'的评分   ##############################' +'\n')
            f.close()

        print('########评分结果###########')
        print(pho + ', ' + score)
        self.record.append(pho + ', ' + score)
        print('##########################')
        self.progressBar_2.setValue( int((self.curr_pho_num*1.0/self.all_pho_num)*100) )
        self.curr_pho_num +=1
        if self.curr_pho_num > self.all_pho_num:
            self.curr_pho_num = 1
            with open(self.mos_addr_show_le_2.text(), 'a') as f:
                f.write('\n'.join(self.record))
            f.close()

            self.record=[]
            print('结束啦')
            QMessageBox.information(self,
                                    '温馨提示',
                                    '已评分结束哦~',
                                    QMessageBox.Ok)
            self.progressBar_2.setValue(0)
            self.start_mark_btn.setEnabled(True)
            self.start_mark_btn.setText('开始评价')

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            # 判断是否鼠标在控件上 后来发现其实不需要，只需要把m_flag初始化！
            # if not (self.start_button.underMouse() or self.exit_button.underMouse() or self.change_skin_button.underMouse() or self.get_info_button.underMouse() ):
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QCursor(Qt.ClosedHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))

# NR_IQA评分线程
class My_NR_IQA_Thread(QThread): # 建立一个任务线程类

    score_signal = pyqtSignal(str, str) #设置触发信号传递的参数数据类型,这里是字符串

    def __init__(self):
        super(My_NR_IQA_Thread, self).__init__()



    def setting(self, algorithm, pho_path, eng):
        self.algo = algorithm
        self.pho_path = pho_path
        self.eng = eng

    def run(self): # 在启动线程后任务从这个函数里面开始执行

        algo = goto_nriqa()
        for pho in self.pho_path:
            score = algo.run(algorithm_name=self.algo, photo_path=pho, eng=self.eng)
            score = np.round(float(str(score)), 4)
            print(score)
            # main_iqa_pane.real_mark_lb.setText(str(score).split('.')[0])
            self.score_signal.emit(pho, str(score))

    def stop(self):
        self.stop()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = BatchNRPane()
    window.set('BRISQUE')
    # window.exit_signal.connect(lambda :print("退出"))
    # window.register_account_pwd_signal.connect(lambda a, p: print(a, p))
    window.show()

    sys.exit(app.exec_())