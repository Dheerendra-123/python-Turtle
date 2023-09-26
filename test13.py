import turtle
t=turtle.Turtle()
t.speed()
list=["yellow","blue","orange","purple","red","pink","violet","blue"]
for i in range(400): 
    t.color(list[i%8])
    t.pensize(i/10+1)
    t.forward(i)
    t.left(39)
turtle.done()    