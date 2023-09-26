import turtle
t=turtle.Turtle()
t.speed(20)
t.up()
list=["yellow","blue","orange","purple","red","pink","violet"]
t.goto(400,300)
for i in range (5):
    for j in range(7):
       t.down()
       t.begin_fill()
       t.fillcolor(list[j])
       t.circle(30)
       t.end_fill()
       t.up()
       t.backward(60)
       t.down()  
    t.left(90)   
turtle.done()    