import tkinter
import random

width = 500
height = 500
canvas = tkinter.Canvas(width=width,height=height)
canvas.pack()

heightmap = [[] for i in range(height//5)]

for i in range(0,width//5):
    for j in range(0,height//5):
        heightmap[i].append(random.randrange(0,255))


for i in range(len(heightmap)):
    for j in range(len(heightmap[0])):
        i = i%(len(heightmap)-1)
        j = j%(len(heightmap[0])-1)
        neighbors = (heightmap[i-1][j], heightmap[i+1][j], heightmap[i-1][j-1], heightmap[i-1][j+1], heightmap[i+1][j+1], heightmap[i+1][j-1], heightmap[i][j+1], heightmap[i][j-1])            
        heightmap[i][j] = sum(neighbors)//len(neighbors)


for i in range(0,width//5):
    for j in range(0,height//5):
        color = "#" + str(heightmap[i][j])*3
        canvas.create_rectangle(i,j,i+50,j+50, fill=color, outline="")
