from turtle import*
import colorsys
setup(800,800)
speed(0)
tracer(10)
width(3)
bgcolor("black")

for i in range (1):
    for j in range(100):
        for k in range(5):
            right(90)
            forward(100)
            right(45)
            forward(100)
            circle(200)
            for l in range(20):
                color(colorsys.hsv_to_rgb(k/15,l/25,1))
                left(45)
                circle(150)
done()    