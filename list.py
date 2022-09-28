user1 = ['Ankit', 'Raja', 'Mohan', 'Raja', 'Suresh']
# user1.remove('Raja')

for x in user1:
    if x == 'Raja':
        user1.remove(x)

print(user1)

# Pop the value based on index
print(user1.pop(1))
