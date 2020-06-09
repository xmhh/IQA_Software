from Start_Pane import StartPane
from Get_Info_Pane import GetInfoPane
from Warmup_Exp_Pane import WarmupExpPane
from Main_Exp_Pro_Pane import MainExpProPane
from Setting_Pane import Settings_Pane
from DIY_Pho_Size import DIYPhoSizePane
from PyQt5.Qt import *

import json


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    # 控制面板的创建
    start_pane = StartPane()
    get_info_pane = GetInfoPane()
    warmup_exp_pane = WarmupExpPane()
    main_exp_pane = MainExpProPane()
    settings_pane = Settings_Pane()
    diy_pho_size_pane = DIYPhoSizePane()
    # 设置信息
    configure = 0



    # 槽函数
    def Jumpfrom_start_to_getinfo():
        start_pane.close()
        get_info_pane.show()

    def Jumpfrom_getinfo_to_start():
        get_info_pane.close()
        start_pane.show()

    def Jumpfrom_getinfo_to_warmup():
        get_info_pane.close()
        warmup_exp_pane.show()

    def Jumpfrom_warmup_to_getinfo():
        warmup_exp_pane.close()
        get_info_pane.show()

    def Jumpfrom_warmup_to_mainxep():
        warmup_exp_pane.close()
        main_exp_pane.show()
        main_exp_pane.help_tips_pane.wizard.show()
        main_exp_pane.refresh_settings()
        main_exp_pane.GT_pho_pane.show()



    def Jump_to_settings(item):
        settings_pane.show()
        settings_pane.goto_exact_body(item)

    def Refresh_exp_settings():
        main_exp_pane.refresh_settings()

    def Set_constrain_of_phoszie():
        max_size = int(main_exp_pane.display_widget.width() *0.85)
        diy_pho_size_pane.set_constrain(max_size)
        diy_pho_size_pane.show()

    def set_diy_pho_size():
        with open("./settings/configure.json", "r", encoding='UTF-8') as f:
            global configure
            configure = json.load(f)
        f.close()
        size_pair = configure['PhotoDis']['PhotoSize']['TestSize']['PhoSizeDict']['1']
        # 这里只是diy_pho_size_pane变了configure，之后setting还会更新setting，因此还要把更新后的pho——size传给setting_pane的configure
        settings_pane.configure['PhotoDis']['PhotoSize']['TestSize']['PhoSizeDict']['1'] = size_pair
        size_pair = size_pair.replace(',', ' x ')
        print('目前的自定义大小：', size_pair)

        settings_pane.test_size_cbox.setItemText(1, size_pair)
        settings_pane.gt_size_cbox.setItemText(1, size_pair)




    # 信号的连接
    start_pane.jumpfrom_start_to_getinfo_signal.connect(Jumpfrom_start_to_getinfo)
    get_info_pane.jumpfrom_getinfo_to_start_signal.connect(Jumpfrom_getinfo_to_start)
    get_info_pane.jumpfrom_getinfo_to_warmup_signal.connect(Jumpfrom_getinfo_to_warmup)
    warmup_exp_pane.jumpfrom_warmup_to_getinfo_signal.connect(Jumpfrom_warmup_to_getinfo)
    warmup_exp_pane.jumpfrom_warmup_to_mainexp_signal.connect(Jumpfrom_warmup_to_mainxep)
    main_exp_pane.jump_to_settingpane_signal.connect(Jump_to_settings)
    settings_pane.refresh_pho_list_in_mainpane_signal.connect(Refresh_exp_settings)
    settings_pane.goto_diy_pho_size_signal.connect(Set_constrain_of_phoszie)
    diy_pho_size_pane.refresh_pho_size_in_mainpane_signal.connect(set_diy_pho_size)

    start_pane.show()
    # get_info_pane.show()

    sys.exit(app.exec_())