from turtle import *
 
 #we want to paint a house

#step 1: draw a square
speed(20)
width(7)
color("purple")
begin_fill()
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()
#end of spuare

#drawing a door
begin_fill()
forward(70)
color("yellow")
left(90)

forward(110)
right(90)

forward(60)
right(90)

forward(110)
end_fill()
#end of a door
penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
#drawing a loof
right(150)
forward(200)

left(120)
forward(200)
end_fill()

color("purple")
left(30)
forward(200)


penup()
goto(170, 170)
pendown()

color("brown")
begin_fill()
#drawing a window
forward(40)
right(90)

forward(40)
right(90)
 
forward(40)
right(90)
forward(40)
end_fill()

penup()
goto(200,200)
pendown()

color("purple")
right(90)
forward(200)

right(90)
right(45)
penup()
forward(185)
pendown()

color("brown")
begin_fill()
left(45)
forward(40)
right(90)
forward(40)

right(90)
forward(40)

right(90)
forward(40)
end_fill()
#end of a window

exitonclick()