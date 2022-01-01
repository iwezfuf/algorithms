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

    def implementRule(rule):
        if len(rule[1]) > 1:
            res = random.choices(rule[1][0], weights = rule[1][1], k = 1)[0]
        elif type(rule[1][0]) == list:
            res = random.choice(rule[1][0])
        else:
            res = rule[1][0]
        return res
    
    
    steps = axiom
    for iteration in range(iterations):
        new_steps = []
        for i in range(len(steps)):
            for rule in rules:
                if len(rule[0]) > 1:
                    try:
                        if rule[0] in steps[i-1]+"<"+steps[i]+">"+steps[i+1]:
                            new_steps.append(implementRule(rule))
                            break
                    except: pass
                        
                elif steps[i] == rule[0]:
                    new_steps.append(implementRule(rule))
                    break

                    
            else:
                new_steps.append(steps[i])
        steps = "".join(new_steps)

    stack = []
    for step in steps:
        if any([step == i for i in alphabet]):
            t.forward(10)
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

#t.left(90)
#l_system(["T", "R", "L", "F"], "T", [["T",["R+[T]--[--L]R[++L]-[T]++T"]], ["R",["F[--L][++L]F"]], ["R",["[+FX-FX-FX+I+FX-FX-FX]"]], ["F>X",["FX"]], ["F",["FF"]]], 30, 4)
