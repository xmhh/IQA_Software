import cv2
import numpy as np
import scipy.io as scio
import time
import pywt
from scipy.special import gamma



class CPBD(object):

    def __init__(self):
        img_path = r'image1.bmp'
        self.img = cv2.imdecode(np.fromfile(img_path, dtype=np.uint8), cv2.IMREAD_GRAYSCALE)

    def cpbd_compute(self, img):
        # 定义常量
        num_or = 6
        num_scales = 2


        gam = np.arange(0.2, 10, 0.001)
        r_gam = gamma(1/gam) * gamma(3/gam) / (gamma(2/gam) ** 2)

        img = img.astype('float32')

        size = img.shape
        # threshold to characterize blocks as edge / non - edge blocks
        threshold = 0.002
        # fitting param
        beta = 3.6
        # block size
        rb = 64
        rc = 64
        # maximum block indices
        max_blk_row_idx = size[0] // rb
        max_blk_col_idx = size[1] // rc

        widthjnb = np.hstack((np.ones((1, 51)) * 5, 3 * np.ones((1, 205))))

        total_num_edges = 0
        hist_pblur = np.zeros((1, 101))
        cum_hist = np.zeros((1, 101))

        input_image_canny_edge = cv2.Canny(img)
        input_image_sobel_edge = cv2.Sobel(img, -1, dx=0, dy=1)

        width = self.marziliano_method(input_image_sobel_edge, img)

        for i in range(max_blk_row_idx):
            for j in range(max_blk_col_idx):

                decision = self.get_edge_blk_decision(input_image_sobel_edge[rb*(i-1):rb*i-1, rc*(j-1):rc:j-1], threshold)

                if decision == 1:
                    local_width = width[rb*(i-1):rb*i-1, rc*(j-1):rc:j-1]
                    local_width = local_width[local_width != 0]

                    blk_contrast = blkproc()  # ??????????????
                    blk_jnb = widthjnb[blk_contrast]

                    prob_blur_detection = 1 - np.exp(-np.abs(local_width/blk_jnb)*beta)

                    for k in range(size[0]*size[1]):
                        temp_index = np.round(prob_blur_detection[k]*100)+1
                        hist_pblur[temp_index] = hist_pblur[temp_index] + 1
                        total_num_edges += 1

        if total_num_edges !=0:
            hist_pblur /= total_num_edges
        else:
            hszie = hist_pblur.shape
            hist_pblur = np.zeros(shape=hszie)

        sharpness_metric = np.sum(hist_pblur[:63])

    def marziliano_method(self, E, A):
        # 初始化边缘map
        edge_with_map = np.zeros(A.shape, 'float32')
        A = A.astype('float32')

        # 求A的梯度
        Gx, Gy = np.gradient(A)

        # 初始化edges
        angle_A = np.zeros(A.shape, 'float32')

        # 计算边缘的角度
        for i in range(A.shape[0]):
            for j in range(A.shape[1]):
                if Gx[i][j] != 0:
                    angle_A[i][j] = np.arctan2(Gy[i][j], Gx[i][j]) * (180 / np.pi)

                if Gx[i][j] == 0 and Gy[i][j] == 0:
                    angle_A[i][j] = 0

                if Gx[i][j] <= 1e-6 and (Gy[i][j] - np.pi / 2) <= 1e-6:
                    angle_A[i][j] = 90

        # 四舍五入angle
        angle_Arnd = 45 * np.round(angle_A / 45)  # 返回浮点数的四舍五入值
        for i in angle_Arnd:
            print(i)

        count = 0
        for m in range(1, A.shape[0] - 1):
            for n in range(1, A.shape[1] - 1):
                if E[m][n] == 1:

                    # 如果 gradient angle = 108/-180
                    if angle_Arnd[m][n] == 180 or angle_Arnd[m][n] == -180:
                        count += 1
                        for k in range(101):
                            posy1 = n - 1 - k
                            posy2 = n - 2 - k
                            if posy2 <= 0:
                                break

                            if (A[m][posy2] - A[m][posy1]) <= 0:
                                break

                        width_count_side1 = k + 1

                        for k in range(101):
                            negy1 = n + 1 + k
                            negy2 = n + 2 + k
                            if negy2 >= A.shape[1] - 1:
                                break
                            if (A[m][negy2] - A[m][negy1]) >= 0:
                                break
                        width_count_side2 = k + 1

                        edge_with_map[m][n] = width_count_side1 + width_count_side2

                    # 如果 gradient angle = 0
                    if angle_Arnd[m][n] == 0:
                        count += 1
                        for k in range(101):
                            posy1 = n + 1 + k
                            posy2 = n + 2 + k
                            if posy2 >= A.shape[1] - 1:
                                break

                            if (A[m][posy2] - A[m][posy1]) <= 0:
                                break

                        width_count_side1 = k + 1

                        for k in range(101):
                            negy1 = n - 1 - k
                            negy2 = n - 2 - k
                            if negy2 <= 0:
                                break
                            if (A[m][negy2] - A[m][negy1]) >= 0:
                                break
                        width_count_side2 = k + 1

                        edge_with_map[m][n] = width_count_side1 + width_count_side2


    def get_edge_blk_decision(self, img_in, T):
        # 判断block是不是边缘
        size = img_in.shape
        L = size[0] * size[1]
        img_edge_pixels = np.sum(img)

        return  img_edge_pixels > (L*T)


    def get_contrast_block(self):
        img = self.img
        return np.max(img) - np.min(img)




if __name__ == '__main__':

    t1 = time.time()
    img_path = r'lena256.jpg'
    img = cv2.imdecode(np.fromfile(img_path, dtype=np.uint8), cv2.IMREAD_GRAYSCALE)
    # a = CPBD()
    # A = np.zeros(img.shape, 'float32')
    # print(A)
    # print(np.gradient(img))
    # print()
    widthjnb = np.hstack((np.ones((2, 2)) * 5, 3 * np.ones((2, 3))))
    print(widthjnb)

    t2 = time.time() - t1
    print('用时：', t2, 's')




