#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-
# @Time    : 2022/8/11 22:42
# @Author  : wangjun
# @File    : Zipfile.py

import os
import zipfile

def zip(zippath, file_path):
    """

    :param zippath:压缩包名称路径
    :param file_path: 需要压缩的文件
    :return:
    """
    # 判断是文件还是文件夹
    if os.path.isfile(file_path):
        with zipfile.ZipFile(zippath, 'w') as zf:
            zf.write(file_path)
    else:
        with zipfile.ZipFile(zippath, 'w') as zf:
            for root, dirs, files in os.walk(file_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    zf.write(file_path)

if __name__ == '__main__':
    zip(r'../测试报告.zip', r'../Report')
