import tkinter
import random

width = 500
height = 500
canvas = tkinter.Canvas(width=width,height=height)
canvas.pack()

for i in range(0,width,5):
    for j in range(0,height,5):
        color = "#" + str(random.randrange(0,256))*3
        canvas.create_rectangle(i,j,i+5,j+5, fill=color)
