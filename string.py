name = "Sanny Kumar"
print(name.upper())
print(name)
print('Find out the length of name :', len(name))

str1 = "Hello, World"
print('Array of value by index', str1[1])

# string in - Looping of string
for x in str1:
    print(x, '\t')
print('Hello\tWorld')


# string in - Check string is available or not
description = "India is our country"
print("country" in description)
print('Length of description is : ', len(description))
descSplit = description.split()
print(descSplit, descSplit[0])


# string in -
if "Ctry" in description:
    print('yes it available')
else:
    print('it\'s not available')

# string not in
allGame = 'Football, Cricket, Football, Football'
if 'masic' not in allGame:
    print('Not Available here', allGame)
    customize = allGame.replace('Football', 'Hockey')

    print(customize)
    print(allGame)
    print(allGame.split(','))
    print(allGame.count('Football'))

# String method
str2 = 'Namaste python {} , Here total is {} cow'
print(str2[3:8])  # Slicing string
print(str2.format(2, 16))
print(str2.find('t'))
print(str2.index('t'))


