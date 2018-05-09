
#!/usr/bin/env python
# -*- coding: utf-8 -*-

s = (x * x for x in range(5))
print(s)
'''
generator() can not be printed directly,can be  printed by next() and for 
'''
for x in s:
   print(x)
# Fibonacci 
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
     #  yield b  pyhton2.7报错
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

f = fib(10)
print('fib(10):', f)
for x in f:
    print(x)

# call generator manually:
g = fib(5)
while 1:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break

~                 
