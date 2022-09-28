user1 = ['Ankit', 'Raja', 'Mohan', 'Raja', 'Suresh', 'Rahul', 'Rakesh', 'Ayan', ]
# user1.remove('Raja')

for x in user1:
    print('Slice the list value :', user1[1: len(user1)-1])
    if x == 'Raja':
        user1.remove(x)

print('All \'Raja\' name value removed', user1)

# Pop the value based on index
print(user1.pop(1))

# Pop the last index value
print(user1.pop())
print(user1)