import tkinter
import random

height = 800
width = 1500
canvas = tkinter.Canvas(height=height, width=width, background="black")
canvas.pack()


def midpoint(first, second, factor, middle, top=False):
    midpoint = [0,0]
    midpoint[0] = (first[0]+second[0])/2
    midpoint[1] = (first[1]+second[1])/2

    perpendicular = (second[1]-first[1], first[0]-second[0])
    lenght = (perpendicular[0]**2 + perpendicular[1]**2)**0.5   # normalizing
    perpendicular = (perpendicular[0]/lenght, perpendicular[1]/lenght)   # normalizing
    variance = random.randrange(-factor//2,factor//2)+random.randrange(-factor//2,factor//2)   # gaussian/normal distribution
    if middle:
        #variance = 0
        #variance = random.randrange(0,factor//4)+random.randrange(0,factor//4)
        if top:
            #variance = factor
            variance = random.randrange(0,factor//2)+random.randrange(0,factor//2)
        else:
            #variance = -factor
            variance = -random.randrange(0,factor//2)-random.randrange(0,factor//2)
    midpoint = [midpoint[0]+variance*perpendicular[0], midpoint[1]+variance*perpendicular[1]]

        
    return midpoint


def mountain(first, second, third, factor=height//2, maxLevel=10, currentLevel=1, middle=False, top=True):
    if currentLevel == maxLevel:
        #canvas.after(1)
        #canvas.update()
        #if middle: uplne na nic ale zaujimave
        canvas.create_line(first[0], first[1], second[0], second[1], fill="white")
        canvas.create_line(first[0], first[1], third[0], third[1], fill="white")
        canvas.create_line(second[0], second[1], third[0], third[1], fill="white")
    else:
        fs = midpoint(first, second, factor, middle, top)
        ft = midpoint(first, third, factor, middle, not top) 
        st = midpoint(second, third, factor, middle, top)
        mountain(first, fs, ft, factor//2, maxLevel, currentLevel+1, False, top) # vlavo
        mountain(second, fs, st, factor//2, maxLevel, currentLevel+1, False, top) # vpravo
        mountain(third, ft, st, factor//2, maxLevel, currentLevel+1, False, top) # hore
        mountain(fs, ft, st, factor//2, maxLevel, currentLevel+1, True, not top) # stred
        


def run():
    canvas.create_rectangle(0,0,width,height,fill="black")
    try:
        qual = int(quality.get())
        if qual < 1 or qual > 8:
            qual = 5
    except: qual = 5

    try:
        randomn = int(randomness.get())
        if randomn < 0:
            randomn = 180
    except: randomn = 180
        
    mountain([100,600], [750,100], [1400,600], randomn, qual, 1, False)



quality = tkinter.Entry(text="Enter number 1-8")
quality.pack(side="left")

randomness = tkinter.Entry(text="Enter positive number, default 180, randomness")
randomness.pack(side="left")

newMountain = tkinter.Button(text="New mountain", command=run)
newMountain.pack(side="left")


canvas.mainloop()
