import unittest,logging
from api.login_api import LoginApi
from utils import assert_common_utils
class TestLogin(unittest.TestCase):
    #初始化
    def setUp(self) -> None:
        # LoginApi
        self.login_api = LoginApi()


    def tearDown(self) -> None:
        pass

    # 测试登录成功
    def test01_login_success(self):
        response = self.login_api.login("18598274082","19ede66f218015fd9df85ac886488926","0")
        logging.info("登录结果为:{}".format(response.json()))
        # assert_common_utils(self,response,200,0,None)
        assert_common_utils(self, response, 200, 0)
    # 测试账号不存在
    def test02_login_username_is_not_exist(self):
        response_not = self.login_api.login("18598274000","19ede66f218015fd9df85ac886488926","0")
        logging.info("not登录结果为:{}".format(response_not.json()))