from turtle import *
from random import *

# Lists for use in choice()
color_picker_background = ["black"]
color_picker_pen = [ "white", "gray", "#098d9c"]
color(choice(color_picker_pen),"")

# Initial Turtle Settings
shape("turtle")
pensize(randint(1,3))
bgcolor(choice(color_picker_background))
speed(0)

# Set loop Variables
loops = randint(20, 200)
current = 0

# Start drawing pattern
setposition(0,0)

while current < loops:
    
    # Set Variables
    size = randint(30,50)
    extent = randint(90,360)
    steps = randint(3, 36)
    distance = randint(1,80)
    angle = randint(90,180)
    move = [left(angle), left(angle), circle(size, extent, steps), forward(distance)]
    
    print(move)
    current = current +1
    
# End
done()

