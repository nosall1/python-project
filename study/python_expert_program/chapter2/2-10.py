# -*- coding:utf-8 -*-
"""
"""
import itertools


def starting_at_five():
    value = input()
    while value != '':
        for el in itertools.islice(value.split(), 4, None):
            yield el
        value = input()


iter = starting_at_five()
iter.next()
