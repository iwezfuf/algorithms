def toBase(n, base):
    symbols = "0123456789ABCDEF"
    if n < base:
        return symbols[n]
    else: return toBase(n//base, base) + symbols[n%base]


def reverse(s):
    if len(s) < 1:
        return s
    return reverse(s[1:]) + s[0]


def palindrome(s):
    if len(s) < 1:
        return True
    if s[0] == s[-1]:
        return palindrome(s[1:-1])
    else: return False



import turtle
import random

##t = turtle.Turtle()
##myWin = turtle.Screen()

def drawSpiral(myTurtle, lineLen):
    if lineLen > 0:
        myTurtle.forward(lineLen)
        myTurtle.right(90)
        drawSpiral(myTurtle,lineLen-5)

def tree(t, branchLen, width):
    t.width(max(1,width))
    branchLen *= random.randint(95,100)/100
    if branchLen > 5:
        if branchLen < 15:
            t.color("green")
        else: t.color("brown")
        randangle = random.randint(95,105)/100
        t.forward(branchLen)
        t.right(20*randangle)
        tree(t, branchLen-10, width-random.randint(1,100)/40)
        t.left(40*randangle)
        tree(t, branchLen-10, width-random.randint(1,100)/40)
        t.right(20*randangle)
        t.penup()
        t.backward(branchLen)
        t.pendown()

#turtle.tracer(0, 0)
##t.penup()
##t.left(90)
##t.backward(200)
##t.speed(10000)
##t.width(15)
##t.pendown()
##t.color("brown")
###tree(t, 100, 15)
##
##
##t.width(1)

def drawTriangle(points, color, t):
    p1, p2, p3 = points
    t.fillcolor(color)
    t.up()
    t.goto(p1[0],p1[1])
    t.down()
    t.begin_fill()
    t.goto(p2[0],p2[1])
    t.goto(p3[0],p3[1])
    t.goto(p1[0],p1[1])
    t.end_fill()

    
def getMid(point1, point2):
    return ((point1[0]+point2[0])/2, (point1[1]+point2[1])/2)

def sierpinski(points, degree, t):
    colors = ['blue','red','green','white','yellow','violet','orange']
    drawTriangle(points, colors[degree], t)
    left, top, right = points
    if degree > 0:
        sierpinski([getMid(left, top), top, getMid(top, right)], degree-1, t)
        sierpinski([left, getMid(left,top), getMid(left,right)], degree-1, t)
        sierpinski([getMid(left,right), getMid(top,right), right], degree-1, t)
        
        
#sierpinski([[-200,-150],[0,100],[200,-150]], 5, t)




##myWin.exitonclick()


def makeChange(coins, value):
    minlist = [0]*(value+1)
    lastcoins = [0]*(value+1)
    for cents in range(1, value+1):
        coinCount = cents
        lastcoin = 1
        for coin in [i for i in coins if i <= cents]:
            if minlist[cents-coin]+1 < coinCount:
                coinCount = minlist[cents-coin]+1
                lastcoin = coin
        minlist[cents] = coinCount
        lastcoins[cents] = lastcoin

    coins = []
    while value > 0:
        lastcoin = lastcoins[value]
        coins.append(lastcoin)
        value -= lastcoin
    print("Min amount of coins:",len(coins), "\nCoins: ", *coins)


#makeChange([1,5,10,25], 162)


def factorial(n):
    if n <= 1:
        return 1
    else: return factorial(n-1)*n

#print(factorial(5))
    


##t = turtle.Turtle()
##myWin = turtle.Screen()
##
###turtle.tracer(0, 0)
##t.penup()
##t.left(90)
##t.backward(200)
##t.speed(1)
###t.width(15)
##t.pendown()
###t.color("brown")


#t.width(1)


def someCircles(n):
    t.circle(n)
    if n > 5:
        t.up()
        t.right(90)
        t.forward(n/2)
        t.left(90)
        t.down()
        someCircles(n/2)
        t.up()
        t.left(90)
        t.forward(n/2)
        t.left(90)
        t.down()
        t.up()
        t.left(90)
        t.forward(n)
        t.right(90)
        t.down()
        someCircles(n/2)
        t.up()
        t.right(90)
        t.forward(n)
        t.left(90)
        t.down()

##t.up()
##t.goto(0,0)
##t.down()

def cantor(n):
    t.down()
    if n > 1:
        t.right(90)
        t.forward(n)
        t.left(180)
        t.forward(n/3)
        t.up()
        t.right(270)
        t.forward(20)
        t.right(180)
        cantor(n/3)
        t.up()
        t.left(90)
        t.forward(n/3*2)
        t.right(90)
        cantor(n/3)
        t.up()
        t.forward(20)
        t.down()

#cantor(500)


##t.right(90)
def koch(n):
    if n > 20:
        koch(n/3)
        t.left(60)
        koch(n/3)
        t.right(120)
        koch(n/3)
        t.left(60)
        koch(n/3)
    else:
        t.forward(n/3)
        
        
##for i in range(3):
##    koch(1000)
##    t.right(120)

##t.down()
#t.left(90)

def hilbertCurve(n, angle=90, size=5):
    if n:
        t.right(angle)
        hilbertCurve(n-1, -angle)
        t.forward(size)
        t.left(angle)
        hilbertCurve(n-1, angle)
        t.forward(size)
        hilbertCurve(n-1, angle)
        t.left(angle)
        t.forward(size)
        hilbertCurve(n-1, -angle)
        t.right(angle)
        
#hilbertCurve(5)


def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else: return fib(n-1) + fib(n-2)

#print(fib(9))


#t.up()
#t.goto(0,0)
#t.down()


#t.right(90)

##t.goto(200,-500)
##t.begin_fill()
##t.circle(1000)
##t.end_fill()
##
##t.up()
##t.goto(0,0)
###t.right(90)
##t.down()
##t.hideturtle()
##turtle.colormode(255)
##t.pencolor((255,255,255))

def dragonCurve(n, size=200, angle=90):
    if n:
        t.right(angle/2)
        dragonCurve(n-1, size/1.41421356237, 90)
        t.left(angle)
        dragonCurve(n-1, size/1.41421356237, -90)
        t.right(angle/2)
    else: t.forward(size)

#turtle.tracer(0, 0)

#dragonCurve(10)
import time
##t.speed(2)

def gosperCurve(n, size=150, angle=60, ang=0, noi=60):
##    if n:
##        t.right(ang)
##        gosperCurve(n-1, size/2, 60)
##        t.left(60)
##        if angle == 60:
##            gosperCurve(n-1, size/2, -60)
##        else:
##            gosperCurve(n-1, size/2, -60)
##            gosperCurve(n-1, size/2, -60)
##        t.left(120)
##        gosperCurve(n-1, size/2, -60, 60)
##        t.right(angle)
##        gosperCurve(n-1, size/2, 60)
##        t.right(120)
##        if angle == 60:
##            gosperCurve(n-1, size/2, 60, -60)
##            gosperCurve(n-1, size/2, 60, -60)
##        else: gosperCurve(n-1, size/2, 60, -60)
##        t.right(60)
##        gosperCurve(n-1, size/2, -60)
##
##        
##    else:
##        t.forward(size)

##    if n:
##        t.color("orange")
##        gosperCurve(n-1, size/2)
##        t.color("blue")
##        if angle == 60:
##            gosperCurve(n-1, size/2, -60, 60)
##        else:
##            gosperCurve(n-1, size/2, -60, 60)
##            gosperCurve(n-1, size/2, -60)
##        t.left(180)
##        t.color("green")
##        gosperCurve(n-1, size/2, -60, -60)
##        #t.right(angle)
##        t.color("brown")
##        gosperCurve(n-1, size/2, 60, -angle)
##        t.right(120)
##        t.color("red")
##        if angle == 60:
##            gosperCurve(n-1, size/2, -60)
##            gosperCurve(n-1, size/2, -60)
##        else: gosperCurve(n-1, size/2, -60)
##        t.right(180)
##        t.color("black")
##        gosperCurve(n-1, size/2, 60, 120)
##        t.left(60)
##
##        
##    else:
##        t.left(ang)
##        t.forward(size)


    if n:
        gosperCurve(n-1, size/2, angle, 60)
        #t.left(60)
        if angle == 60:
            gosperCurve(n-1, size/2, -angle, 120)
        else:
            gosperCurve(n-1, size/2, -angle)
            gosperCurve(n-1, size/2, -angle, 120)
        #t.left(120)
        gosperCurve(n-1, size/2, -angle, -angle, -60)
        #t.right(angle)
        gosperCurve(n-1, size/2, angle, -120)
        #t.right(120)
        if angle == 60:
            gosperCurve(n-1, size/2, angle)
            gosperCurve(n-1, size/2, angle, -60, -60)
        else: gosperCurve(n-1, size/2, angle, -60, -60)
        #t.right(60)
        gosperCurve(n-1, size/2, angle, noi)
        #t.left(60)

        
    else:
        t.forward(size)
        t.left(ang)


#gosperCurve(2)



##myWin.exitonclick()
        
"""
Write a program to solve the following problem:
You have two jugs: a 4-gallon jug and a 3-gallon jug.
Neither of the jugs have markings on them.
There is a pump that can be used to fill the jugs with water.
How can you get exactly two gallons of water in the 4-gallon jug?
"""

def jugs(jug1, jug2, n, first=0, second=0, tried=[]):
    if first == n or second == n:
        print(first, second)
        return True

    if [first,second] in tried:
        return False
    print(first, second)

    tried.append([first, second])
        
    if jugs(jug1, jug2, n, max(0, first-(jug2-second)), min(jug2, second+first), tried) \
       or jugs(jug1, jug2, n, min(jug1, first+second), max(0, second-(jug1-first)), tried) \
       or jugs(jug1, jug2, n, jug1, second, tried) \
       or jugs(jug1, jug2, n, first, jug2, tried) \
       or jugs(jug1, jug2, n, 0, second, tried) \
       or jugs(jug1, jug2, n, first, 0, tried):
        return True

#jugs(4, 5, 3)


"""
Write a program that solves the following problem:
Three missionaries and three cannibals come to a river and find a boat that holds two people.
Everyone must get across the river to continue on the journey.
However, if the cannibals ever outnumber the missionaries on either bank, the missionaries will be eaten.
Find a series of crossings that will get everyone safely to the other side of the river.
"""


def river(shore1=[3,3], shore2=[0,0], tried=[]):
    #print(shore1, shore2)
    
    if [shore1, shore2] in tried:
        return False

    if shore1[1] > shore1[0] and shore1[0]:
        return False
    if shore2[1] > shore2[0] and shore2[0]:
        return False

    print(shore1, shore2)

    if sum(shore2) == 6:
        return True
        
    tried.append([shore1, shore2])

    return river([shore1[0], max(0, shore1[1]-1)], [shore2[0], shore2[1]+min(1, shore1[1])], tried) or \
       river([shore1[0], shore1[1]+min(1, shore2[1])], [shore2[0], max(0, shore2[1]-1)], tried) or \
       river([max(0, shore1[0]-1), shore1[1]], [shore2[0]+min(1, shore1[0]), shore2[1]], tried) or \
       river([shore1[0]+min(1, shore2[0]), shore1[1]], [max(0, shore2[0]-1), shore2[1]], tried) or \
       river([shore1[0], max(0, shore1[1]-2)], [shore2[0], shore2[1]+min(2, shore1[1])], tried) or \
       river([shore1[0], shore1[1]+min(2, shore2[1])], [shore2[0], max(0, shore2[1]-2)], tried) or \
       river([max(0, shore1[0]-2), shore1[1]], [shore2[0]+min(2, shore1[0]), shore2[1]], tried) or \
       river([shore1[0]+min(2, shore2[0]), shore1[1]], [max(0, shore2[0]-2), shore2[1]], tried) or \
       river([max(0, shore1[0]-1), max(0, shore1[1]-1)], [shore2[0]+min(1, shore1[0]), shore2[1]+min(1, shore1[1])]) or \
       river([shore1[0]+min(1, shore2[0]), shore1[1]+min(1, shore2[1])], [max(0, shore2[0]-1), max(0, shore2[1]-1)])


#river()


"""
Suppose you are a computer scientist/art thief who has broken into a major art gallery.
All you have with you to haul out your stolen art is your knapsack which only holds W pounds of art,
but for every piece of art you know its value and its weight.
Write a dynamic programming function to help you maximize your profit.
Here is a sample problem for you to use to get started:
Suppose your knapsack can hold a total weight of 20. You have 5 items as follows:

item     weight      value
  1        2           3
  2        3           4
  3        4           8
  4        5           8
  5        9          10
"""

items = [[2,3], [3,4], [4,8], [5,8], [9,10]]

def knapsack(max_weight):
    best = [[0,[]]]*(max_weight+1)
    for weight in range(1, max_weight+1):
        for i in range(len(items)):
            if items[i][0] <= weight and i+1 not in best[weight-items[i][0]][1]:
                val = best[weight-items[i][0]][0] + items[i][1]
                if val > best[weight][0]:
                    best[weight] = [val,best[weight-items[i][0]][1]+[i+1]]
    return best[max_weight]


#print(knapsack(20))


"""
This problem is called the string edit distance problem, and is quite useful in many areas of research.
Suppose that you want to transform the word “al*g/orithm” into the word “alligator.”
For each letter you can either copy the letter from one word to another at a cost of 5,
you can delete a letter at cost of 20, or insert a letter at a cost of 20.
The total cost to transform one word into another
is used by spell check programs to provide suggestions for words that are close to one another.
Use dynamic programming techniques to develop an algorithm that gives you the smallest edit distance between any two words.
"""


def stringEditDistance(word1, word2, cost=0, tried=[]):
    if word1 == word2:
        return cost

    if [word1, word2] in tried:
        return ##
    
    tried.append([word1, word2])
    
    costs = []
    for i in range(len(word1)):
        costs.append(stringEditDistance(word1[:i]+word1[i+1:], word2, cost+20, tried))

        abc = list(word2)
        
        if len(word2) > i:
            costs.append(stringEditDistance(word1[:i]+word2[i]+word1[i+1:], word2, cost+5, tried))

            
        for letter in abc:
            costs.append(stringEditDistance(word1[:i]+letter+word1[i:], word2, cost+20, tried))
    
    cost += min(costs, default=0)

    return cost



#print(stringEditDistance("aligator", "alligator"))
