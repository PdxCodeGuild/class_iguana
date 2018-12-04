#lab01.turtle.py

from turtle import *


i = 0
edge_length = 150
n_sides = 16
fillcolor('blue')
begin_fill()

i = 0
while i < n_sides:
	forward(edge_length/n_sides)
	right(360/n_sides)
	i = i + 1

end_fill()

left(45)
forward(150)


done()