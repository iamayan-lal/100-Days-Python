from turtle import Turtle, Screen
import random
import turtle as t
t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

tim = Turtle()
tim.shape("turtle")
# Challenge 1 : Make a Square
'''
for i in range(4):
    tim.forward(100)
    tim.left(90)
'''
# Challenge 2 : Make dashed line(_ _ _ _ _)
'''
for i in range(15):
    tim.forward(10)
    penup()
    tim.forward(10)
    pendown()
'''
# Challenge 3 : Making a Triangle, Square, Pentagon, Hexagon, Heptagon, Octagon, Nonagon and Decagon
'''
def draw_shape(num_sides):
    for i in range(num_sides):
        angle = float(360 / num_sides)
        tim.forward(100)
        tim.right(angle)
for shape_side_n in range (3,11):
    tim.color(random.choice(colors))
    draw_shape(shape_side_n)
'''
# Challenge 4 : Draw a Random Walk
'''
tim.pensize(10)
for _ in range(200):
    directions = [0,90,180,270]
    tim.forward(30)
    tim.setheading(random.choice(directions))
    tim.color(color())
    tim.speed("fastest")
'''
#Challenge 5 : Draw a Spirograph
'''
tim.speed("fastest")
def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)
draw_spirograph(5)
'''
screen = Screen()
screen.exitonclick()