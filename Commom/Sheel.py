# coding:utf-8
"""
封装shell语法，使用命令行执行pytest命令及生成报告
"""

import subprocess as sub
from Commom.Log import Mylogging

class Shell:
    Mylogging()
    @staticmethod
    def invoke(cmd):
        proc = sub.Popen(args=cmd, shell=True)
        outdata = proc.communicate()
        return outdata


if __name__ == '__main__':
    Mylogging()
    s = Shell()
    cmd = 'java -version'

    r = s.invoke(cmd)









