# -*- coding:utf-8 -*-
import os
from configparser import ConfigParser


class ParserConf():
    """
    这个类，主要用于获取配置文件config.ini文件里面的配置文件的ip端口账户密码datebases等配置信息的，
    方便通过config.ini文件内的配置信息切换不同的数据库用于接下的数据库查询
    """
    def __init__(self, file_name='config.ini'):  # 默认传参文件名为config.ini
        """

        :param file_name:
        """
        # 定义要读取的文件 conf_path，os的路径方法dirname是当前文件夹绝对路径，加os的sep方法是斜杠\，在加file_name文件名
        self.conf_path = os.path.dirname(os.path.realpath(__file__)) + os.sep + file_name
        self.conf = ConfigParser(allow_no_value=True, delimiters='=')  # 创建ConfigParser类的实例
        self.confile = os.path.join(os.getcwd(), self.conf_path)
        if os.path.exists(self.conf_path):  # 如果文件存在
            self.conf.read(self.conf_path, encoding='utf-8')  # 则打开文件
        else:  # 如果不存在。
            print('不存在' + file_name + '文件')  # 则提示不存在

    def get_config_value_by_key(self, section='dev', key='host'):  # 传入section节点名和key键名，获得section和key
        # self.conf.read(self.confile, encoding='utf-8')
        # 获取指定的section， 指定的option的值
        if self.conf.has_option(section, key):
            return self.conf.get(section, key)
        else:
            print("没找到对应的section节点和key键下的值,请看一下是不是节点名输错了")
        # print('获取%s 节点，%s 的值为 %s' % (section, key, key_value))

    # 获取所有的section
    def get_all_sections_from_config_file(self):  # 在类里面传入文件名。获取键名和值名
        # self.conf.read(self.confile, encoding='utf-8')
        print(self.conf.sections())
        # sections = self.conf.sections()
        # return sections

    # 更新指定section, option的值
    def update_value_by_section_and_key(
            self, section_name, key, key_value):  # 重写一个节点内key的value
        # self.conf.read(self.confile, encoding='utf-8')  # 在类里里面传入文件名，方法里面传入key键名，更新所有值
        self.conf.set(section_name, key, key_value)
        self.conf.write(open(self.confile, 'w'))

    # 在类里面传入文件名，方法里面传入section节点名，获取该节点下的所有值,默认section的值是user1
    def get_section_value(self, section='user1'):
        # self.conf.read(self.confile, encoding='utf-8')
        value = self.conf.items(section)
        if self.conf.has_section(section):
            return value
        else:
            print("传入的section错误，请重新传一个")

    def get_key_from_section(self, section_name='user1'):  # 传入节点名，获取指定节点下的所有键值对,默认section的值是user1
        key = self.conf.options(section_name)
        if self.conf.has_section(section_name):
            return key
        else:
            print('传入的section错误，请重新传一个')


if __name__ == '__main__':
    # s = ParserConf("D:\demo\env\dev\config.ini").get_config_value_by_key('user1', 'host2')
    # b = ParserConf().get_key_from_section()
    # a = ParserConf().get_section_value()
    c = ParserConf().get_config_value_by_key('dev', 'host')
    # ParserConf().get_all_sections_from_config_file()

    # print(b)
    # print(a)
    print(c)
    # print(d)
