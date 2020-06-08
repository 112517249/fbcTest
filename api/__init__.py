# 初始化日志配置的代码应该在api,__init__.py中,后续所有的接口测试操作都会通过script脚本运行,
# 而script脚本会调用api中封装的接口,每次调用api的接口时,会都先运行api模块下的__init__.py文件,
# 从而利用这个机制自动地对日志进行初始化操作
# 初始化后 ,只要是在调用api后的代码,都能用logging打印日志
import app
import logging
# 初始化日志
app.init_logging()

# 测试
logging.info("测试日志")

