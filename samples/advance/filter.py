#!/usr/bin/env python
#-*-coding:utf-8 -*-

def is_odd(n):
   return n % 2==1
L=range(100)
print(list(filter(is_odd,L)))

def is_empty(s):
   return s and s.strip()
print(list(filter(is_empty,['','a','b',None,'C'])))
