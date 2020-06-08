# 导包
import unittest, logging, app
import requests
from api.fbc_api import FbcApi
import pymysql
from utils import assert_common_utils,DBUtils
# 创建测试类集成
class TestFbcDemo(unittest.TestCase):
    def setUp(self) -> None:
        # 实例化FbcApi
        self.fbc_api=FbcApi()

    def tearDown(self) -> None:
        pass

    # 创建测试函数
    def test_fbc_user(self):
        # 初始化日志(已引入api初始化日志,所以不需要再初始化)
        # app.init_logging()
        # 调用登录接口
        response = self.fbc_api.login("18598274082","19ede66f218015fd9df85ac886488926","0")
        # 打印登录结果
        logging.info("登录结果:{}".format(response.json()))
        # 取出token
        token = response.json().get('content').get('token')
        app.TOKEN = token
        logging.info("token:{}".format(token))
        logging.info("app.TOKEN为:{}".format(app.TOKEN))
        # 断言登录结果
        #self.assertEqual(200,response.status_code)
        assert_common_utils(self,response,200,0,None)
        # 断言登录errorMessage数据
        self.assertEqual(None, response.json().get("errorMessage"))
        self.assertEqual(0, response.json().get("statusCode"))

        # 连接数据库
        with DBUtils() as db:
            # 执行操作
            db.execute("select mobile from t_user where id=2179;")
            # 打印查询结果
            result = db.fetchone()
            logging.info("sql结果:{}".format(result))
            self.assertEqual("18598274082",result[0])

            # 设置headers
            headers ={"lang":"zh_CN","token":app.TOKEN}

            # 查询个人信息
            response_list = requests.post("http://192.168.1.135:8082/api/user/getUser",data={"token":app.TOKEN},headers=headers)
            # 断言查询响应状态码
            self.assertEqual(200, response_list.status_code)
            # 断言登录statusCode数据
            self.assertEqual(0, response.json().get("statusCode"))
            logging.info("getUser结果:{}".format(response_list.json()))

        # 我的资产
        response_myAssets = requests.get("http://192.168.1.135:8082/api/finance/coin/myAssets",params={"token":app.TOKEN},headers=headers)
        # 断言
        self.assertEqual(200, response_myAssets.status_code)
        self.assertEqual(0, response_list.json().get("statusCode"))
        logging.info("myAssets结果:{}".format(response_myAssets.json()))


        response_list = requests.get("http://192.168.1.135:8082/api/amount/queryAccountList",params={"token":app.TOKEN},headers=headers)
        # 断言返回数据
        self.assertEqual(0,response_list.json().get("statusCode"))
        logging.info("queryAccountList结果:{}".format(response_myAssets.json()))