# -*- coding: UTF-8 -*-
import os
from torch.utils.data import DataLoader, Dataset
import torchvision.transforms as transforms
from PIL import Image
import one_hot_encoding as ohe
import captcha_setting


class mydataset(Dataset):

    def __init__(self, folder, transform=None):
        self.train_image_file_paths = [os.path.join(folder, image_file) for image_file in os.listdir(folder)]
        print(self.train_image_file_paths)
        self.transform = transform

    def __len__(self):
        return len(self.train_image_file_paths)

    def __getitem__(self, idx):
        image_root = self.train_image_file_paths[idx]
        image_name = image_root.split(os.path.sep)[-1]
        image_name = image_name.split('.')[0]
        image = Image.open(image_root)
        if self.transform is not None:
            image = self.transform(image)       #to_Tensor
        label = ohe.encode(image_name)  # one hot
        return image, label


transform = transforms.Compose([
    transforms.Grayscale(),
    transforms.ToTensor(),
])


def get_train_data_loader():
    dataset = mydataset(captcha_setting.TRAIN_DATASET_PATH, transform=transform)
    return DataLoader(dataset, batch_size=50, shuffle=True)


def get_test_data_loader():
    dataset = mydataset(captcha_setting.TEST_DATASET_PATH, transform=transform)
    return DataLoader(dataset, batch_size=1, shuffle=True)


def get_predict_data_loader():
    dataset = mydataset(captcha_setting.PREDICT_DATASET_PATH, transform=transform)
    return DataLoader(dataset, batch_size=1, shuffle=True)
