from tkinter import *
from turtle import *

# Set Variable:
axis_x = 300
axis_y = 300

# Player control functions
def forward(event):
    t.forward(9)

def back(event):
    t.back(9)

def left(event):
    t.left(90)

def right(event):
    t.right(90)

#Main window from Tkinter:
window = Tk()
window.title("Complete the maze game")
canvas = Canvas(height = 640, width = 640)
canvas.pack()

# Turtle settings for starting position
t = RawTurtle(canvas)
t.pencolor("blue")
t.pensize(5)
t.screen.bgpic("maze - 640 x 640.gif")
t.penup()
t.left(90)
t.setposition(0,0)
t.pendown()

# Press key for movement
window.bind("<Up>", forward)
window.bind("<Down>", back)
window.bind("<Left>", left)
window.bind("<Right>", right)

# Start the program
window.mainloop()

