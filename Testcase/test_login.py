
from Commom.Request import Request


class Test_verificationCode:

    def test_code_get01(self):
        """
        :return:测试示例
        """
        res = Request()
        url = '……'
        get_status = res.get(url=url)
        assert get_status == 200







