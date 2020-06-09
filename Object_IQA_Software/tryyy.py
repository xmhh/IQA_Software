import biqi2
import time
import numpy as np
import cv2
import scipy.io as sio
import os

img_path = 'lena256.jpg'
t2 = time.time()
biqi_obj = biqi2.initialize()

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
print(score)