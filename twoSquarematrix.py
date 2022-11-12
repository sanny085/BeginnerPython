"""
Input: matrixA = {{1, 2}, {3, 4}},
matrixB = {{4, 3}, {2, 1}}
Output: {{5, 5}, {5, 5}}
"""

matrixA = [[1, 2], [3, 4]]
matrixB = [[4, 3], [2, 1]]


def addition(matrixA, matrixB):
    sumMatrix = []
    for x in range(len(matrixA)):
        sumMatrix.append([])
        for y in range(len(matrixB)):
            addition = matrixA[x][y] + matrixB[x][y]
            print(addition)
            sumMatrix[x].insert(y, addition)

    return sumMatrix


finalMatrix = addition(matrixA, matrixB)
print("Result : ", finalMatrix)
# Output: [[5, 5], [5, 5]]
