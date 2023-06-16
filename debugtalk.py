# -*- coding:utf-8 -*-
# 六、在 debugtalk.py（必须是这里）中写一个查询数据 sql 的方法
import datetime
import time

import requests
from faker import Faker
from httprunner import __version__
from mysqlDB import MysqlDb
from util import DbStudy, getphone
import mysqlDB
from util.MyTime import RunTimeMy


#
# def sleep(n_secs):
#     time.sleep(n_secs)
#
#
# # 定义查询数据 sql 的方法 并调用
#
# mysqlDB = MysqlDb()
#
#
# def get_user_name():
#     user_name = mysqlDB.user_name()
#     return user_name[0]
#
#
# import handle_mysql
#
#
# # 查询充值前余额
# def before_recharge_amount(inver_user_id):
#     sql1 = "SELECT leave_amount FROM member WHERE id ="
#     sql2 = str(inver_user_id)
#     sql3 = ';'
#     # 拼接sql语句
#     check_sql = sql1 + sql2 + sql3
#     # 创建实例
#     sql_class = handle_mysql.HandleMysql()
#     # 调用实例类中的方法
#     mysql_data = sql_class.get_one_value(sql=check_sql)
#     sql_class.close()
#     return float(mysql_data['leave_amount'])
#
#
# # 计算充值后的余额
# def new_recharge_amount(amount, before_amount):
#     return float(amount) + float(before_amount)

def select_one_data(sql):
    """
    封装一个查询数据库一条返回数据的方法
    :param sql: sql语句
    :return: 返回一条数据，切片后的数据
    """
    #

    # s = "select * from ejy_ucs.member_coupon where member_id='2122346538';"
    k = DbStudy.DB('dev').select_one(sql=sql)[1]
    # v = DbStudy.DB('dev').select_one(sql=s)[1]
    # print("你执行的sql：语句为：", sql)
    # print("sql语句查询的结果为：", k)
    # return k
    return k


def select_one_data_str(sql=None):
    """
    封装一个查询数据库返回一条数据的方法
    :param sql: 输入sql语句，
    :return: 返回一条数据，切片后的数据，并进行str字符串转换
    """
    k = DbStudy.DB('dev').select_one(sql=sql)
    a = k[1]
    return str(a)


def select_one_data_str_test(sql=None):
    """
    封装一个查询数据库返回一条数据的方法
    :param sql: 输入sql语句，
    :return: 返回一条数据，切片后的数据，并进行str字符串转换
    """
    k = DbStudy.DB('dev').select_one(sql=sql)
    # kk = list(k)  [a]
    # for i in k:
    # i += 1
    # if i == 1:
    return k


def select_one_data_all(sql=None):
    """
    查询sql，返回全部数据
    :param sql: sql语句
    :return: 返回一条数据完整不切片
    """
    k = DbStudy.DB('dev').select_one(sql=sql)
    return k


def select_one_data_none():  # 封装一个查询数据库一条返回数据的方法
    """
    返回查询内容，sql写死
    :return:
    """

    s = "select * from ejy_ucs.member_coupon where member_id='2122346538';"
    # k = DbStudy.DB('dev').select_one(sql=sql)[1]
    v = DbStudy.DB('dev').select_one(sql=s)[1]
    # print("你执行的sql：语句为：", sql)
    # print("sql语句查询的结果为：", k)
    # return k
    return v


# 随机生成手机号
def phone():
    """
    随机生成手机号
    :return: 随机手机号
    """
    p = getphone.get_phone()
    return p


def createphone_number():
    """
    用Faker随机生成手机号码
    :return:随机生成手机号码
    """
    fake = Faker(locale='zh_CN')
    return fake.phone_number()


# 随机一个生成姓名
def createName():
    """
    随机生成一个姓名
    学习：Faker模块
    :return: 随机姓名
    """
    fake = Faker(locale='zh_CN')
    return fake.name()


def createSSN():
    """
    随机生成身份证号码
    :return: 随机身份证号码
    """
    fake = Faker(locale='zh_CN')
    return fake.ssn()


def createAddress():
    """
    随机生成一个地址
    :return:随机生成一个地址
    """
    fake = Faker(locale='zh_CN')
    return fake.address()


def createEmail():
    """
    随机生成一个电子邮箱
    :return: 随机电子邮箱
    """
    fake = Faker(locale='zh_CN')
    return fake.email()


def creatCredit_card_number():
    """
    随机生成一个信用卡号
    :return: 随机信用卡号
    """
    fakr = Faker(locale='zh_CN')
    return fakr.credit_card_number()


def createSentence():
    """
    随机生成一句话
    :return: 随机一句话
    """
    fake = Faker(locale='zh_CN')
    return fake.sentence()


# 获取时间
def get_NumSecondTime():
    """
    获取当前时间
    :return: 获取当前时间
    """
    run = RunTimeMy()
    s2 = run.getNumSecondTime()
    return s2


# 获取中文年月日时分秒的时间
def get_NumSecondTimezhongwen():
    """
    获取当前时间，带中文年月日时分秒的
    :return: 带中文年月日时分秒的
    """
    run = RunTimeMy()
    s3 = run.getNumSecondTimezhongwen()
    return s3


def getTime_H5():
    """
    获取签名里面的时间戳
    :return: 切片出来返回时间
    """
    ret = requests.get("https://dev.ejiayou.com/sign/h5/tRmFSGexZmIxVR4o/Ea8u3e23tvYD8yi3")
    time_h5 = ret.text.split('=')[1].split('&')[0]
    return time_h5


def getsign_H5():
    """
    获取签名里面的snig
    :return: 切片出来返回snig
    """
    ret = requests.get("https://dev.ejiayou.com/sign/h5/tRmFSGexZmIxVR4o/Ea8u3e23tvYD8yi3")
    sign_h5 = ret.text.split('/')
    return sign_h5


value = getsign_H5()


def forEach(key=None):
    '''

    :param key:传入一个key for循环切片出来
    :return:如果i == key 返回第一个，否则返回第二个
    '''
    for i in range(len(value)):
        if i == key:
            return value[0]
        else:
            return value[1]


def getEndTime():
    """
    获取当前时间
    :return: 当前时间年月日时分秒数字
    """
    nowTime = time.localtime()
    strFormatTime = time.strftime("%Y%m%d%H%M%S", nowTime)
    return strFormatTime


def getStartTime(intDayNum=None):
    """
    传入天数数字，进行加法运算。返回的就是2天后的日期。
    :param intDayNum: 传入天数，比如说2天。
    :return: 返回的就是2天后的日期。
    """
    now_time = datetime.datetime.now()
    return (now_time + datetime.timedelta(days=intDayNum)).strftime("%Y%m%d%H%M%S")

# TODO 封装获取redis数据的方法，还未进行
def get_redis_data():
    pass
#


# 获取当前时间戳
# def get_time():

if __name__ == '__main__':
    # print(select_one_data("select * from ejy_ucs.member_coupon where member_id='2122346538';")[1])
    s = "select * from ejy_ucs.member_coupon where member_id='2122346538';"
    d = "SELECT * FROM ensd_ocs.user_order_0 WHERE user_id='2122346538' ORDER BY create_date_time desc limit 10;"
    # print(select_one_data("select * from ejy_ucs.member_coupon where member_id='2122346538';"))
    # print(select_one_data_none())
    print(type(select_one_data_str_test(d)))
    # print(phone())
    # print(get_NumSecondTime())
    # print(get_NumSecondTimezhongwen())
    # print(createName())
    # print(createphone_number())
    # print(createSSN())
    # print(createAddress())
    # print(createEmail())
    # print(createSentence())
    # print(creatCredit_card_number())
    # print(getsign_H5())
    # print(value)
    # print(forEach())
    # print(getEndTime())
    # print(getStartTime(1))
    # print(select_one_data_none())
    # print(select_one_data_all(sql=s))
