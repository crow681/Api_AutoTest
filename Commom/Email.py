# coding:utf-8
"""
使用QQ邮箱发送带测试报告的邮件
"""
import logging
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr
from email.header import Header
from email.mime.application import MIMEApplication

import yaml

from Commom.Log import Mylogging


def mail():
    log = Mylogging()  # 初始化日志
    paml_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    with open(f'{paml_path}/Config/parm.yaml', 'r', encoding='utf-8') as file:
        data = yaml.safe_load(file)
        my_sender = data['mail']['sender']
        my_pass = data['mail']['pass']
        my_user = data['mail']['user']

    msg = MIMEMultipart()  # 创建附件实例
    msg['From'] = formataddr(['溺水的鱼', my_sender])  # 发件人昵称，邮箱
    msg['To'] = formataddr(['wang-jun', my_user])  # 收件人昵称，邮箱
    subject = '邮件附件测试'
    msg['Subject'] = Header(subject, 'utf-8')  # 邮件标题

    msg.attach(MIMEText('接口自动化测试报告', 'plain', 'utf-8'))  # 正文

    # 构造附件，附件路径
    report_zip = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '\测试报告.zip'

    att = MIMEApplication(open(f'{report_zip}', 'rb').read())
    att["Content-Type"] = "application/octet-stream"
    # att["Content-Disposition"] = 'attachment; filename="测试报告"'
    att.add_header('Content-Disposition', 'attachment', filename='测试报告.zip')
    msg.attach(att)

    try:
        with smtplib.SMTP_SSL(host='smtp.qq.com', port=465) as server:
            server.login(my_sender, my_pass)
            server.sendmail(my_sender, [my_user, ], msg.as_string())  # 发送邮件
            log.debug('测试报告邮件发送成功！')
    except Exception as e:
        logging.exception('邮件发送失败', e)


if __name__ == "__main__":
    # mail()
    paml_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(paml_path)



