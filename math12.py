import random

# Square root of number
number = 16
print(number ** 0.5)

# Exponential Operator
m = 3
n = 2
print(m ** n)

n = 8
srt_root = n ** 0.5
print('The square root of %0.4f is %0.3f' % (n, srt_root))

# Random number from given range
number = int(input('Enter the number for range : '))
print('Random number 1 : ', random.randrange(1, number))
print('Random number 2 : ', random.randint(1, number))

# Kilometer to meter
kilometer = int(input('Enter km : '))
print('%d in meter is : %d ' % (kilometer, kilometer * 1000))

# 1. Max Number from the three number
number = 14, 45, 10, 20, 78, 56, 58
number = list(number)
print(number)
print(len(number))
greaterNumber = 0
i = j = 0
while i < len(number):
    if greaterNumber < number[i]:
            greaterNumber = number[i]
            print('Greater', i, greaterNumber)
    i += 1

print('Greater number is 1 : ', greaterNumber)


# 2. Max Number from the three number
def maxTwoNumber(x, y):
    if x > y:
        return x
    else:
        return y


def maxNumber(a, b, c):
    return maxTwoNumber(a, maxTwoNumber(b, c))


a, b, c = input('First Number : ').split(" ")
output = maxNumber(int(a), int(b), int(c))
print(type(int(a)))
print('Greater number is 2 : ', output)
