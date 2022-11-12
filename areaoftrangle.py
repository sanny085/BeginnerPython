# Semi Perimeter of the triangle
# s = 1/2*(a+b+c)
# area = (s(s-a)(s-b)(s-c)) ** 0.5
s1 = int(input('Enter first side of triangle'))
s2 = int(input('Enter second side of triangle'))
s3 = int(input('Enter three side of triangle'))

s = int((s1+s2+s3)/2)
print('Perimeter is ', s)

area = (s*(s-s1)*(s-s2)*(s-s3)) ** 0.5
print('Area of triangle is ', area)
