number = int(input("Enter your number"))

i = number
rev = 0
while i > 0:
    rev = int(rev*10) + int(i % 10)
    print('rev', rev)
    i //= 10

print("Reverse of number is  : ", rev)