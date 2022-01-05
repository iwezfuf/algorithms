import tkinter
import random
import time

height = 800
width = 1000
canvas = tkinter.Canvas(height=height, width=width, background="black")
canvas.pack()


def create_city(start, end, maxDetail=7, buildings=True, currentDetail=1, ciarahor1ver0=False):

    randomness_x = random.randint(-(end[0]-start[0])//(4*(1+maxDetail*0.07)), (end[0]-start[0])//(4*(1+maxDetail*0.07)))
    randomness_y = random.randint(-(end[1]-start[1])//(4*(1+maxDetail*0.07)), (end[1]-start[1])//(4*(1+maxDetail*0.07)))
        
    point = ((start[0]+end[0])//2+randomness_x, (start[1]+end[1])//2+randomness_y)


    def divide():
        if ciarahor1ver0:
            if currentDetail < maxDetail-1:
                canvas.create_line(start[0], point[1], end[0], point[1], fill="white")
            if currentDetail < maxDetail:
                create_city(start, (end[0], point[1]), maxDetail, buildings, currentDetail+1, False)
                create_city((start[0], point[1]), end, maxDetail, buildings, currentDetail+1, False)
            
        else:
            if currentDetail < maxDetail-1:
                canvas.create_line(point[0], start[1], point[0], end[1], fill="white")
            if currentDetail < maxDetail:
                create_city(start, (point[0], end[1]), maxDetail, buildings, currentDetail+1, True)
                create_city((point[0], start[1]), end, maxDetail, buildings, currentDetail+1, True)

    def add_buildings():
        if currentDetail > maxDetail-1:
            if random.randint(0,5):
                
                color = "gray" + str(random.randint(20,40))
                
                leng = end[0]-start[0]
                heig = end[1]-start[1]

                if leng > 7.5*2**(10-maxDetail) and heig > 7.5*2**(10-maxDetail):
                    offsets = []
                    for i in range(4):
                        offsets.append(random.randint(1000*2**(10-maxDetail),3500*2**(10-maxDetail))/1000)
                    canvas.create_rectangle(start[0]+offsets[0], start[1]+offsets[1], end[0]-offsets[2], end[1]-offsets[3], fill=color)
            else:
                divide()
        else: divide()


    if buildings:
        add_buildings()
    else: divide()
            


create_city([0,0], [1000,800], 7, True)

def run():
    canvas.delete("all")
    try:
        qual = int(detail.get())
        if qual < 1 or qual > 10:
            qual = 7
    except: qual = 7
    create_city([0,0], [1000,800], qual, True)


detail = tkinter.Entry(text="detail")
detail.pack(side="left")

but = tkinter.Button(text="new city", command=run)
but.pack(side="left")

canvas.mainloop()
