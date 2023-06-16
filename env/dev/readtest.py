# -*- coding:utf-8 -*-
import configparser

cf = configparser.ConfigParser()
def read_sections1():
    cf.read("config.ini")  # read方法读取配置文件，
secs = cf.sections()  # 获取cf读的cinfig.ini里面的section（一个配置文件中可以有多个配置，如数据库相关的配置，邮箱相关的配置）
# 每个section由[]包裹，即[section])，并以列表的形式返回 其实就是获取文件内的所有数据，文件必须有一个[]形式的表头
print(secs)  # 打印结果看看

options = cf.options("user1")  # 获取某个section名为user1所对应的键   section可以理解为节点
print(options)  # 打印结果看看

items = cf.items("user1")  # 获取section里面的user1所对应的全部键值对
print(items)  # 打印结果看看

name = cf.get("user1","host")  # 查看user1这组数据里的键名为host的值
print(name)
