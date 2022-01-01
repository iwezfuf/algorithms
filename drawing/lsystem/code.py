import turtle
import random

t = turtle.Turtle()
myWin = turtle.Screen()

turtle.tracer(0, 0)   # aby som nevidel ako to robi
t.hideturtle()
t.speed(10)

#t.goto(200,-500) # pise pritom ako ide na tu poziciu
#t.up() # nepise 
#t.down() # znova pise
#t.setheading(90) # aby zacala otocena hore, inak zacne otocena doprava

#turtle.colormode(255)
#t.pencolor((255,255,255))


def l_system(alphabet, axiom, rules, angle=90, iterations=4):
    steps = axiom
    for iteration in range(iterations):
        new_steps = []
        for letter in steps:
            for rule in rules:
                if letter in rule[0]:
                    if len(rule[1]) > 1:
                        new_steps.append(random.choices(rule[1][0], weights = rule[1][1], k = 1)[0])
                    elif type(rule[1][0]) == list:
                        new_steps.append(random.choice(rule[1][0]))
                    else:
                        new_steps.append(rule[1][0])
                    break
                        
                    
            else:
                new_steps.append(letter)
        steps = "".join(new_steps)

    stack = []
    for step in steps:
        if any([step == i for i in alphabet]):
            t.forward(5)
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
                

#l_system(["F", "G"], "F", [["F",[["F+G", "F+"], [0.995,0.005]]], ["G",["F-G"]]], 90, 10)
