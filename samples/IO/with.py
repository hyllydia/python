#!/usr/bin/env python
#-8- coding:utf-8 -*-

from datetime import datetime

with open('test.txt','w') as f:
   f.write('Today is')
   f.write(datetime.now().strftime(' %Y-%m-%d %H:%M:%S'))
'''
strftime format
nian yue ri shifenmiao
time.strftime(' %Y-%m-%d %H:%M:%S')

'''
with open('test.txt','r') as f:
   s=f.read()
   print('open for read...')
   print(s)

with open('test.txt','rb+') as f:
   s=f.read()
   print('open as binary for read...')
   print(s)
'''
meiyou read binary format
'''
fpath = r'/root/yhou/test_py.txt'

with open(fpath,'r') as f:
   s=f.read()
   print(s)
~                       
