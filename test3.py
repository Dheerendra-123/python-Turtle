import turtle
t=turtle.Turtle()
t.color("white")
wn=turtle.Screen()
wn.bgcolor("black")
t.begin_fill()
t.fillcolor("red")
t.speed(6)
for i in range(4):
    t.forward(200)
    t.left(90)
    
t.end_fill ()
turtle.done()

    