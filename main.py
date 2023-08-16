def add(a, b):
    # Return the sum of a and b
    return a + b


def sub(a, b):
    # Return the difference between a and b
    return a - b


def mul(a, b):
    # Return the product of a and b
    return a * b


def div(a, b):
    # Return the quotient of a and b
    if b == 0:
        print('Invalid equation: Division by zero')
        return None
    return a / b


def mod(a, b):
    # Return the remainder of a divided by b
    if b == 0:
        print('Invalid equation: Modulo by zero')
        return None
    return a % b


def main():
    while True:
        eq = input('Enter equation: ')
        # Parse the equation to get the operator
        if '+' in eq:
            a, b = eq.split('+')
            answer = add(float(a), float(b))
        elif '-' in eq:
            a, b = eq.split('-')
            answer = sub(float(a), float(b))
        elif '*' in eq:
            a, b = eq.split('*')
            answer = mul(float(a), float(b))
        elif '/' in eq:
            a, b = eq.split('/')
            answer = div(float(a), float(b))
            if answer is None:
                continue
        elif '%' in eq:
            a, b = eq.split('%')
            answer = mod(float(a), float(b))
            if answer is None:
                continue
        else:
            print('Invalid equation, please try again with +, -, *, /, %')
            continue

       