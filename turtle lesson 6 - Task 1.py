from tkinter import *

#Main window - Tkinter:
Tk().title("My EtchAsketch")
canvas = Canvas(height = 640, width = 427)
scene = PhotoImage(file="Hello Image.gif")
canvas.create_image(0, 0, image=scene, anchor=NW)
canvas.pack()

# Start the program
mainloop()




