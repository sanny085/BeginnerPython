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


# Remove all duplicate value
number = [10, 20, 19, 10, 26, 19, 26]
filterValue = []
for x in number:
    if x not in filterValue:
        filterValue.append(x)

# approach 1
print('All filter value : ', filterValue)
# approach 2
print('All filter by set data type', list(set(number)))

# List comprehension
rangeBefore = [x for x in range(10) if x < 5]
print(rangeBefore)

fruits = ['apple', 'mango', 'banana', 'apple', 'mango', 'apple']
filterFruitName = [y.upper() for y in fruits if y != 'apple']
print(filterFruitName)

# Sort the list
value = [12, 2, 45, 36, 10, 9, 56, 78]
# value.sort()
print('Value sorted', value)
for x in range(len(value)):
    y = int(x)+1
    for y in range(len(value)):
        if value[x] > value[y]:
            temp = value[x]
            value[x] = value[y]
            value[y] = temp


print('Final Sorted value :', value)





