import tkinter
import random

width = 500
height = 500
canvas = tkinter.Canvas(width=width,height=height)
canvas.pack()

size = 5 # musi byt 2^n + 1

heightmap = [[[] for j in range(size)] for i in range(size)]
heightmap[0][0], heightmap[0][size-1], heightmap[size-1][size-1], heightmap[size-1][0] = 128, 128, 128, 128

def diamondSquareAlgorithm(heightmap, start=(0,0), end=(len(heightmap)-1, len(heightmap)-1), randomness=0.1):
    middle = int((end[0]-start[0])/2)
    print(heightmap, start, end, middle)
    heightmap[middle][middle] = (heightmap[start[0]][start[1]]+heightmap[start[0]][end[1]]+heightmap[end[0]][start[1]]+heightmap[end[0]][start[0]])/4
    print(heightmap)
    
##    if middle[0] != int(middle[0]):
##        return
##    if middle[1] != int(middle[1]):
##        return
    diamondSquareAlgorithm(heightmap, start, middle, randomness//2)
    diamondSquareAlgorithm(heightmap, (middle[0], start[1]), (end[0], middle[1]), randomness//2)
    diamondSquareAlgorithm(heightmap, (start[0], middle[1]), (middle[0], end[0]), randomness//2)
    diamondSquareAlgorithm(heightmap, middle, end, randomness//2)


diamondSquareAlgorithm(heightmap)
