import requests
import re
import math
import os
import time
from bs4 import BeautifulSoup
from urllib import request
import time
def get_pic():
    url = 'http://124.160.107.92:9090/GenerateIdentifyingCode.aspx?' + time.strftime('%S', time.localtime())
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
        'Cookie': 'ASP.NET_SessionId=crlwax5a5bc3cx0kya5epf4f',
        'Host': '124.160.107.92:9090',
        'Referer': 'http://124.160.107.92:9090/Index.aspx',
    }
    response = requests.get(url,headers=header).content
    return response

def main():
    for i in range(0,1000):
        source = get_pic()
        print(source)
        path = 'sample\\train'
        if not os.path.exists(path):
            os.mkdir(path)
        spath = path + '\\' + str(i) + '.jpg'
        if not os.path.exists(spath):
            with open(spath, 'wb') as f:
                f.write(source)
                f.close()
                print('ok')

if __name__ == '__main__':
    main()