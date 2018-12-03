
"""
author: Richard Sherman
2018-12-03

lab01-turtle.py
    draws a suspicious-looking stick figure"""

from turtle import *

speed(5)

edge_length = 200
n_sides = 100
i = 0
while i < n_sides:
    forward(edge_length/n_sides)
    right(360/n_sides)
    i = i + 1

#eyes
penup()
setposition(-10,-25)
pendown()
forward(7)
penup()
setposition(10, -25)
pendown()
forward(7)

#nose
penup()
setposition(1, -40)
pendown()
forward(7)
left(135)
forward(14)

#mouth
penup()
setposition(-7, -45)
pendown()
right(135)
forward(20)

#body
penup()
setposition(1, -60)
pendown()
right(90)
forward(100)

#legs
right(45)
forward(50)
penup()
setposition(1, -160)
pendown()
right(275)
forward(50)

#arms
penup()
setposition(-75, -100)
pendown()
left(60)
forward(160)

done()