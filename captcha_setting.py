# -*- coding: UTF-8 -*-
import os
# 验证码中的字符
NUMBER = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

ALL_CHAR_SET = NUMBER + ALPHABET
ALL_CHAR_SET_LEN = len(ALL_CHAR_SET) #10+26 = 36
MAX_CAPTCHA = 4

# 图像大小
# IMAGE_HEIGHT = 60
# IMAGE_WIDTH = 100
IMAGE_HEIGHT = 24
IMAGE_WIDTH = 80

TRAIN_DATASET_PATH = 'sample' + os.path.sep + 'my_train'
TEST_DATASET_PATH = 'sample' + os.path.sep + 'test'
PREDICT_DATASET_PATH = 'sample' + os.path.sep + 'predict'