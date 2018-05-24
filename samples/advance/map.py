
#!/usr/bin/env python
#-*_coding:utf-8 -*-

def f(x):
   return x*x

r=map(f,[1,2,3,4,5,6])
print(list(r))

def normalize(name):
   return name.capitalize()
L1=['adam','LISA','barT']
L2=map(normalize,L1)
print(list(L2))

'''
def normalize01(name01):
   return name01[:1].upper()+name01[1:].lower()
if _name01_=='_main_':        # do not understand  这里不明白，此代码也没有运行成功
   L1=['lydia','luCY','JUDY']
   L2=map(normalize01,L1)
   print(list(L2))
'''
