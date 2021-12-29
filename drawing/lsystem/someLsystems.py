import turtle
import random

t = turtle.Turtle()
myWin = turtle.Screen()

#turtle.tracer(0, 0)
#t.hideturtle()
t.speed(10)

t.goto(200,-500)

##turtle.colormode(255)
##t.pencolor((255,255,255))


def l_system(alphabet, axiom, rules, angle=90, iterations=4):
    steps = axiom
    for iteration in range(iterations):
        new_steps = []
        for letter in steps:
            for rule in rules:
                if letter in rule[0]:
                    new_steps.append(rule[1])
                    break
            else:
                new_steps.append(letter)
        steps = "".join(new_steps)

    stack = []
    for step in steps:
        if any([step == i for i in alphabet]):
            t.forward(2)
        elif step == "+":
            t.left(angle)
        elif step == "-":
            t.right(angle)
        elif step == "[":
            stack.append([t.pos(), t.heading()])
        elif step == "]":
            t.up()
            pos, heading = stack.pop()
            t.goto(pos)
            t.setheading(heading)
            t.down()
                


#l_system([F,G], F, [[F,F+G], [G,F-G]], 90, 5)
#l_system(["F", "G"], "F", [["F","F+G"], ["G","F-G"]], 90, 10)    # Dragon curve
#l_system(["F"], "F--F--F", [["F","F+F--F+F"]], 60, 4)        # Koch snowflake
#l_system(["F"], "F+F+F+F", [["F","F-F+F+FFF-F-F+F"]], 90, 3)   # Quadratic-Koch-Island
#l_system(["F"], "F", [["F","+F--F+"]], 45, 10)    # Levy curve
#l_system(["F"], "F+F+F+F", [["F","FF+F-F+F+FF"]], 90, 4)    # Tiles
#l_system(["F"], "F+F+F+F", [["F","FF+F+F+F+F+F-F"]], 90, 4)   # Rings


#l_system(["F"], "F", [["F", "F+F-F-F+F"]], 90, 6)

 
# More l-system formulas for fractals: https://elc.github.io/posts/plotting-fractals-step-by-step-with-python/

##t.up()
##t.right(90)
#t.forward(500)
##t.left(180)
##l_system(["X", "F"], "X", [["X", "F+[[X]-X]-F[-FX]+X"], ["F", "FF"]], 25, 7)  # Fractal plant
##t.up()
##t.setheading(0)
##t.forward(100)
##t.down()
#t.setheading(90)
#l_system(["X", "F"], "X", [["X", "F+[[X]-X]-F[-FX]+X"], ["F", "FF"]], 25, 7)

#l_system(["F", "G"], "F++F++F++F++F", [["F","F+++++++++++++++++FFFFF++++F"]], 36, 4)

#l_system(["F", "G"], "F++F++F++F++F", [["F","F++++++++++++++++++++FFFFF++++F"]], 85, 4)

#l_system(["F", "G"], "F", [["F","F+F--F+F"]], 60, 4) #Koch curve
# l_system(["F"], "A", [["A","-BF+AFA+FB-"], ["B", "+AF-BFB-FA+"]], 90, 4)   # Hilbert curve
