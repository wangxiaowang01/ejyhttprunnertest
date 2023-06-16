# -*- coding:utf-8 -*-
# 创建读取数据库配置文件 readConfig.py
# 导入几个要用的包
import os, codecs, configparser


# 创建读取数据库的配置文件
class ReadConfig:
    """
    # 定义一个类ReadConfig（object）没有继承自谁的话括号可以去掉
    """
    def __int__(self):  # 定义一个私有方法__int__
        self.cf = configparser.ConfigParser()  # 实例化configparser对象出来给cf
        # 获取当前文件夹的父目录的绝对路径
        self.path = os.path.dirname(os.path.dirname(__file__))
        # 获取config文件内的ini文件
        self.file_path = os.path.join(self.path, 'config', 'config.ini')
        # 获取ini文件
        self.cf.read(self.file_path, encoding='utf-8')

    def Mysql(self):
        value = self.cf.get("Mysql", os.name)
        return value

    def DateBase(self, name):
        value = self.cf.get("DATEBASE", name)
        return value
