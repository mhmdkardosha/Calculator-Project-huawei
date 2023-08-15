def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        print('Invalid equation: Division by zero')
        return None
    return a / b

def mod(a, b):
    if b == 0:
        print('Invalid equation: Modulo by zero')
        return None
    return a % b

def main():
    while True:
        eq = input('Enter equation: ')
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

        print('Answer:', answer)
        ans = input('Do you want to continue? (y/n): ')
        while ans not in ['y', 'n']:
            print('Invalid answer, please try again with y or n')
            ans = input('Do you want to continue? (y/n): ')
        if ans == 'n':
            print('Thank you for using our calculator')
            break

if __name__ == '__main__':
    main()
