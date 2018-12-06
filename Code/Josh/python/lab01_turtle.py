from turtle import *

screensize(1000,1000)
i = 0
while i < 360:
    forward(100)
    left(45)
    i = i + 45
penup()
left(90)
forward(150)
pendown()
i = 0
while i < 360:
    forward(5)
    left(45)
    i = i + 45
penup()
right(90)
forward(100)
pendown()
i = 0
while i < 360:
    forward(5)
    left(45)
    i = i + 45
penup()
right(90)
forward(60)
pendown()
i = 0
while i < 180:
    forward(8)
    right(10)
    i = i + 10
penup()
forward(40)
right(90)
forward(50)
right(45)
pendown()
forward(40)
right(135)
forward(40)#end of nose
penup()
left(90)
forward(95)#start of neck
pendown()
forward(100)
left(90)
forward(100)
left(45)
forward(100)
left(180)
forward(100)
right(45)
forward(200)
left(45)
forward(100)
left(180)
forward(100)
right(45)
forward(100)
right(90)
forward(200)
left(45)
forward(150)
left(45)
forward(60)
left(180)
forward(60)
right(45)
forward(150)
left(90)
forward(150)
right(45)
forward(60)#end of lazy eyed man stop face man
penup()
forward(100)


done()