#learn with prem
import turtle
import colorsys
screen = turtle.Screen()
screen. setup(500, 600, startx=0, starty=100)
t = turtle.Turtle()
s = turtle.Screen ()
s.bgcolor("black")
t. speed (0)
n = 36
h = 0
for i in range(360):
    c = colorsys. hsv_to_rgb(h, 1,0.8)
    h += 1/n
    t.color(c)
    t.circle(90)
    t. left(10)

