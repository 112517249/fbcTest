# 存放全局变量,公有的配置函数或者类
import logging
import os
from logging import handlers
# 当前项目父级目录
BASR_DIR = os.path.dirname(os.path.abspath(__file__))
TOKEN=""
# 定义初始化日志配置的函数:初始化日志的输出路
def init_logging():
    # 创建日志器
    logger = logging.getLogger()
    # 设置日志等级
    logger.setLevel(logging.INFO)
    # 创建处理器,通过处理控制日志的打印
    # 创建控制台处理器
    sh = logging.StreamHandler()
    # 创建文件处理器when='S',interval=10两次运行间隔时间超10秒会拆分日志,backupCount 保留日志文件数量
    fh =logging.handlers.TimedRotatingFileHandler(BASR_DIR+"/log/fbc.log",when='S',interval=10,backupCount=3,encoding='utf-8')
    # 设置日志格式
    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    # 创建格式化器
    formatter = logging.Formatter(fmt)
    # 将格式化器添加到处理器中
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)
    # 将处理器添加到日志器中
    logger.addHandler(sh)
    logger.addHandler(fh)

    # 可以返回logger,用logger打印
    # return logger
if __name__ == '__main__':
    # 初始化日成配置时,由于没有返回日志器,所以这个配置函数中的全部配置都会配置到logging的root节点
    # logger = init_logging()
    init_logging()
    # 既然初始化到了root节点,可以直接使用logging模块打印日志
    logging.info("测试日志打印")
    # logger.info("测试日志打印")