# coding:utf-8

"""
封装request
"""
import requests
import json
import yaml
import os

class Request:

    def __init__(self):
        yaml_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        with open(f'{yaml_path}/Config/parm.yaml', 'r', encoding='utf-8') as file:
            data = yaml.safe_load(file)
            self.url = 'http://{0}:{1}'.format(data['evn']['host'], data['evn']['port'])

    def get(self, url, header=None, *arg):
        """
        :param url: 接口地址
        :param header: 请求头
        :return: 状态码
        """

        res = requests.get(url=self.url + url, headers=header, *arg)
        status_code = res.status_code

        return status_code

    def post(self, url, body, header=None, *arg):
        """

        :param url: 接口地址
        :param body: 请求参数 dict
        :param header: 请求头
        :return: 响应数据，状态码
        """
        res = requests.post('POST', url=self.url + url, body=body, headers=header, *arg)
        status_code = res.status_code
        response = json.loads(res.data.decode('utf-8'))

        basePageObj = response['basePageObj']
        dataList = response['dataList']
        resultCode = response['resultCode']
        resultMsg = response['resultMsg']
        resultObj = response['resultObj']

        return status_code, basePageObj, dataList, resultCode, resultMsg, resultObj


if __name__ == "__main__":
    re = Request()
    code = re.get(url='/verificationCode.do')
    print(code)
