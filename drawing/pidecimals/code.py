import turtle

with open("pi.txt", "r") as f:
    pi = f.readline()
t = turtle.Turtle()
myWin = turtle.Screen()
myWin.screensize(1000,1000)

turtle.tracer(0, 0)
t.hideturtle()
t.speed(1000)
t.up()
t.goto(0, 0)
t.down()

for i in pi:
    t.setheading(36*int(i))
    t.forward(0.4)

turtle.getscreen().getcanvas().postscript(file='image.ps')
myWin.mainloop()
