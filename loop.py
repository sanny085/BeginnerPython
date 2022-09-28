# while loop
i = 1
# example 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
print('\n')

# example 2
j = 0
while j < 5:
    j += 1
    if j == 3:
        continue
    print(j)

# example 3
table = 3
i = 1
while i <= 10:
    print('Table of ', table, 'X', i, ':', i*table)
    i += 1

# example 4 - pattern printing
k = 1
while k <= 10:
    print(k * "*")
    k += 1
# example 5 - pattern printing
for x in range(6):
    print(x)
    print(x * "*")


# For loop 1
fruits = ['apple', 'banana', 'mango', 'animal', 'milk']
for x in fruits:
    if x == 'animal':
        continue
    print(x)

name = 'Sanny'
for x in name:
    print(x)

# For loop 2
age = [78, 74, 56, 34, 12, 10, 8, 3, 2, 1]
for x in age:
    if x > 18:
        print('Valid age is :', x)
    elif x < 18 and x > 3:
        continue
    else:
        print('You are very kid', x)

# range
number = 5
for x in range(number):
    print('our range is ', x)

# range by 3rd parameter
for x in range(3, 30, 2):
    print('Number incremented by 2 ', x)

# Find vowel in name
name = input('Enter your name : ')
vowel = ['a', 'e', 'i', 'o', 'u']
countVowel = 0
countConso = 0

for x in name.replace(" ", ""):
    if x in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
        # x in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        countVowel += 1
        print('This letter is vowel : ', x)
    else:
        countConso += 1
        print('This is consonant', x)


print('String is :', name)
print('Length of string is : ', len(name.replace(" ", "")), 'Vowel is :', countVowel, 'Consonant is :', countConso)



