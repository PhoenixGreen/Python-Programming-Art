from turtle import *

# Initial pen settings
shape("turtle")
pensize(5)
pencolor("black")

# Building a square loop
def square(side_length):
    current = 0

    while current < 4:
        forward(side_length)
        right(90)
        current = current +1

# Call the function
square(300)
square(100)

# stop listening for turtle
done()
