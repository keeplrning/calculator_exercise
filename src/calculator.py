operations = {
    "+" : (lambda x, y : x + y),
    "-" : (lambda x, y : x - y),
    "*" : (lambda x, y : x * y),
    "/" : (lambda x, y : x / y)
    }


def calculate_pre(expression):

    def calculate(tokens):
        token = tokens[0]
        del tokens[0]
        if token == '+':
            return calculate(tokens) + calculate(tokens)
        elif token == '-':
            return calculate(tokens) - calculate(tokens)
        elif token == '*':
            return calculate(tokens) * calculate(tokens)
        elif token == '/':
            return calculate(tokens) / calculate(tokens)
        else:
            return int(token)

    toks = expression.split()
    return calculate(toks)


def calculate_infix(expression):

    def evaluate_expr(stack):
        res = stack.pop() if stack else 0
        while stack and stack[-1] != ')':
            sign = stack.pop()
            if sign == '+':
                res += stack.pop()
            elif sign == '-':
                res -= stack.pop()
            elif sign == '*':
                res *= stack.pop()
            else:
                res /= stack.pop()
        return res

    def calculate():
        stack = []
        n, operand = 0, 0
        for i in range(len(expression) - 1, -1, -1):
            ch = expression[i]
            if ch.isdigit():
                operand = (10**n * int(ch)) + operand
                n += 1
            elif ch != ' ':
                if n:
                    stack.append(operand)
                    n, operand = 0, 0
                if ch == '(':
                    res = evaluate_expr(stack)
                    stack.pop()
                    stack.append(res)
                else:
                    stack.append(ch)
        if n:
            stack.append(operand)
        return evaluate_expr(stack)
    return calculate()
