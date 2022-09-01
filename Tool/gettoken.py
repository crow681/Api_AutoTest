#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-
# @Time    : 2022/8/15 16:16
# @Author  : wangjun
# @File    : gettoken.py

import urllib3

from Commom.Request import Request
from getcode import Get_code
import json

def token(url):
    r = Request()
    c = Get_code('http://139.186.140.210:8200/operation/verificationCode/verificationCode.do')
    code, codetoken = c.identify_code()
    data = {
        'userId':'admin',
        'password': 'HZCiVPgKAICHC7VDbs9/rw==',
        'code':code,
        'codeToken':codetoken
    }
    tt = r.post(url=url, body=json.dumps(data))
    token = tt[5]["userToken"]
    return token

if __name__ == "__main__":
    s = token('http://139.186.140.210:8200/operation/login/login.do')
    print(s)
