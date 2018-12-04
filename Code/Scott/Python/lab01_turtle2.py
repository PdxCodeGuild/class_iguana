#lab01.turtle.py

from turtle import *

penup()
setposition(0,100)
pendown()
edge_length = 200
n_sides = 25

i = 0
while i < n_sides:
	forward(edge_length/n_sides)
	right(360/n_sides)
	i = i + 1
penup()
setposition(0,38)
pendown()
right(90)
forward(50)
right(100)
forward(75)

forward(15)
right(144)
forward(15)
right(144)
forward(15)
right(144)
forward(15)
right(144)
forward(15)

penup()
setposition(0,38)
pendown()
right(135)
forward(50)
right(45)
forward(75)

forward(15)
right(144)
forward(15)
right(144)
forward(15)
right(144)
forward(15)
right(144)
forward(15)

penup()
setposition(0,38)
pendown()
forward(120)
right(75)
forward(60)
left(90)
forward(60)
right(90)

i = 0
while i < 4:
    forward(20)
    left(90)
    i = i + 1

penup()
setposition(10, -85)
left(90)
pendown()
forward(60)
left(90)
forward(45)
right(90)

i = 0
while i < 4:
    forward(20)
    left(90)
    i = i + 1

# def foot(side, angle):
# 	i = 0
# 	while i < 4:
# 		side = forward()
# 		angle = left()
# 		i = i + 1



done()