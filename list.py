user1 = ['Ankit', 'Raja', 'Mohan', 'Raja', 'Suresh', 'Rahul', 'Rakesh', 'Ayan']
# user1.remove('Raja')
print(user1, len(user1))
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
# List comprehension
rangeBefore = [x for x in range(10) if x < 5]
print(rangeBefore)

fruits = ['apple', 'mango', 'banana', 'apple', 'mango', 'apple']
filterFruitName = [y.upper() for y in fruits if y != 'apple']
print(filterFruitName)
print('Total Number of apple is : ', fruits.count('apple'))


branch = ['suzuki', 'maruti', 'suzuMami']
print(branch.index('suzuki'))
