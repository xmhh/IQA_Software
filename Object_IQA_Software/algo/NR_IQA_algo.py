import matlab.engine
import biqi2
import time
import numpy as np
import cv2
import scipy.io as sio
import os


algorithm_list = ['BIQI', 'BRISQUE', 'NIQE', 'BLIINDS-Ⅱ', 'CPBD', 'DIIVINE', 'NJQA']

class NR_IQA(object):
    def __init__(self, single_pic_path=None, batch_pic_path=None):
        self.algo_name = 'BRISQUE'
        self.single_pic_path = single_pic_path
        self.batch_pic_path = batch_pic_path

    def score_back(self):
        if self.algo_name == 'BIQI':
            score = self.brisque()
            return score

    def biqi(self):
        img_path = self.single_pic_path
        t1 =time.time()
        # 启动matlab引擎
        biqi_obj = biqi2.initialize()
        t2 = time.time()
        print('启动用时',t2- t1)

        # 读入图片
        img =  cv2.imdecode(np.fromfile(img_path, dtype=np.uint8), cv2.IMREAD_GRAYSCALE)
        sio.savemat('img.mat', {'img':img})
        t3 = time.time()
        print('加载时间', t3 - t2)

        # 评价
        score = biqi_obj.biqi()
        t4= time.time()
        print('计算时间', t4 - t3)
        os.remove('img.mat')
        return score

    def briqsue(self):
        return 0

if __name__ == '__main__':
    img_path = 'lena256.jpg'
    score = NR_IQA(single_pic_path=img_path).biqi()
    print(score)