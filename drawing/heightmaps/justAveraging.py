import tkinter
import random

width = 500
height = 500
canvas = tkinter.Canvas(width=width,height=height)
canvas.pack()

heightmap = [[] for i in range(height//5)]

for i in range(0,width//5):
    for j in range(0,height//5):
        color = int(random.randrange(0,255))
        heightmap[i].append(color)


def averageIt(heightmap):
    for i in range(len(heightmap)):
        for j in range(len(heightmap[0])):
            iplus1 = min(i+1, 99)
            jplus1 = min(j+1, 99)
            neighbors = (heightmap[i-1][j], heightmap[iplus1][j], heightmap[i-1][j-1], heightmap[i-1][jplus1], heightmap[iplus1][jplus1], heightmap[iplus1][j-1], heightmap[i][jplus1], heightmap[i][j-1])            
            heightmap[i][j] = sum(neighbors)//8


for _ in range(3):
    averageIt(heightmap)

for i in range(0,width//5):
    for j in range(0,height//5):
        color = "#%02x%02x%02x" % (heightmap[i][j], heightmap[i][j], heightmap[i][j]) 
        canvas.create_rectangle(i*5,j*5,i*5+50,j*5+50, fill=color, outline="")
