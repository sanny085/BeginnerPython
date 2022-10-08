# Remove all duplicate value
number = [10, 20, 19, 10, 26, 19, 26]
filterValue = []
for x in number:
    if x not in filterValue:
        filterValue.append(x)

# approach 1
filterValue.sort(reverse = True)
print('All filter value : ', filterValue)
# approach 2
print('All filter by set data type', list(set(number)))



# Sort the list
value = [12, 2, 45, 36, 10, 112, 9, 56, 78]
# value.sort()
print('Value sorted', value)
for x in range(len(value)):
    for y in range(len(value)):
        if value[x] < value[y]:
            temp = value[x]
            value[x] = value[y]
            value[y] = temp
            print(x, y, '1st section :', value)


print('Final Sorted value :', value)
