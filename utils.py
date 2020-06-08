# 自定义工具类
# 封装通用断言
import os

import pymysql,json

def assert_common_utils(self,response,http_code,statusCode):
    self.assertEqual(http_code,response.status_code)
    self.assertEqual(statusCode,response.json().get("statusCode"))



class DBUtils:
    #初始化类时,要运行的代码
    def __init__(self,host="192.168.1.139", user='root', password='123456',
                               database='online_trade_server'):
        self.host=host
        self.user=user
        self.password=password
        self.database=database

    # 代表使用with语法时,进入函数时会先运行enter的代码
    def __enter__(self):
        self.conn =pymysql.connect(host=self.host,user=self.user,password=self.password,database=self.database)
        # 获取游标
        self.cursor =self.conn.cursor()
        return self.cursor
    # 退出with语句块时,会运行exit的代码
    def __exit__(self, exc_type, exc_val, exc_tb):
        # 关闭游标,关闭连接
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()

    # 读取数据文件
def read_login_data():
        # 定义数据文件路径
        login_data_path = os.path.dirname(os.path.abspath(__file__))+"/data/login.json"
        # 读取数据文件
        with open(login_data_path,mode='r',encoding='utf-8') as f:
            jsonData = json.load(f)
            # 定义result_list用于存放读取的数据
            reselt_list = []
            # 遍历json数据
            for case_data in jsonData:
                mobile =case_data.get('mobile')
                password = case_data.get('password')
                way = case_data.get('way')
                http_code = case_data.get('http_code')
                statusCode = case_data.get('statusCode')

                reselt_list.append((mobile,password,way,http_code,statusCode))
                # reselt_list.append(tuple(case_data.values()))

        print("读取的数据:",reselt_list)
        return reselt_list
if __name__ =='__main__':
    read_login_data()