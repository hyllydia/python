#!/usr/bin/env python
# -*- coding: utf-8 -*-

print([x * x for x in range(1, 11)])
print([x * x for x in range(1, 11) if x % 2 == 0])
print([m + n for m in 'ABC' for n in 'XYZ'])

d = {'x': 'A', 'y': 'B', 'z': 'C' }
print([k + '=' + v for k, v in d.items()])

L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])


L1 = ['Hello', 'World',18,24, 'IBM', 'Apple','Lydia']
print([s.lower() for s in L1 if isinstance(s,str)==True])
#The isinstance() function checks if the object (first argument) is an instance or subclass of classinfo class (second argument).
'''
isinstance() 函数来判断一个对象是否是一个已知的类型，类似 type()。

    isinstance() 与 type() 区别：

        type() 不会认为子类是一种父类类型，不考虑继承关系。

        isinstance() 会认为子类是一种父类类型，考虑继承关系。

    如果要判断两个类型是否相同推荐使用 isinstance()。
isinstance(object, classinfo)
'''
