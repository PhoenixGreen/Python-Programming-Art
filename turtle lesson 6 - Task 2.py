from tkinter import *
from turtle import *

# Commands for the buttons - tutle
def forward():
    t.forward(100)

def back():
    t.back(100)

def left():
    t.left(90)

def right():
    t.right(90)

def left45():
    t.left(45)

def right45():
    t.right(45)

#Main window - Tkinter:
window = Tk()
window.title("MyEtchAsketch")
canvas = Canvas(height = 640, width = 427,)
canvas.pack()

# Draw turtle on main window - turtle and tkinter
t = RawTurtle(canvas)

# Buttons - tkinter
Button(master = window, text = "Forward", command = forward).pack(side = LEFT)
Button(master = window, text = "Back", command = back).pack(side = LEFT)
Button(master = window, text = "Left", command = left).pack(side = LEFT)
Button(master = window, text = "Right", command = right).pack(side = LEFT)

Button(master = window, text = "Left 45", command = left45).pack(side = LEFT)
Button(master = window, text = "Right 45", command = right45).pack(side = LEFT)

# Start the program - tkinter
window.mainloop()

