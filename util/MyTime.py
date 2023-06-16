# -*- coding:utf-8 -*-
# 或许时间，学习用的文件

# 获取系统时间贡酒
# 先导包
import os
import datetime
import time


# 封装类
class RunTimeMy:
    def getTime(self, strFormat=None):
        # 按照格式获取时间
        # 定义nowTime是time的本机时间
        nowTime = time.localtime()
        # 这里定义的入参strFormat是指传入时间格式，如"%Y-%m-%d %H:%M:%S"这样
        strFormatTime = time.strftime(strFormat, nowTime)
        # 传入strFormat进来，返回strFormatTime出去。
        return strFormatTime

    """
    注意格式：大写Y是年，小写m是月，小写d是天
    大写H是时，大写M是分，大写S是秒
    注意横杠和冒号拼接
    """

    # 获取时间日期
    def getDateTime(self):
        # 这里定义的入参strFormat是指传入时间格式，如"%Y-%m-%d %H:%M:%S"这样
        return self.getTime("%Y-%m-%d %H:%M:%S")

    # 获取日期
    def getDate(self):
        return self.getTime("%Y-%m-%d")

    # 获取到秒的时间（没有横杠冒号的纯数字）
    def getNumSecondTime(self):
        return self.getTime("%Y%m%d%H%M%S")

    # 获取到小时的时间(没有横杠冒号)
    def getNumHourTime(self):
        return self.getTime("%Y%m%d%H")

    # 获取到日的日期
    def getNumDayTime(self):
        return self.getTime("%Y%m%d")

    # 带年月日时分秒的
    def getNumSecondTimezhongwen(self):
        return self.getTime("%Y{}%m{}%d{} %H{}%M{}%S{}").format("年", "月", "日", "时", "分", "秒")


if __name__ == '__main__':
    run = RunTimeMy()
    print(run.getDateTime())
    print(run.getDate())
    print(run.getNumSecondTime())
    print(run.getNumHourTime())
    print(run.getNumDayTime())
    print(run.getNumSecondTimezhongwen())
