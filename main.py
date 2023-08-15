def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


def mod(a, b):
    return a % b


if __name__ == '__main__':
    eq = input('Enter equation: ')
    while True:
        answer = 0
        if '+' in eq:
            a, b = eq.split('+')
            answer += add(float(a), float(b))
        elif '-' in eq:
            a, b = eq.split('-')
            answer += sub(float(a), float(b))
        elif '*' in eq:
            a, b = eq.split('*')
            answer += mul(float(a), float(b))
        elif '/' in eq:
            a, b = eq.split('/')
            if b == '0':
                print('Invalid equation')
                continue
            answer += div(float(a), float(b))
        elif '%' in eq:
            a, b = eq.split('%')
            answer += mod(float(a), float(b))
        else:
            print('Invalid equation, please try again with +, -, *, /, %')
            continue
        print('Answer: ' + str(answer))
        ans = input('Do you want to continue? (y/n): ')
        while True:
            if ans == 'y':
                eq = input('Enter equation: ')
                break
            elif ans == 'n':
                print('Thank you for using our calculator')
                exit()
            else:
                print('Invalid answer, please try again with y or n')
                ans = input('Do you want to continue? (y/n): ')
                continue
