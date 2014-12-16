class Operand:
    def __init__(self, opStr):
        self.opStr = opStr

def calcrpn(instr):
    stack = []
    for i in instr:
        if i >= 0 and i < 999:
            stack.append(i)
        elif i == '+':
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append(op2 + op1)
        elif i == '-':
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append(op2 - op1)
        elif i == '*':
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append(op2 * op1)
        elif i == '/':
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append(op2 / op1)
        elif i == '^':
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append(op2 ** op1)
    return stack

print calcrpn([24.0, 3.0, '/'])
