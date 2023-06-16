# -*- coding:utf-8 -*-
# 这个文件是学习用的，学习写通过读取配置文件链接数据库，把连接数据库的基础方法放在这里
import os
import pymysql
from env.dev.ConfigParser import ParserConf


class DB:  # 创建DB类,注意创建这个类实例的时候，必须传参，传ini配置文件的节点名进来
    """
    # 创建DB类,注意创建这个类实例的时候，必须传参，传ini配置文件的节点名进来
    """
    def __init__(self, section_name):  # 创建属性
        cf = ParserConf()  # 创建ParserConf实例化

        self.host = cf.get_config_value_by_key(section_name, 'host')  # 获得配置文件里的host
        self.user = cf.get_config_value_by_key(section_name, 'user')  # 获得配置文件里的user
        self.passwd = cf.get_config_value_by_key(section_name, 'passwd')  # 获得配置文件里的passwd
        self.prot = cf.get_config_value_by_key(section_name, 'prot')  # 获得配置文件里的prot
        self.database = cf.get_config_value_by_key(section_name, 'database')  # 获取配置文件里面的database名
        self.section_name = section_name

    def connect(self):  # 创建建立连接数据库的方法
        self.db = pymysql.connect(host=self.host, port=int(self.prot), user=self.user, password=self.passwd,
                                  database=self.database, charset='utf8')  # 创建建立连接
        self.cursor = self.db.cursor()  # 创建游标cursor

    def close(self):  # 创建关闭连接的方法， 下面如果对数据库做了操作，就调一下这个方法就会关闭游标和连接
        # 关闭游标 每次调用一次这个方法就会自动执行这两个操作
        self.cursor.close()
        self.db.close()  # 关闭连接

    def select_one(self, sql):
        """
        输入一条sql 用户单条查询，不常用

        :param sql(str):传入一条sql
        :return: 如果sql正确，返回查找结果，如果错误，返回报错信息
        """
        result = 0
        try:
            self.connect()
            self.cursor.execute(sql)
            result = self.cursor.fetchone()
            self.close()
            # print("你连接的数据库host为：" + self.host)
            # print("你连接的数据库的datebase为：" + self.database)
            # print("你输入的sql语句为：", sql)
        except Exception as e:
            print("你连接的数据库host为：" + self.host)
            print("你连接的数据库的datebase为：" + self.database)
            print("你输入的sql语句为：", sql)
            print("输入的sql语句错误select error是：", e)
        return result

    def select_all(self, sql):  # 封装一个新建查询方法，返回all fetchall
        """
        输入一条sql 用户多条查询，常用

        :param sql(str): 传入一条sql
        :return: 如果sql正确，返回查找结果，如果错误，返回报错信息
        """
        result = 0
        try:
            self.connect()  # 建立连接
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            self.close()
            print("你连接的数据库host为：" + self.host)
            print("你连接的数据库的datebase为：" + self.database)
            print("你输入的sql语句为：", sql)
        except Exception as e:
            print("你连接的数据库host为：" + self.host)
            print("你连接的数据库的datebase为：" + self.database)
            print("你输入的sql语句为：", sql)
            print('打印sql语句错误select error：', e)
        return result

    def edit(self, sql=None):  # 封装回滚方法，如果sql修改、插入、删除的方法输入错了，就调用一次回滚，保证数据库安全
        """
        如果sql修改、插入、删除的方法输入错了，就调用一次回滚，保证数据库安全
        :param sql:
        :return:
        """
        result = 1
        try:
            self.connect()  # 建立连接
            self.cursor.execute(sql)
            result = self.cursor.execute(sql)
            self.db.commit()
            self.close()
            print("你连接的数据库host为：" + self.host)
            print("你连接的数据库的datebase为：" + self.database)
            print("你输入的sql语句为：", sql)
        except Exception as e:
            print("增删查的sql语句错误，报错为：", e)
            result = 0
            print("执行回滚方法，保护数据库")
            self.db.rollback()
        return result

    """_edit(self,sql) 其实就是做个判断，看看sql语句对不对，对就填进去，不对也不会影响库 下面的增删改都是基于这个方法"""

    def insert_info(self, sql=None):  # 封装新增插入方法
        """
        封装新增插入方法
        :param sql: 传入一条sql
        :return: 返回插入结果
        """
        print("你连接的数据库host为：" + self.host)
        print("你连接的数据库的datebase为：" + self.database)
        print("你输入的sql语句为：", sql)
        return self.edit(sql)

    def updata(self, sql=None):  # 封装修改数据方法
        """
        # 封装修改数据方法
        :param sql: 传入一条update的sql
        :return: 更新结果，如果sql、错误，打印报错信息
        """
        print("你连接的数据库host为：" + self.host)
        print("你连接的数据库的datebase为：" + self.database)
        print("你输入的sql语句为：", sql)
        return self.edit(sql)

    def delete(self, sql=None):  # 封装删除数据库方法，慎用
        """
        # 封装删除数据库方法，慎用
        :param sql: 传入一条update的sql
        :return: 返回删除结果，如果sql、错误，打印报错信息
        """
        print("你连接的数据库host为：" + self.host)
        print("你连接的数据库的datebase为：" + self.database)
        print("你输入的sql语句为：", sql)
        return self.edit(sql)


if __name__ == '__main__':
    t = DB('dev')
    # print(t.select_one("SELECT * from  ejy_ucs.member_coupon where member_id='103969997';"))
    # print("asdasda")
#
#     t.insert_info(sql="INSERT INTO ejy_finance.ejiayou_station_pay_mode_rel (station_id, station_name, pay_mode_id, settle_id, is_open, station_state, state, create_time, update_time, creator, updater, create_by, update_by)
# VALUES ('38289', 'Mike测试直降活动，勿动改数据', 1, '[{"isBind":1,"settleId":2}]', 1, 1, 1, now(), now(), '李强', '李强', null, null);")
