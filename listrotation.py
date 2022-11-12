arr1 = [2, 4, 6, 7, 1, 5, 9]
position = int(input("Enter index for rotating : "))

"""
i = 0
newList : []
while  i < len(arr1):
"""
print("Current array : ", arr1)
newList = arr1[position:len(arr1)]
newList.extend(arr1[0:position])

print("Rotated Array Value :", newList)

print('Slice value is :', arr1[0:2])