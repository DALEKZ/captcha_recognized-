# -*- coding: UTF-8 -*-
import torch
import torch.nn as nn
from torch.autograd import Variable
import numpy as np
import captcha_setting
import my_dataset
from cnn_model import CNN

num_epochs =  35    #30
batch_size = 70     #70
learning_rate = 0.001

def main():
    cnn = CNN()
    cnn.train()
    print('init net')
    criterion = nn.MultiLabelSoftMarginLoss()   #损失函数
    optimizer = torch.optim.Adam(cnn.parameters(), lr=learning_rate)    #优化算法

    train_dataloader = my_dataset.get_train_data_loader()
    for epoch in range(num_epochs):
        for i, (images, labels) in enumerate(train_dataloader):
            images = Variable(images)
            labels = Variable(labels.float())
            predict_labels = cnn(images)
            loss = criterion(predict_labels, labels)
            optimizer.zero_grad()       #梯度置零，也就是把loss关于weight的导数变成0.
            loss.backward()
            optimizer.step()
            if (i+1) % 10 == 0:
                print("epoch:", epoch, "step:", i, "loss:", loss.item())
            if (i+1) % 100 == 0:
                torch.save(cnn.state_dict(), "model/2000_model.pkl")
                print("保存模型")
        print("epoch:", epoch, "step:", i, "loss:", loss.item())
    torch.save(cnn.state_dict(), "model/2000_model.pkl")
    print("保存最后模型 ")


if __name__ == '__main__':
    main()


