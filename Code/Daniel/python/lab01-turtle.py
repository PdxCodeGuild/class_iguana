from turtle import *

speed(100)

edge_length = 200
n_sides = 100
legLength = 70
armLength = 50
legAngle = 20

# head
i = 0
while i < n_sides:
	forward(edge_length/n_sides)
	right(540/n_sides)
	i = i + 1

# body
left(90)
forward(80)

# legs
left(legAngle)
forward(legLength)
back(legLength)
right(legAngle * 2)
forward(legLength)
back(legLength)
right(180 - legAngle)

# arms
forward(armLength)
left(150)
forward(armLength)
back(armLength)
right(200)
forward(armLength)
right(180)

done()