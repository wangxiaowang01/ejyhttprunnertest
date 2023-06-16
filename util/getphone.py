# -*- coding:utf-8 -*-
import random


def get_phone():
    # 随机生成电话号码的前缀
    prefix = random.choice(
        ['131', '132', '133', '135', '189', '151', '152', '153', '155', '156', '157', '158', '159'])
    suffix = ''.join(random.choice(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']) for _ in range(9))
    # 将前缀和后缀组合起来，生成电话号
    return prefix + suffix


class GetPhone:
    pass
if __name__ == '__main__':
    G = GetPhone
    print(get_phone())

