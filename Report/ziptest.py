#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-
# @Time    : 2022/8/11 22:42
# @Author  : wangjun
# @File    : ziptest.py

import os
import logging
from tarfile import open

from Commom.Log import log_basic

def tar_report():
    """

    :return:打包压缩测试报告
    """
    log_basic()
    try:
        with open('../Report/测试报告', 'x:gz') as mytar:
            mytar.add('../Report')
        logging.info('测试报告已压缩完成')
    except FileExistsError:
        os.remove('../Report/测试报告')
        with open('../Report/测试报告', 'x:gz') as mytar:
            mytar.add('../Report')
        logging.info("测试报告已压缩完成")


if __name__ == '__main__':
    tar_report()

