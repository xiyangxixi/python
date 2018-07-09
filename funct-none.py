#! /usr/bin/env python
# -*- coding: utf-8 -*-
def add(L=None):
    if L is None:
        L = []
        L.append('HUAHUA')
        return  L
print(add())
'''
**kw 为关键字参数，在几个参数中间放一个* 为命名关键字参数
如 def test(name, age, **kw) def test(a, b, *, c, d)
'''