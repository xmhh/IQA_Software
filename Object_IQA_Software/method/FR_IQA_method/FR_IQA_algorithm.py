from sewar.full_ref import *
import cv2

class FR_IQA_method(object):

    def __init__(self):
        pass

    def get_score(self, algorithm, img1_path, img2_path):
        img1 =  cv2.imdecode(np.fromfile(img1_path, dtype=np.uint8), cv2.IMREAD_GRAYSCALE)
        # img1 =  cv2.imdecode(np.fromfile(img1_path, dtype=np.uint8), cv2.INTER_BITS2)
        img2 =  cv2.imdecode(np.fromfile(img2_path, dtype=np.uint8), cv2.IMREAD_GRAYSCALE)
        # img2 =  cv2.imdecode(np.fromfile(img2_path, dtype=np.uint8), cv2.INTER_BITS2)

        algorithm_dict = {
            'MSE': mse(GT=img1, P=img2),
            'RMSE': rmse(GT=img1, P=img2),
            'PSNR': psnr(GT=img1, P=img2),
            'SSIM': ssim(GT=img1, P=img2),
            'UQI': uqi(GT=img1, P=img2),
            'MS-SSIM': msssim(GT=img1, P=img2),
            'ERGAS': ergas(GT=img1, P=img2),
            'SCC': scc(GT=img1, P=img2),
            'RASE': rase(GT=img1, P=img2),
            'SAM': sam(GT=img1, P=img2),
            'VIF_P': vifp(GT=img1, P=img2)

        }

        return algorithm_dict.get(algorithm, None)


if __name__ == '__main__':
    fr_iqa = FR_IQA_method()

    img1 = 'img1.bmp'
    img2 = 'img5.bmp'
    a = fr_iqa.get_score('VIF_P', img1, img2)
    print(a)