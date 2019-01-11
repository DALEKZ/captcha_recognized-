# -*- coding: UTF-8 -*-
import numpy as np
import torch
from torch.autograd import Variable
import captcha_setting
import my_dataset
from cnn_model import CNN
import one_hot_encoding

def main():
    cnn = CNN()
    cnn.eval()
    cnn.load_state_dict(torch.load('model/1500_model.pkl'))
    print("load cnn net.")

    test_dataloader = my_dataset.get_test_data_loader()

    correct = 0
    total = 0
    error = []
    true = []
    for i, (images, labels) in enumerate(test_dataloader):
        image = images
        vimage = Variable(image)
        predict_label = cnn(vimage)

        c0 = captcha_setting.ALL_CHAR_SET[np.argmax(predict_label
                                                    [0, 0:captcha_setting.ALL_CHAR_SET_LEN].data.numpy())]
        c1 = captcha_setting.ALL_CHAR_SET[np.argmax(predict_label
                                                    [0, captcha_setting.ALL_CHAR_SET_LEN:2 * captcha_setting.ALL_CHAR_SET_LEN].data.numpy())]
        c2 = captcha_setting.ALL_CHAR_SET[np.argmax(predict_label
                                                    [0, 2 * captcha_setting.ALL_CHAR_SET_LEN:3 * captcha_setting.ALL_CHAR_SET_LEN].data.numpy())]
        c3 = captcha_setting.ALL_CHAR_SET[np.argmax(predict_label
                                                    [0, 3 * captcha_setting.ALL_CHAR_SET_LEN:4 * captcha_setting.ALL_CHAR_SET_LEN].data.numpy())]
        predict_label = '%s%s%s%s' % (c0, c1, c2, c3)
        true_label = one_hot_encoding.decode(labels.numpy()[0])
        print("true_label: ",true_label)
        print("predict_lable: ",predict_label,"\n")
        total += labels.size(0)
        if(predict_label == true_label):
            correct += 1
        else:
            error.append(predict_label)
            true.append(true_label)
        if(total%200==0):
            print('测试集数量：%d， 准确率 : %f %%' % (total, 100 * correct / total))
    print('测试集数量：%d， 准确率 : %f %%' % (total, 100 * correct / total))
    print('预测错误例子：\n')
    print('正确字符：',true)
    print('错误字符：',error)


if __name__ == '__main__':
    main()


