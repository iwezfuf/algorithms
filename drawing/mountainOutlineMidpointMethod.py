import tkinter
import random
import time

height = 800
width = 1500
canvas = tkinter.Canvas(height=height, width=width, background="black")
canvas.pack()


def mountain(start=[0,height//2], end=[width, height//2], factor=height//2, maxLevel=10, currentLevel=1, seed=1):
    random.seed(seed)
    if currentLevel == maxLevel:
        canvas.create_line(start[0], start[1], end[0], end[1], fill="white")
    else:
        midpoint = [(start[0]+end[0])//2, (start[1]+end[1])//2]
        midpoint[1] += random.randrange(-factor,factor)
        mountain(start, midpoint, factor//2, maxLevel, currentLevel+1, random.randint(1,1000))
        random.seed(seed)
        mountain(midpoint, end, factor//2, maxLevel, currentLevel+1, random.randint(1001,2000))


def run():
    maxLevel = 10
    random.seed()
    seed = random.randint(1,10000)
    for level in range(1,maxLevel+1):
        canvas.delete("all")
        mountain([0,height//2], [width, height//2], height//2, level, 1, seed)
        canvas.update()
        time.sleep(0.1)

        
newMountain = tkinter.Button(text="New mountain", command=run)
newMountain.pack(side="left")
canvas.mainloop()
