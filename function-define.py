#! /usr/bin/env ptyhon
#  -*- coding: utf-8 -*-
def test(x):
    if not isinstance(x, (int, float)):
        raise  TypeError('bad operand type')
    if x >= 0:
        return  x
    else:
        return -x
'''
如果想定义一个空函数，当前还不知道函数用来做什么，可做占位符，加pass，让程序可正常运行
def test(x):
    pass
'''
print(test(555))