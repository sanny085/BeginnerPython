def calculator(num1, num2, sign):
    if sign == '+':
        return add(num1, num2)
    elif sign == '-':
        return sub(num1, num2)
    elif sign == '*':
        return mul(num1, num2)
    elif sign == '/':
        return dev(num1, num2)
    elif sign == '%':
        return mod(num1, num2)
    else:
        return 'EnValid operation'


def add(num1, num2):
    return num1+num2


def sub(num1, num2):
    return num1-num2


def mul(num1, num2):
    return num1*num2


def dev(num1, num2):
    return num1/num2


def mod(num1, num2):
    return num1 % num2


num1 = int(input('Enter your num1 '))
num2 = int(input('Enter your num2 '))
sign = input('Enter your operator \'+, -, *, /, %\' ')
if num1 and num2:
    print(num1, num2, sign)
    output = calculator(num1, num2, sign)
    print('Result is : ', output)

