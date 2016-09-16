
k = int(input())


import turtle
turtle.shape('turtle')

def ris(n):
    t = n
    while n > 0:
        turtle.forward(t*10+10)
        turtle.left(360/t)
        n -= 1


i = 3
l = 10
p = 1
while i <= k:
    ris(i)
    i +=1
    turtle.penup()
    turtle.goto(-5*p,0)
    turtle.right(90)
    turtle.forward(l)
    turtle.left(90)
    turtle.pendown()
    l=l+10
    p+=1

#turtle.forward(50)
#turtle.left(90)
#turtle.forward(50)
#turtle.right(90)
#turtle.forward(50)
#turtle.right(90)
#turtle.forward(50)
