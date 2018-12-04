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



done()