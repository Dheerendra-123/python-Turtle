import turtle
t=turtle.Turtle()
t.speed(20)
t.up()
list=["yellow","blue","orange","purple","red","pink","violet"]
t.goto(600,0)
for i in range(7):
    t.down()
    t.begin_fill()
    t.fillcolor(list[i])
    t.circle(100)
    t.end_fill()
    t.up()
    t.backward(200)
    t.down()
turtle.done()    