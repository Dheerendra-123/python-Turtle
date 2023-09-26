import turtle
t=turtle.Turtle()
t.speed(0)
list=["red","yellow","orange","green"]
for i in range (300):
    t.color(list[i%4])
    t.pensize(i/12+1)
    t.forward(i)
    t.left(84)
turtle.done()    