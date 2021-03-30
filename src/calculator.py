operations = {
    "+" : (lambda x, y : x + y),
    "-" : (lambda x, y : x - y),
    "*" : (lambda x, y : x * y),
    "/" : (lambda x, y : x / y)
    }

def calculate_pre(expression) :
    tokens = expression.split()
    store = []
    
    for token in reversed(tokens) :
        if token in operations :
            arg_1 = store.pop()
            arg_2 = store.pop()
            
            result = operations[token](arg_1, arg_2)
            store.append(result)
        else :
            store.append(int(token))

    return store.pop()
        