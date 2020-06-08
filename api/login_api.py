# 导包
import requests
# 创建登录api
class LoginApi:
    def __init__(self):
       self.login_url = "http://192.168.1.135:8082/api/user/login"


        # 封装登录接口
    def login(self,mobile,password,way):

        jsonData = {"mobile": mobile, "password": password, "way": way}
        return requests.post(self.login_url, data=jsonData)