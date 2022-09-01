# coding:utf-8
import os
import pytest
from Commom.Email import mail
from Commom.Log import Mylogging
from Commom.Sheel import Shell

"""

1.使用pytest生成测试结果
2.利用测试结果生成测试报告
3.发送邮件通知

"""

if __name__ == "__main__":

    # 日志初始化
    Mylogging()

    result_path = "../Report/result/"
    report_path = "../Report/report/"
    project_abspath = os.path.dirname(os.path.abspath(__file__))
    cmd = f"allure generate {result_path} -o {report_path} --clean"

    pytest.main(['-s', '-q', f'{project_abspath}/Testcase', '--clean-alluredir', f'--alluredir={result_path}'])
    # Shell().invoke(step1)
    Shell().invoke(cmd)

    # 打包测试报告
    zip(f'{project_abspath}/测试报告.zip', f"{project_abspath}/Report")
    mail()

