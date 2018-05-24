
#!/usr/bin/env python
#-*- coding:utf-8 -*-

def fn(x,y):
   return x*y
l=range(6)
r=reduce(fn,l[1:])  # slice shi dui list or tuple
print(r)


from functools import reduce
DIGITS={'0':0,
        '1':1,
        '2':2,
        '3':3,
        '4':4,
        '5':5,
        '6':6,
        '7':7,
        '8':8,
        '9':9
      #  '.':-1   jiang zifuchuan zhuanhuan weo fudianshu do not understand
       }
def str2int(s):
   def fn(x,y):
      return 10*x+y
   def char2num(s):
      return DIGITS[s]
   return reduce(fn,map(char2num,s))
print(str2int('13579'))
#print(str2int('123.456'))
# lambda???
~                   
