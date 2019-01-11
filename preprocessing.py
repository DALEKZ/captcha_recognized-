#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 预处理

from PIL import Image
import uuid
import numpy as np
import os

root_path = 'sample/process'


# 转为灰度图
def convert2gray(img):
    img = img.convert("L")
    return img


# 二值化
def binarizing(img, threshold):
    pix_data = img.load()
    w, h = img.size
    for y in range(h):
        for x in range(w):
            if pix_data[x, y] < threshold:
                pix_data[x, y] = 0
            else:
                pix_data[x, y] = 255

    return img


# 传入二值化后的图片进行垂直投影
def vertical(img):
    pixdata = img.load()
    w, h = img.size
    result = []
    for x in range(w):
        black = 0
        for y in range(h):
            if pixdata[x, y] == 0:
                black += 1
            result.append(black)
    return result


def main():
    for img_file in os.listdir(root_path):
        path = os.path.join(root_path, img_file)
        img = Image.open(path)
        gray_img = convert2gray(img)
        bin_img = binarizing(gray_img, 145)
        bin_img.save('sample/process/' + img_file)


if __name__ == '__main__':
    main()
