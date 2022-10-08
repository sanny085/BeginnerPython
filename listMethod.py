valueCollector = []
position, value = input('Enter position and value : ').split(" ")

print("position and value", position, value)

valueCollector.insert(0, 5)
valueCollector.insert(1, 10)
valueCollector.insert(0, 6)


print('List :', valueCollector)
valueCollector.remove(6)

print('List :', valueCollector)
