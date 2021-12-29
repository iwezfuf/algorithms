import tkinter
import random

width = 500
height = 500
canvas = tkinter.Canvas(width=width,height=height)
canvas.pack()

heightmap = [[[] for j in range(129)] for i in range(129)]
heightmap[0][0], heightmap[0][128], heightmap[128][128], heightmap[128][0] = 128

def diamondSquareAlgorithm(area, randomness):
    ld, lh, pd, ph = area
    middle = [abs(ld[0]-ph[0]), abs(ld[1]-ph[1])]
    area
    if middle[0] != int(middle[0]):
        return
    if middle[1] != int(middle[1]):
        return
    diamondSquareAlgorithm((ld,lh), randomness//2)
    diamondSquareAlgorithm((ld,pd), randomness//2)
    diamondSquareAlgorithm((pd,ph), randomness//2)
    diamondSquareAlgorithm((ph,lh), randomness//2)


diamondSquareAlgorithm(([0,0, ], ))
