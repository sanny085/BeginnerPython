# it is order and changeable, does not allow duplicate

# keys(), values(), items()
user = {
    "name": 'Sanny',
     "age": 23,
    "address": "Bhramarpur"
}
print(user)
user['roll'] = 52
if "roll" in user:
    print(user)

# Only we will get keys
for x in user:
    print(x)
print('\n')
# Only we will get value
for x in user:
    print(user[x])

for x in user.values():
    print(x)

# Replace key value pair
for x, y in user.items():
    """items will change dict into tuple base on index [("name" : "Sanny"),(..),(..)]"""
    print('\'', y, '\' : \'', x, '\'')

# update the dict property
user.update({"salary" : "10"})
print(user)

# Pop item from dict -> last value
user.popitem()
print(user)

# delete item based on property name
user.pop('address')
print(user)
del user['age']
print(user)

# Copy of previous dict
print(user)
copyItems = user.copy()
copyItems['rollNumber'] = 'We are items'

print()
print(copyItems)

