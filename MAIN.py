import turtle
import test1 as lineal
# these values are for the compass star shape
Outer_Point = 10
Inner_Point = 3
# this value represents how far on the x,y-axis the grid will go
Grid_Size = 10
# this value represents how large each grid box will appear on your screen
BoxSize = 5
# if your compass star goes off-screen then increase these values because these make the screen larger
turtle.screensize(2500, 2500)

turtle.speed(10)
# this next section creates the thicker lines to represent the x-axis and the y-axis
Grid_Size = Grid_Size * BoxSize
turtle.pensize(2)
turtle.setpos(-Grid_Size, 0)
turtle.setpos(Grid_Size, 0)
turtle.penup()
turtle.setpos(0, -Grid_Size)
turtle.pendown()
turtle.setpos(0, Grid_Size)
turtle.pensize(1)
turtle.left(90)
xg = 0
yg = 0

# the next section creates the grid
while xg < Grid_Size * 2:
    turtle.penup()
    turtle.setpos(-Grid_Size + xg, Grid_Size)
    turtle.pendown()
    turtle.setpos(-Grid_Size + xg, -Grid_Size)
    xg = xg + BoxSize
while yg < Grid_Size * 2:
    turtle.penup()
    turtle.setpos(Grid_Size, -Grid_Size + yg)
    turtle.pendown()
    turtle.setpos(-Grid_Size, -Grid_Size + yg)
    yg = yg + BoxSize
# end of grid section

# line #1

x0 = 0
y0 = Outer_Point
x1 = Inner_Point
y1 = Inner_Point
loop1 = 1

#this is the beginning of the bresenham algorithim

lineal.line_algorithim()

# line #2

x0 = Outer_Point
y0 = 0
x1 = Inner_Point
y1 = Inner_Point
loop1 = 1

lineal.line_algorithim()


# line #3

x0 = Outer_Point
y0 = 0
x1 = Inner_Point
y1 = -Inner_Point
loop1 = 1

lineal.line_algorithim()

# line #4

x0 = 0
y0 = -Outer_Point
x1 = Inner_Point
y1 = -Inner_Point
loop1 = 1

lineal.line_algorithim()

# line #5

x0 = 0
y0 = -Outer_Point
x1 = -Inner_Point
y1 = -Inner_Point
loop1 = 1

lineal.line_algorithim()

# line #6

x0 = -Outer_Point
y0 = 0
x1 = -Inner_Point
y1 = -Inner_Point
loop1 = 1

lineal.line_algorithim()

# line #7

x0 = -Outer_Point
y0 = 0
x1 = -Inner_Point
y1 = Inner_Point
loop1 = 1

lineal.line_algorithim()

# line #8

x0 = 0
y0 = Outer_Point
x1 = -Inner_Point
y1 = Inner_Point
loop1 = 1

lineal.line_algorithim()
turtle.done()