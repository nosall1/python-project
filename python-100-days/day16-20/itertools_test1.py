#-*- coding:utf-8 -*-
'''
迭代工具模块
'''

import itertools
# 产生ABCD的全排列
per=itertools.permutations('ABCD')
for x in per:
    print(x)

# 产生ABCDE的雾选三组合
per=itertools.combinations('ABCDE',3)
for x in per:
    print(x)

# 产生ABCD和123的笛卡尔积
per=itertools.product('ABCD','123')
for x in per:
    print(x)

# 产生ABC的无限循环序列
per=itertools.cycle(('A','B','C'))
for x in per:
    print(x)