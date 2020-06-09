from method.NR_IQA_method.BRISQUE.brisque import BRISQUE
from method.NR_IQA_method.NIQE.start import niqe_score
from method.NR_IQA_method.BIQI.start import biqi_score
from method.NR_IQA_method.CPBD.start import cpbd_score
from method.NR_IQA_method.BLIINDS_2.start import bliinds2_score
from method.NR_IQA_method.NJQA.start import njqa_score


algorithm_tuple = {'BIQI', 'BRISQUE', 'NIQE', 'BLIINDS_2', 'DESIQUE', 'CPBD',
                          'FISH', 'FISH_bb', 'S3', 'LPC', 'DIIVINE', 'Martziliano', 'NJQA'}


class goto_nriqa(object):

    def __init__(self):
        pass

    def run(self, algorithm_name, photo_path, eng):


        if algorithm_name == 'BRISQUE':
            score = BRISQUE(photo_path).return_mark()
            return score

        if algorithm_name == 'BIQI':
            score = biqi_score(photo_path, eng)
            return score

        if algorithm_name == 'NIQE':
            score = niqe_score(photo_path, eng)
            return score

        if algorithm_name == 'BLIINDS_2':
            # 这个图片一大速度贼慢！！！
            score = bliinds2_score(photo_path, eng)
            return score

        # if algorithm_name == 'DESIQUE':
        #     DESIQUE(photo_path).return_mark()
        #
        if algorithm_name == 'CPBD':
            score = cpbd_score(photo_path, eng)
            return score
        #
        # if algorithm_name == 'FISH':
        #     BIQI(photo_path).return_mark()
        #
        # if algorithm_name == 'FISH_bb':
        #     BIQI(photo_path).return_mark()
        #
        # if algorithm_name == 'S3':
        #     BIQI(photo_path).return_mark()
        #
        # if algorithm_name == 'LPC':
        #     BIQI(photo_path).return_mark()
        #
        # if algorithm_name == 'DIIVINE':
        #     BIQI(photo_path).return_mark()
        #
        # if algorithm_name == 'Martziliano':
        #     BIQI(photo_path).return_mark()
        #
        if algorithm_name == 'NJQA':
            score = njqa_score(photo_path, eng)
            return score















