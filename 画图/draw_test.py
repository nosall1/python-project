#-*- coding:utf-8 -*-

import turtle
repeats=0
turtle.fillcolor('red')
turtle.begin_fill()
while repeats<360:
    turtle.forward(1)
    turtle.right(1)
    repeats+repeats+1
turtle.end_fill()
turtle.done