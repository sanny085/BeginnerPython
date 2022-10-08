# Tuple has two method index and count
# We can not update or change tuple directly - Need to take help of list

vowel = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
vow = con = 0
print('Initial vow and cons : ', vow, ':', con)
print('Zeroth index : ', vowel[4])

# Find out total vowel and consonant in word
word = input("Enter some word : ")
for x in word.replace(" ", ""):
    if x in vowel:
        vow += 1
    else:
        con += 1
print('Total length of word is : ', len(word.replace(" ", "")), '\nVowel is : ', vow, '\nConsonant is : ', con)

# Update the tuple index by using list
user = ('Sanny', 'Mohit', 'Rakesh', 'Himanshu')
print(user[1:3])  # slice the tuple
newUser = list(user)  # []
newUser.append('Rohit')
print(newUser)

newUser[0] = 'Raja'
user = tuple(newUser)  # ()
print(user)

# print all candidate name
for x in user:
    print(x)

# get value by using index
i = 0
while i < len(list(user)):
    print(user[i])
    i += 1


# Unpack tuple
user = ('Raja', 'Mohit', 'Rakesh', 'Deepak', 'Sanny')

firstName, secondName, *restName = user
print('First Name : ', firstName)
print('Second Name : ', secondName)
print('Rest of s;l name', restName)







