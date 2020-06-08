import unittest,logging
from api.login_api import LoginApi
from utils import assert_common_utils, read_login_data
from parameterized.parameterized import parameterized
class TestLogin(unittest.TestCase):
    # 初始化
    def setUp(self) -> None:
        # LoginApi
        self.login_api = LoginApi()


    def tearDown(self) -> None:
        pass

    # 测试参数化登录
    @parameterized.expand(read_login_data)
    def test01_login(self,mobile,password,way,http_code,statusCode):
        response = self.login_api.login(mobile,password,way)
        logging.info("参数登录结果为:{}".format(response.json()))
        # 断言登录结果
        assert_common_utils(self,response,http_code,statusCode)
