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
      print('%s!,%s' %(greeting,','.join(args)))  # .join() ？？？
hello('Hi')   # =>greeting='HI', agrs()
hello('Hi','Lydia') # => greeting='Hi', args=('Lydia')
hello('Hi','Lydia','kelly','sandy') # =>greeting='Hi',agrs=('Lydia','kelly','sandy')

names=('xiaoming','xiaohong')
hello('Hi',*names)
