import cv2
import numpy as np
import scipy.io as scio
import time
import pywt
from scipy.special import gamma



class DIIVINE(object):

    def __init__(self):
        pass

    def divine_feature_extract(self, img):
        # 定义常量
        num_or = 6
        num_scales = 2
        gam = np.arange(0.2, 10, 0.001)
        r_gam = gamma(1/gam) * gamma(3/gam) / (gamma(2/gam) ** 2)

        img = img.astype('float32')



    def divine_overall_quality(self, param):

        atrain = r




if __name__ == '__main__':

    t1 = time.time()
    img_path = r'image1.bmp'
    img = cv2.imdecode(np.fromfile(img_path, dtype=np.uint8), cv2.IMREAD_GRAYSCALE)
    a = DIIVINE()
    print(a.compute_statistics(img))
    t2 = time.time() - t1
    print('用时：', t2, 's')




