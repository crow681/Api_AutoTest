# coding:utf-8
"""
通过接口获取验证码base64编码后解密为图片,使用ddddocr库对图片进行识别
"""
import os.path

from requests import post
from base64 import b64decode
import json

import ddddocr


class Get_code():



    def __init__(self, url: str):
        """
        :type url: str
        """
        self.url = url

    def identify_code(self):
        """
        :return:验证码数字及验证码token
        """
        ocr = ddddocr.DdddOcr()
        url = self.url
        image_abspath = os.path.abspath(os.path.join(os.getcwd(), os.pardir))

        resp = post(url, data='')
        response = resp.text  # 获取验证码接口响应字符
        code_img = json.loads(response)['resultObj']
        code_img_dict = code_img.values() # 获取值
        for value in code_img_dict:  # 取值
            if 'data' in value:  # 判断是否是编码的base64字符串
                code_b64_str = value.split('data:image/jpeg;base64,')[1]
                with open(f'{image_abspath}/Image/code_img.png', 'wb') as f:  # 将验证码base64字符串解码还原成图片
                    img = b64decode(code_b64_str)
                    f.write(img)

                with open(f'{image_abspath}/Image/code_img.png', 'rb') as f:  # 识别图片中的验证码数字
                    img_bytes = f.read()
                    code_nums = ocr.classification(img_bytes)
            else:
                code_token = value  # 取token

        return code_nums, code_token


if __name__ == '__main__':

    url = 'http://118.24.255.252/operation/verificationCode/verificationCode.do'  # 验证码接口地址
    L = Get_code(url=url)
    code_num, code_token = L.identify_code()
    print(f'验证码是：{code_num}\n验证码的Token是：{code_token}')



