# -*- coding:utf-8 -*-
# 这个文件用来封装类方法名来运行httprunner
# 先导包
from httprunner.api import HttpRunner
import os

# 继承运行的类， 设置runner变量用等号接收
runner = HttpRunner(failfast=False)

# 用类runner点run（"yml路径"）运行对应的yml文件测试套件或者测试用例
# 测试一下webhook有没有用啊


runner.run('testsuites/demo_testsuite_c.yml')  # 这条是运行调试一下，


os.system('chcp 65001')
# resull = os.system(r"dir")
ss = "woshi是啊啊"
# print(resull)
cmd = "hrun .\\testsuites\demo_testsuite_c.yml --log-level debug"
# os.system(cmd)  # 这里是运行系统开局报告的命令
