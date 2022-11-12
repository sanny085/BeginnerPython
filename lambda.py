# Lambda function is an anonymous function
# It can take n number of arguments

x = lambda a, b: a * b
print(x(5, 6))


def calculator(a):
    return lambda n : n * a


parent = calculator(4)
print(parent(6))
