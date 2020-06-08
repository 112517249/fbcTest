# 导包
import requests
# 创建api类
class FbcApi:
    def __init__(self):
        pass
    # 封装登录接口
    def login(self,mobile,password,way):
        login_url = "http://192.168.1.135:8082/api/user/login"
        jsonData = {"mobile":mobile,"password":password,"way":way}
        return requests.post(login_url,data=jsonData)