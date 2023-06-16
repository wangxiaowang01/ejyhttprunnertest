# -*- coding:utf-8 -*-
# 这个文件主要放学习的内容。
"""
Faker模块
自动造数据利器，Faker 了解一下？
在软件需求、开发、测试过程中，有时候需要使用一些测试数据，针对这种情况，
我们一般要么使用已有的系统数据，要么需要手动制造一些数据。
由于现在的业务系统数据多种多样，千变万化。在手动制造数据的过程中，
可能需要花费大量精力和工作量，此项工作既繁复又容易出错，
比如要构造一批用户三要素(姓名、手机号、身份证)、构造一批银行卡数据、或构造一批地址通讯录等。

这时候，人们常常为了偷懒快捷，测试数据大多数可能是类似这样子的:
测试, 1300000 000123456
张三, 1310000 000123456
李四, 1320000 000234567
王五, 1330000 000345678
测试数据中包括了大量的“测试XX”，要么就是随手在键盘上一顿乱敲，都是些无意义的假数据。

"""
from util import DbStudy

list1 = [1, 24, 34, 44, 533, 5, 219]
i = 0
for i in range(len(list1)):  # 通过下标
    i += 1
    if i == 1:
        print(list1[i])
    # else:
    #     print("没找到")
d = "SELECT * FROM ensd_ocs.user_order_0 WHERE user_id='2122346538' ORDER BY create_date_time desc limit 10;"


class test_1:
    def select_one_data_str(sql=None):
        abe = "SELECT * FROM ensd_ocs.user_order_0 WHERE user_id='2122346538' ORDER BY create_date_time desc limit 10;"

        """
        封装一个查询数据库返回一条数据的方法
        :param sql: 输入sql语句，
        :return: 返回一条数据，切片后的数据，并进行str字符串转换
        """
        k = DbStudy.DB('dev').select_one(sql=abe)
        a = list(k)
        return str(a)
if __name__ == '__main__':
    test_1.select_one_data_str()