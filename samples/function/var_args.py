#!/usr/bin/env python
#-*-coding:utf-8-*-
def product(*nums):
   pro=1
   for n in nums:
       pro=pro*n
   return pro
print('product(5)=',product(5))
print('product(2,3)=',product(2,3))
print('product(5,6,8)=',product(5,6,8))
print('product(5,6,7,9)=',product(5,6,7,9))


def hello(greeting,*args):
   if (len(args)==0):
      print('%s!' %greeting)
   else:
      print('%s!,%s' %(greeting,','.join(args))) 
      '''
      .join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串
       a = ['a','b','c','d','e']
       print '-'.join(a)
       print '*'.join(a[1:3])
       输出:
       a-b-c-d-e
       b*c
       '''
hello('Hi')   # =>greeting='HI', agrs()
hello('Hi','Lydia') # => greeting='Hi', args=('Lydia')
hello('Hi','Lydia','kelly','sandy') # =>greeting='Hi',agrs=('Lydia','kelly','sandy')

names=('xiaoming','xiaohong')
hello('Hi',*names)
