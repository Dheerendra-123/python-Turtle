from turtle import*
import colorsys
bgcolor("black")
pensize(1)
speed(20)
for i in range(1000):
    color (colorsys.hsv_to_rgb(i/20,1,1))
    circle(i,300)
    left(92)