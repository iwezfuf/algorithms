import tkinter
import random

height = 700
width = 1500
canvas = tkinter.Canvas(height=height, width=width, background="black")
canvas.pack()
RANDOMNESS_SLOWDOWN = 2


class Vertex:
    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y
        self.edges: dict[Vertex, Edge] = {}

    def __repr__(self):
        return f"({self.x}, {self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def add_edge(self, vertex: 'Vertex'):
        new_edge: Edge = Edge(self, vertex)
        self.edges[vertex] = new_edge
        vertex.edges[self] = new_edge

class Edge:
    def __init__(self, first: Vertex, second: Vertex):
        self.first: Vertex = first
        self.second: Vertex = second
        self.middle: Vertex = None

    def __repr__(self):
        return f"{self.first} - {self.second}"

    def __str__(self):
        return f"{self.first} - {self.second}"
    
    def split(self, randomness: int) -> Vertex:
        if self.middle:
            return self.middle
        
        midpoint = Vertex((self.first.x + self.second.x) / 2, (self.first.y + self.second.y) / 2)
        perpendicular = (self.second.y - self.first.y, self.first.x - self.second.x)
        lenght = (perpendicular[0]**2 + perpendicular[1]**2)**0.5   # normalizing
        perpendicular = (perpendicular[0]/lenght, perpendicular[1]/lenght)   # normalizing
        if randomness > 0:
            variance = random.randrange(-randomness//2, randomness//2) + random.randrange(-randomness//2, randomness//2)   # gaussian/normal distribution
            midpoint.x += perpendicular[0] * variance
            midpoint.y += perpendicular[1] * variance
        self.middle = midpoint

        self.first.add_edge(midpoint)
        midpoint.add_edge(self.second)

        return midpoint
    

    def draw(self):
        canvas.create_line(self.first.x, self.first.y, self.second.x, self.second.y, fill="white")


def mountain(left: Vertex, right: Vertex, top: Vertex, factor=height//2, levels=9, seed=1):
    leftEdge: Edge = left.edges.get(top)
    rightEdge: Edge = right.edges.get(top)
    bottomEdge: Edge = left.edges.get(right)

    if levels == 0:
        leftEdge.draw()
        rightEdge.draw()
        bottomEdge.draw()
        return

    random.seed(seed)

    if leftEdge.middle is None:
        leftEdge.split(factor)
    if rightEdge.middle is None:
        rightEdge.split(factor)
    if bottomEdge.middle is None:
        bottomEdge.split(factor)

    leftEdge.middle.add_edge(bottomEdge.middle)
    mountain(left, bottomEdge.middle, leftEdge.middle, factor//RANDOMNESS_SLOWDOWN, levels - 1, random.randint(1,1000)) # left
    random.seed(seed)
    bottomEdge.middle.add_edge(rightEdge.middle)
    mountain(bottomEdge.middle, right, rightEdge.middle, factor//RANDOMNESS_SLOWDOWN, levels - 1, random.randint(1001,2000)) # right
    random.seed(seed)
    leftEdge.middle.add_edge(rightEdge.middle)
    mountain(leftEdge.middle, rightEdge.middle, top, factor//RANDOMNESS_SLOWDOWN, levels - 1, random.randint(2001,3000)) # top
    random.seed(seed)
    mountain(leftEdge.middle, rightEdge.middle, bottomEdge.middle, factor//RANDOMNESS_SLOWDOWN, levels - 1, random.randint(3001,4000)) # middle


def run():
    canvas.create_rectangle(0,0,width,height,fill="black")

    try:
        randomn = int(randomness.get())
    except: randomn = 175

    random.seed()
    seed = random.randint(1,10000)

    for level in range(6, 10):
        canvas.delete("all")
        random.seed(seed)
        left: Vertex = Vertex(100, 600)
        right: Vertex = Vertex(1400, 600)
        top: Vertex = Vertex(750, 100)
        for first, second in ((left, right), (left, top), (right, top)):
            edge: Edge = Edge(first, second)
            first.edges[second] = edge
            second.edges[first] = edge

        mountain(left, right, top, randomn, level, seed)
        canvas.update()
        wait_button.wait_variable(var)
        # time.sleep(0.1)


randomness = tkinter.Entry(text="Enter positive number, default 180, randomness")
randomness.pack(side="left")

newMountain = tkinter.Button(text="New mountain", command=run)
newMountain.pack(side="left")

var = tkinter.IntVar()
wait_button = tkinter.Button(text="Next iteration", command=lambda: var.set(1))
wait_button.pack(side="left")

canvas.mainloop()
