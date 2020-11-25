#-*- coding:utf-8 -*-
"""
 Fibonacci数列
"""
def fibonacci():
    a,b=0,1
    while True:
        yield b
        a,b=b,a+b
fib=fibonacci()
print ([fib.next() for i in range(10)])