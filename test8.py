def draw_circle(x,y,color,rad):
    t.up()
    t.goto(x,y)
    t.down()
    t.begin_fill()
    t.fillcolor(color)
    t.circle(rad)
    t.end_fill()
    t.up()
    t.home()

import turtle
t=turtle.Turtle()
t.speed(20)
draw_circle(0,-50,"green",50)
draw_circle(200,-200,"yellow",50)
draw_circle(-200,-200,"orange",50)
draw_circle(200,200,"red",50)
draw_circle(-200,200,"purple",50)
draw_circle(0,-500,"green",50)
draw_circle(100,-20,"yellow",50)
draw_circle(-20,-300,"orange",50)
draw_circle(20,20,"red",50)
draw_circle(-240,290,"purple",50)
turtle.done()
