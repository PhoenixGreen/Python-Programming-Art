from turtle import *

# Initial Turtle Settings
shape("turtle")
pensize(4)
color("brown","")
bgcolor("yellow")
speed(0)

# Set Variables
detail = 12     # decrease for more branches
length = 80     # increase for larger tree
thickness = 20  # vary to see effect
angle = 20      # vary to see effect

def draw_tree(thickness, length):
    if length > 5 and length < 20:
        color("green")
    else:
        color("brown")
        pensize(thickness)
        forward(length)
        right(angle)
        draw_tree(thickness / 1.5, length - detail)
        left(2 * angle)
        draw_tree(thickness / 1.5, length - detail)
        right(angle)
        back(length)
        color("brown")
        
left(90)
penup()
back(100)
pendown()

# The program starts here
draw_tree(thickness, length)

# End
done()


