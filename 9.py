
k = int(input())


import turtle
turtle.shape('turtle')

def ris(n):
    t = n
    turtle.left(90+180/t)
    while n > 0:
        turtle.forward(t*11+10)
        turtle.left(360/t)
        n -= 1


i = 3
l = 10
p = 1
turtle.penup()
turtle.goto(10,0)
turtle.pendown()
while i <= k:
    ris(i)
    i +=1
    turtle.right(90+180/(i-1))
    turtle.penup()
    turtle.goto(0,0)
    turtle.forward(20*p)
    turtle.pendown()
    p+=1

#turtle.forward(50)
#turtle.left(90)
#turtle.forward(50)
#turtle.right(90)
#turtle.forward(50)
#turtle.right(90)
#turtle.forward(50)
