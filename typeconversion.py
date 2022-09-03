import random
print(random.randrange(1, 10))
firstNum = input("Tell me first number : ")
lastNum = input("Tell me last number : ")
Sum = int(firstNum) + int(lastNum)
print("Sum of digit of number is :", Sum)

# get person details
name = input("Enter your Name : ")
age = input("Enter your Age : ")
mentalHealth = input('Enter mental health of Candidate : ')

print(name, 'is', age, 'year olds', mentalHealth)

is_mental_ok = True
if mentalHealth == "Genius":
    is_mental_ok = True
else:
    is_mental_ok = False

print('Mental health of candidate is :', is_mental_ok)