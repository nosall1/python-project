# -*- coding:utf-8 -*-
"""
 迭代器模式
"""


class MyIter(object):
    def __init__(self, n):
        self.index = 0
        self.n = n

    def __iter__(self):
        #如果返回自己，则只能打印一遍平方值
        # return self
        return MyIter(self.n)

    def next(self):
        if self.index < self.n:
            value = self.index ** 2
            self.index += 1
            return value
        else:
            raise StopIteration()

# 生成器
def MyGenerator(n):
    index=0
    while index<n:
        yield index**2
        index+=1


if __name__ == '__main__':
    x_square = MyIter(10)
    for x in x_square:
        print (x)
    # for x in x_square:
    #     print x
    x_square_1=MyGenerator(10)
    for x in x_square_1:
        print (x)
        # lst=['hello alice','hello Bob','hello Eve']
        # lst_iter=iter(lst)
        # print lst_iter
        # print lst_iter.next()
        # print lst_iter.next()
        # print lst_iter.next()
        # print lst_iter.next()
