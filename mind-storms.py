import turtle
import math
def draw_square():
    brad = turtle.Turtle()
    brad.shape("circle")
    brad.color("white")
    for i in range(4):
        brad.forward(50)
        brad.right(90)
def draw_circle(): 
    brad = turtle.Turtle()
    brad.shape("arrow")
    brad.circle(25)

def draw_triangle():
    brad = turtle.Turtle()
    brad.forward(50)
    brad.right(90)
    brad.forward(50)
    brad.right(135)
    brad.forward(math.sqrt((50*50+50*50)))

window = turtle.Screen()
window.bgcolor("red")
draw_square()
draw_circle()
draw_triangle()
window.exitonclick()