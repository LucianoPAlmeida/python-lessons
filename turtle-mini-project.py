import turtle
import math
def draw_shape(angle):
    brad = turtle.Turtle()
    brad.shape("circle")
    brad.color("white")
    brad.right(angle)
    brad.speed(200)
    for i in range(2):
        brad.right(120)
        brad.forward(60)
        brad.right(60)
        brad.forward(60)

def draw_flower():
    for i in range(40): 
        draw_shape(360/40 * i)
    draw_base()

def draw_base():
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("white")
    brad.right(90)
    brad.forward(200)
# Drawing Flower
window = turtle.Screen()
window.bgcolor("blue")
draw_flower()
window.exitonclick()
