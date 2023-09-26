import turtle
t=turtle.Turtle()
t.speed()
list=["yellow","blue","orange","purple","red","pink","violet","blue"]
for i in range(100): 
    t.color(list[i%8])
    t.pensize(i/10+1)
    t.forward(i)
    t.left(59)
turtle.done()