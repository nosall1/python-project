#-*- coding:utf-8 -*-
# Fibonacci数生成器
def fib():
    a,b=0,1
    while True:
        a,b=b,a+b
        yield a

# 偶数生成器
def even(gen):
    for val in gen:
        if val % 2==0:
            yield val

def main():
    gen=even(fib())
    for _ in range(10):
        print(next(gen))

if __name__ == '__main__':
    main()