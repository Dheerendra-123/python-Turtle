import turtle
t=turtle.Turtle()
t.speed(0)
list=["red","yellow","orange","green","pink"]
for i in range(400): 
    t.color(list[i%5])
    t.pensize(i/15+1)
    t.forward(i)
    t.left(87)
turtle.done()    