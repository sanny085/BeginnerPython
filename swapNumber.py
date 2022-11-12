# Swap value without two variable
n1 = int(input('Enter first number : '))
n2 = int(input('Enter second number : '))
x, y = n1, n2
p, q = x, y
print(n1, n2)
n1 = n1 + n2
n2 = n1 - n2
n1 = n1 - n2
print('Without third variable', n1, n2)

# Simple way
x,  y = y, x
print('Simple way', x, y)


# Swap value with more than two variable
temp = p
p = q
q = temp
print('With third var', p, q)






