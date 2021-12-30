import tkinter
import time

height = 1000
width = 1000
background_color = "black"
canvas = tkinter.Canvas(width=width,height=height, background=background_color)
canvas.pack()

refresh_rate = 0.001

center = [250,250]

def rgb(rgb):
    return "#%02x%02x%02x" % rgb 


def horizontal_lines(pos, color):
    while pos < width:
        pos *= 1.2
        canvas.create_line(0,pos,width,pos, fill=color)


def vertical_lines(color):
    for i in range(-8000,height+8000,25):
        if i < width/2:
            j = i + abs(width//2-i)/1.1
        else: j = i - abs(width//2-i)/1.1
        canvas.create_line(j,0,i,height, fill=color)

seconds = 0
while True:
    seconds += refresh_rate
    canvas.update()
    canvas.create_rectangle(0,0,width,height,fill=background_color)
    #print(time.time())
    vertical_lines(rgb((255,255,255)))
    horizontal_lines(seconds*5, rgb((255,255,255)))
    time.sleep(refresh_rate)
