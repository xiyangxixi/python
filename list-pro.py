#! /usr/bin/env python
# -*- coding: utf-8 -*-

#L = []
#for x in range(1, 11):
#    L.append(x * x)
#print(L)

#L = [x * x for x in range(1, 11)]
#print(L)
#L = [m + n for m in 'ABC' for n in 'XYZ']
#print(L)
#d = {'x': 'A', 'y': 'B', 'z': 'C' }
#print([k + '=' + v for k, v in d.items()])
L = ['Hello', 'World', 'ORACLE', 'APPle']
t = [s.lower() for s in L]
print(t)