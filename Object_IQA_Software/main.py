from Object_IQA_Software.Start_Pane import StartChoicePane  # 记得改！！！！！！！！！！！！！
from Object_IQA_Software.Main_IQA_Pane import MainIQAPane
from Object_IQA_Software.Batch_NR_Pane import BatchNRPane

from PyQt5.Qt import *






if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    # engine = matlab.engine.start_matlab()

    # 控制面板的创建
    start_choice_pane = StartChoicePane()
    main_iqa_pane = MainIQAPane()

    #批处理线程的创建
    batch_nr_pane = BatchNRPane()

    main_iqa_pane.algorithm_comboBox.clear()
    algorithm_list = ['BIQI', 'BRISQUE', 'NIQE', 'BLIINDS_2', 'CPBD', 'NJQA']
    main_iqa_pane.algorithm_comboBox.addItems(algorithm_list)




    # 槽函数
    def jump_to_mainexp():
        start_choice_pane.close()
        main_iqa_pane.show()


    def start_batch_nr_thread(algo):
        if algo in algorithm_list:
            if main_iqa_pane.is_batch_active == False:
                batch_nr_pane.set(algo)
                batch_nr_pane.show()
                main_iqa_pane.is_batch_active = True

            else:
                QMessageBox.warning(main_iqa_pane,
                                    '温馨提示',
                                    '请您先进行完当前的批处理评分并退出后，再来选择其他的评分算法！',
                                    QMessageBox.Ok)

    def finish_this_nr_batch():
        main_iqa_pane.is_batch_active = False




    # def caculate_nr_iqa_mark(algorithm, photo_path):
    #     main_iqa_pane.all_info_of_iqa_te.setText('提示：\n正在进行评分，\n请勿重复按键~')
    #
    #     if main_iqa_pane.pho_addr_show_le.text() == '':
    #         main_iqa_pane.all_info_of_iqa_te.append('提示：请先选择图片，然后再进行评分！')
    #
    #     else:
    #         main_iqa_pane.start_mark_btn.setEnabled(False)
    #
    #         algo = goto_nriqa()
    #
    #         score = algo.run(algorithm_name=algorithm, photo_path=photo_path, eng=engine)
    #         score = np.round(float(str(score)), 4)
    #         print(score)
    #         # main_iqa_pane.real_mark_lb.setText(str(score).split('.')[0])
    #         main_iqa_pane.real_mark_lb.setText(str(score))
    #
    #         # main_iqa_pane.start_mark_btn.setEnabled(True)




    # 信号的连接
    # main_iqa_pane.nr_iqa_algorithm_signal.connect(caculate_nr_iqa_mark)
    start_choice_pane.jumpfrom_start_to_mainexp_signal.connect(jump_to_mainexp)
    main_iqa_pane.start_a_batch_nr_pane_signal.connect(start_batch_nr_thread)
    batch_nr_pane.finish_this_batch_signal.connect(finish_this_nr_batch)



    start_choice_pane.show()

    sys.exit(app.exec_())