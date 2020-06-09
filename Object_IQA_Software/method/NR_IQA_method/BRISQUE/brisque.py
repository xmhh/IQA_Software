import cv2
import numpy as np
import os
import time
from scipy.special import gamma


class BRISQUE(object):

    def __init__(self, img_path):
        t0 = time.time()
        self.img_path = img_path
        self.img = cv2.imdecode(np.fromfile(self.img_path, dtype=np.uint8), cv2.IMREAD_GRAYSCALE)
        self.imsize = self.img.shape
        t1 = time.time()
        print("第一次读取需要：", t1 - t0, "s")

        t0 = time.time()
        self.feat = self.brisque_feature(self.img)
        t1 = time.time()
        print("第一次计算feat：", t1 - t0, "s")
        # 下采样
        # 最后发现python和matlab的feat不一样，那是因为matlab下采样时默认采用锐化算法，你只要把imresize中抗锯齿属性关掉即可，即antialiasing置为false
        t0 = time.time()
        self.under_img = cv2.resize(self.img, (int(self.imsize[1] / 2), int(self.imsize[0] / 2)), cv2.INTER_NEAREST)
        t1 = time.time()
        print("第二次读取需要：", t1 - t0, "s")

        t0 = time.time()
        self.feat = self.feat + self.brisque_feature(self.under_img)
        t1 = time.time()
        print("第二次计算feat：", t1 - t0, "s")
        t0 = time.time()
        fid = open('brisque_ind', 'w')
        fid.write('1 ')
        for kk in range(len(self.feat)):
            fid.write("{:d}:{:6f} ".format(kk + 1, self.feat[kk]))
        fid.write('\n')
        fid.close()
        t1 = time.time()
        print("记录feat：", t1 - t0, "s")

        t0 = time.time()
        os.system(r'svm-scale -r brisque_range brisque_ind >> brisque_ind_scaled')
        os.system(r'svm-predict -b 1 brisque_ind_scaled brisque_model brisque_output >>brisque_dump')

        os.remove('brisque_ind')
        os.remove('brisque_ind_scaled')
        os.remove('brisque_dump')

        t1 = time.time()
        print("svm-predict：", t1 -t0, "s")

    # 产生二维高斯核函数  滤波器模板
    def gaussian_2d_kernel(self, kernel_size, sigma):
        kernel = np.zeros((kernel_size, kernel_size))
        center = kernel_size // 2
        if sigma == 0:
            sigma = ((kernel_size - 1) * 0.5 - 1) * 0.3 + 0.8
        s = 2 * (sigma ** 2)
        sum_val = 0
        for i in range(0, kernel_size):
            for j in range(0, kernel_size):
                x = i - center
                y = j - center
                kernel[i, j] = np.exp(-(x ** 2 + y ** 2) / s)
                sum_val += kernel[i, j]
        # 归一化
        sum_val = 1 / sum_val
        return kernel * sum_val
    # 卷积操作
    def correlation(self, img, kernal):

        kernal_heigh = kernal.shape[0]
        kernal_width = kernal.shape[1]
        h = kernal_heigh // 2
        w = kernal_width // 2
        # 边界补全
        img = np.pad(img, ((h, h), (w, w)), 'constant')   # 零方向填充h，1方向填充w

        # 卷积区域，也即原图像部分，用np初始化，之后卷积填值
        cor_heigh = img.shape[0] - kernal_heigh + 1
        cor_width = img.shape[1] - kernal_width + 1
        result = np.zeros((cor_heigh, cor_width), dtype=np.float64)
        for i in range(cor_heigh):
            for j in range(cor_width):
                result[i][j] = (img[i:i + kernal_heigh, j:j + kernal_width] * kernal).sum()
        return result

    def estimate_GGD_parameters(self, vec):
        gam = np.arange(0.2, 10.0, 0.001)  # 产生候选的γ
        r_gam = (gamma(1 / gam) * gamma(3 / gam)) / ((gamma(2 / gam)) ** 2)  # 根据候选的γ计算r(γ)
        sigma_sq = np.mean((vec) ** 2)
        sigma = np.sqrt(sigma_sq)  # 方差估计
        E = np.mean(np.abs(vec))
        r = sigma_sq / (E ** 2)  # 根据sigma和E计算r(γ)
        diff = np.abs(r - r_gam)
        gamma_param = gam[np.argmin(diff, axis=0)]

        return [gamma_param, sigma_sq]

    def estimate_AGGD_parameters(self, vec):
        alpha = np.arange(0.2, 10.0, 0.001)  # 产生候选的α
        r_alpha = ((gamma(2 / alpha)) ** 2) / (gamma(1 / alpha) * gamma(3 / alpha))  # 根据候选的γ计算r(α)
        sigma_l = np.sqrt(np.mean(vec[vec < 0] ** 2))
        sigma_r = np.sqrt(np.mean(vec[vec > 0] ** 2))
        gamma_ = sigma_l / sigma_r
        u2 = np.mean(vec ** 2)
        m1 = np.mean(np.abs(vec))
        r_ = m1 ** 2 / u2
        R_ = r_ * (gamma_ ** 3 + 1) * (gamma_ + 1) / ((gamma_ ** 2 + 1) ** 2)
        diff = (R_ - r_alpha) ** 2
        alpha_param = alpha[np.argmin(diff, axis=0)]
        const1 = np.sqrt(gamma(1 / alpha_param) / gamma(3 / alpha_param))
        const2 = gamma(2 / alpha_param) / gamma(1 / alpha_param)
        eta = (sigma_r - sigma_l) * const1 * const2
        return [alpha_param, eta, sigma_l ** 2, sigma_r ** 2]

    def brisque_feature(self, dis_image):

        dis_image = dis_image.astype(np.float32)  # 类型转换十分重要
        # kernal = self.gaussian_2d_kernel(7, 7 / 6)
        # ux = self.correlation(dis_image, kernal)
        gblur = cv2.getGaussianKernel(7, 7 / 6) * np.transpose(cv2.getGaussianKernel(7, 7 / 6))
        ux = cv2.filter2D(dis_image, -1, gblur, cv2.BORDER_REPLICATE)
        ux_sq = ux * ux
        sigma = np.sqrt(np.abs(cv2.filter2D(dis_image **2, -1, gblur, cv2.BORDER_REPLICATE) - ux_sq))
        mscn = (dis_image - ux) / (1 + sigma)
        f1_2 = self.estimate_GGD_parameters(mscn)
        H = mscn * np.roll(mscn, 1, axis=1)
        V = mscn * np.roll(mscn, 1, axis=0)
        D1 = mscn * np.roll(np.roll(mscn, 1, axis=1), 1, axis=0)
        D2 = mscn * np.roll(np.roll(mscn, -1, axis=1), -1, axis=0)
        f3_6 = self.estimate_AGGD_parameters(H)
        f7_10 = self.estimate_AGGD_parameters(V)
        f11_14 = self.estimate_AGGD_parameters(D1)
        f15_18 = self.estimate_AGGD_parameters(D2)
        return f1_2 + f3_6 + f7_10 + f11_14 + f15_18

    def return_mark(self):
        f = open('brisque_output')
        score = ''
        for line in f.readlines():
            score = line
        f.close()
        os.remove('brisque_output')
        return score

if __name__ == '__main__':
    time1 = time.time()
    a = BRISQUE('lena256.jpg')
    time2 = time.time()
    print('总共：', time2 - time1, 's')
    a.return_mark()



