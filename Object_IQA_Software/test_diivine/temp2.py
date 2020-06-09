import cv2
import numpy as np
import scipy.io as scio
import time
from scipy.special import gamma



class BIQI(object):

    def __init__(self, img_path):
        data = scio.loadmat('niqe_modelparameters.mat')
        # print(data)
        self.block_size_row = 96
        self.block_size_col = 96
        self.cov_prisparam = data['cov_prisparam']
        self.mu_prisparam = data['mu_prisparam']
        np.asarray(self.cov_prisparam, 'float32')
        np.asarray(self.mu_prisparam, 'float32')
        self.img = cv2.imdecode(np.fromfile(img_path, dtype=np.uint8), cv2.IMREAD_GRAYSCALE)
        # print(self.mu_prisparam)
        # print(self.cov_prisparam)

    def compute_quality(self, block_row_overlap=0, block_color_overlap=0,
                        mu_prisparam=0, cov_prisparam=0):
        img = self.img
        block_size_row = self.block_size_row
        block_size_col = self.block_size_col
        # img = img.astype(np.float32)
        feat_num = 18

        size = img.shape
        print('原始尺寸', size)
        block_rownum = size[0] // block_size_row
        block_colnum = size[1] // block_size_col

        # img = cv2.resize(img, (block_colnum*block_size_col, block_rownum*block_size_row), cv2.INTER_NEAREST)  # 个人感觉应该用resize，而不是直接截取
        img = img[0:(block_rownum*block_size_row),0:(block_colnum*block_size_col)]
        size = img.shape
        print('修正后尺寸', size)

        scalenum = 2
        img = img.astype('float64')
        img = img
        gblur = cv2.getGaussianKernel(7, 7 / 6) * np.transpose(cv2.getGaussianKernel(7, 7 / 6))

        for itr_num in range(1, scalenum+1):
            size =img.shape
            block_size_row = block_size_row/itr_num
            block_size_col = block_size_col/itr_num
            mu  =  cv2.filter2D(img, -1, gblur, borderType=cv2.BORDER_REPLICATE)
            # mu = cv2.GaussianBlur(img, (7,7), 7/6)
            mu_sq = mu ** 2
            sigma = np.sqrt(np.abs(cv2.filter2D(img**2, -1, gblur, borderType=cv2.BORDER_REPLICATE) - mu_sq))
            struct_dis = (img - mu) / (sigma + 1)

            feat_scale = self.blockproc(struct_dis,
                                        int(size[0]/block_size_row),
                                        int(size[1]/block_size_col),
                                        int(block_size_row),
                                        int(block_size_col))

            if itr_num==1:

                img = cv2.resize(img, (int(size[1] / 2), int(size[0] / 2)), cv2.INTER_NEAREST)
                feat = feat_scale
                self.feat_1 = feat

            else:
                feat = np.hstack((feat, feat_scale))
                self.feat_2 = feat_scale
                self.feat = feat
            # print(feat.shape)

        # print(feat)
        mu_distparam = np.nanmean(feat, axis=0)
        cov_distparam = np.cov(feat.T)

        # print(cov_prisparam, self.cov_prisparam)
        invcov_param = np.linalg.pinv((self.cov_prisparam+cov_distparam)/2)   # 求伪逆
        part1 = self.mu_prisparam-mu_distparam.T
        part2 = invcov_param
        part3 = np.transpose(self.mu_prisparam-mu_distparam.T)
        quality = np.sqrt(np.dot(np.dot(part1, part2),part3))   #也即part1 * part2 * part3

        return quality[0][0]


    def compute_mean(self, vec):
        return np.mean(vec)


    def compute_feature(self, vec):
        # Input - MSCn coefficients
        # Output - Compute the 18 dimensional feature vector

        [alpha, betal, betar] = self.estimate_AGGD_parameters(vec, is_add_meanparam=False)
        feat1_2 = [alpha, (betal+betar)/2 ]
        H = vec * np.roll(vec, 1, axis=1)
        V = vec * np.roll(vec, 1, axis=0)
        D1 = vec * np.roll(np.roll(vec, 1, axis=1), 1, axis=0)
        D2 = vec * np.roll(np.roll(vec, -1, axis=1), -1, axis=0)
        feat3_6 = self.estimate_AGGD_parameters(H, True)
        feat7_10 = self.estimate_AGGD_parameters(V, True)
        feat11_14 = self.estimate_AGGD_parameters(D1, True)
        feat15_18 = self.estimate_AGGD_parameters(D2, True)

        all_feat = feat1_2 + feat3_6 + feat7_10 + feat11_14 + feat15_18
        return all_feat


    def estimate_AGGD_parameters(self, vec, is_add_meanparam):

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

        betal = sigma_l * np.sqrt(  gamma(1/alpha_param) / gamma(3/alpha_param) )
        betar = sigma_r * np.sqrt(  gamma(1/alpha_param) / gamma(3/alpha_param) )

        if is_add_meanparam == False:
            return [alpha_param, betal, betar]
        else:
            meanparam = (betar - betal) * (gamma(2 / alpha_param) / gamma(1 / alpha_param))
            return [alpha_param, meanparam, betal, betar]


    def blockproc(self,vec, row, col, blk_row, blk_col):
        all_feat = []

        # 按96*96的块运算，并拼接，模拟matlab的blockpro函数
        for cur_col in range(col):
            for cur_row in range(row):
                curr = vec[(cur_row * blk_row) : ((cur_row + 1) * blk_row),
                           (cur_col * blk_col) : ((cur_col + 1) * blk_col)]

                block_feat = self.compute_feature(curr)
                # curr_feat = np.array(block_feat)
                # print(block_feat)

                for feat in block_feat:
                    all_feat.append(feat)


        all_feat_2_np = np.array(all_feat)
        all_feat_2_np.astype('float32')
        all_feat_2_np = all_feat_2_np.reshape(col*row, 18)


        return all_feat_2_np



if __name__ == '__main__':

    t1 = time.time()
    img_path = r'image1.bmp'
    a = BIQI(img_path)
    print(a.compute_quality())
    t2 = time.time() - t1
    print('用时：', t2, 's')




