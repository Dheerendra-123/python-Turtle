import turtle
t=turtle.Turtle()
t.speed()
t.up()
list=["yellow","blue","orange","purple","red","pink","violet","blue"]
t.goto(400,0)
for i in range(9):
    t.down()
    t.begin_fill()
    t.fillcolor(list[i])
    t.circle(100)
    t.end_fill()
    t.up()
    t.backward(100)
    t.down()
turtle.done()    