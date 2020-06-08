# 导包
import unittest
from script.login_params import TestLogin
import os,time
# 测试套件
suite = unittest.TestSuite()
# 测试用例添加到测试套件
suite.addTest(unittest.makeSuite(TestLogin))
# 定义报告名称
report_path = os.path.dirname(os.path.abspath(__file__))+"/report/fbc{}.html".format(time.strftime('%Y%m%d %H%M%S'))
# 打开报告
with open(report_path,mode='wb') as f:
    #初始化HTMLTestRunner_PY3
    from HTMLTestRunner_PY3 import HTMLTestRunner
    runner = HTMLTestRunner(f,verbosity=2,title="FBC接口测试报告",description="自动化测试")
    # 运行测试套件
    runner.run(suite)
