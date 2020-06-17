from tkinter import *

# Set Variable:
axis_x = 300
axis_y = 300

# Player control functions
def move_N(event):
    global axis_y
    canvas.create_line(axis_x, axis_y, axis_x, axis_y - 5, width = 5, fill = "green")
    axis_y = axis_y - 5

def move_S(event):
    global axis_y
    canvas.create_line(axis_x, axis_y, axis_x, axis_y + 5, width = 5, fill = "blue")
    axis_y = axis_y + 5

def move_E(event):
    global axis_x
    canvas.create_line(axis_x, axis_y, axis_x + 5, axis_y, width = 5, fill = "red")
    axis_x = axis_x + 5

def move_W(event):
    global axis_x
    canvas.create_line(axis_x, axis_y, axis_x - 5, axis_y, width = 5, fill = "yellow")
    axis_x = axis_x - 5

#Main window from Tkinter:
window = Tk()
window.title("Complete the maze game")
canvas = Canvas(bg = "black", height = 640, width = 640, highlightthickness = 0)
scene = PhotoImage(file="maze - 640 x 640.gif")
canvas.create_image(0, 0, image=scene, anchor=NW)
canvas.pack()

# Press key for movement
window.bind("<Up>", move_N)
window.bind("<Down>", move_S)
window.bind("<Right>", move_E)
window.bind("<Left>", move_W)

# Start the program
window.mainloop()

