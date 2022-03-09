def operate(n1, op, n2):
    num1 = int(n1)
    num2 = int(n2)
    ans = 0
    if op == '-':
        ans = num1 - num2
    elif op == '+':
        ans = num1 + num2
    elif op == '*':
        ans = num1 * num2
    elif op == '/':
        ans = int(num1 / num2)
    return ans

def evalRPN(tokens):
    if len(tokens) == 1:
        return int(tokens[0])
    stack = []
    for i, x in enumerate(tokens):
        if x not in '+-*/':
            stack.append(x)
        else:
            a = stack.pop()
            b = stack.pop()
            res = operate(b, x, a)
            if i != len(tokens) - 1:
                stack.append(res)
            else:
                return res

print(evalRPN(['18']))
print(evalRPN(['4', '13', '5', '/', '+']))
print(evalRPN(['10', '6', '9', '3', '+', '-11', '*', '/', '*', '17', '+', '5', '+']))
