from turtle import *

# Initial pen settings
shape("turtle")

# First circle
pensize(5)
pencolor("red")
fillcolor("violet")

begin_fill()
circle(150)
end_fill()

# Second circle
pensize(10)
pencolor("black")
fillcolor("green")

begin_fill()
circle(100)
end_fill()

# Thrid circle
pensize(5)
pencolor("blue")
fillcolor("yellow")

begin_fill()
circle(50, 360, 4)
end_fill()

# Fourth circle
# Create your own circle shapes here


# stop listening for turtle
done()
