import turtle
turtle.shape('turtle')
n = 0

turtle.begin_fill()
while n < 360:
    turtle.forward(12)
    turtle.left(6)
    n += 6
turtle.color('yellow')
turtle.end_fill()
turtle.goto(0,0)
turtle.penup()
turtle.goto(-40,170)
turtle.pendown()
turtle.begin_fill()
turtle.color('black')
turtle.circle(-20)
turtle.color('blue')
turtle.end_fill()
turtle.penup()
turtle.goto(50,170)
turtle.pendown()
turtle.begin_fill()
turtle.color('black')
turtle.circle(-20)
turtle.color('blue')
turtle.end_fill()
turtle.pendown()
turtle.penup()
turtle.goto(5,150)
turtle.pendown()
turtle.right(90)
turtle.color('black')
turtle.width(5)
turtle.forward(50)
turtle.penup()
turtle.goto(55,80)
turtle.pendown()
turtle.color('red')
turtle.width(12)
turtle.circle(-50,180)





