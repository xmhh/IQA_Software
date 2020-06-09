import matlab
from matlab import engine
import time
import numpy as np
import cv2
import scipy.io as sio
import os

def niqe_score(img_path, eng):
    t1 =time.time()
    # 启动matlab引擎
    engine = eng
    t2 = time.time()
    print('启动用时',t2- t1)

    # 读入图片
    img =  cv2.imdecode(np.fromfile(img_path, dtype=np.uint8), cv2.IMREAD_GRAYSCALE)
    sio.savemat('img.mat', {'img':img})
    t3 = time.time()
    print('加载时间', t3 - t2)

    # 评价
    score = engine.computequality()
    t4= time.time()
    print('计算时间', t4 - t3)
    os.remove('img.mat')
    return score

if __name__ == '__main__':
    img_path = 'b-2-1.jpg'
    eng = matlab.engine.start_matlab()
    score = niqe_score(img_path, eng=eng)
    print(score)