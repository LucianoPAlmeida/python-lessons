import turtle
import math
def draw_square(angle):
    brad = turtle.Turtle()
    brad.shape("circle")
    brad.color("white")
    brad.right(angle)
    brad.speed(20)
    for i in range(4):
        brad.forward(50)
        brad.right(90)

window = turtle.Screen()
window.bgcolor("blue")
for i in range(40): 
    draw_square(360/40 * i)
window.exitonclick()
