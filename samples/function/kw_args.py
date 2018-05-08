#!/usr/bin/env python
#-*-coding:utf-8-*-
def person(name,age,**kw):
   print('name:',name,'age:',age,'others:',kw)
person('sandy',20)
person('Lydia',18,city='shanghai',job='engineer')
extra={'city':'shanghai','job:':'engineer'}
person('kelly',20,**extra)

def print_scores(**kw1):
   print('      Name  Score')
   print('*****************')
   for name,score in kw1.items():
       print('%10s  %d' %(name,score))
   print('%%%%%%%%%%%%%%%%%')
print_scores(adma=92,lisa=90,bob=80)
data={'lydia':100,'kelly':90,'sandy':80}
print_scores(**data)
