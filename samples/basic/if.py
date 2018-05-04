#!/usr/bin/env python

height=1.75
weight=80.5
#a=weight/height
bmi = weight/height/height
if bmi>=32:
   print('over fat')
elif bmi>=28:
   print('fat')
elif bmi>=25:
   print('overweight')
elif bmi>=18.5:
   print('normal')
else:
   print('too light')
