class Stack():
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


def parChecker(string):
    stack = Stack()
    valid = True
    index = 0
    while index < len(string) and valid:
        symbol = string[index]
        if symbol in "([{":
            stack.push(symbol)
        else:
            if stack.isEmpty():
                valid = False
            else:
                top = stack.pop()
                if not matches(symbol, top):
                    valid = False
        index += 1

    if valid and stack.isEmpty():
        return True
    else: return False


def matches(rightpar, leftpar):
    opens = "([{"
    closers = ")]}"
    return opens.index(leftpar) == closers.index(rightpar)


def infixtopostfix(infix):
    prec = {"**":4, "*":3, "/":3, "+":2, "-":2, "(":1}
    operands = Stack()
    postfix = []
    for char in infix.split():
        if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or char in "0123456789":
            postfix.append(char)
        elif char == "(":
            operands.push(char)
        elif char == ")":
            top = operands.pop()
            while top != "(":
                postfix.append(top)
                top = operands.pop()
        else:
            while not operands.isEmpty() and (prec[operands.peek()] > prec[char]):
                postfix.append(operands.pop())
            operands.push(char)

    while not operands.isEmpty():
        postfix.append(operands.pop())
    return " ".join(postfix)



def postfixEval(postfix):
    operands = Stack()
    for char in postfix.split():
        if char in "0123456789":
            operands.push(int(char))
        else:
            operand2 = operands.pop()
            operand1 = operands.pop()
            operands.push(doMath(char, operand1, operand2))
    return operands.pop()

def doMath(op, op1, op2):
    if op == "*":
        return op1*op2
    elif op == "/":
        return op1/op2
    elif op == "+":
        return op1+op2
    else: return op1-op2
