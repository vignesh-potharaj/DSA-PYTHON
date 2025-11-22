# Matrix Traversal
# Visiting every element in the matrix in some order using loops.
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# 1. Row-wise traversal
def matrixTraversal1(arr):
    print("Matrix Transversal:")
    for i in range(len(arr)):
        for j in range((len(arr[0]))):
            print(arr[i][j], end = " ")
        print('')

matrixTraversal1(matrix)
# Output:
# Matrix Transversal:
# 1 2 3 
# 4 5 6 
# 7 8 9


# 2. Column-wise traversal
def matrixTraversal2(arr):
    print("Matrix Transversal:")
    for i in range(len(arr)):
        for j in range((len(arr[0]))):
            print(arr[j][i], end = " ")
        print('')

matrixTraversal2(matrix)

# Output:
# Matrix Transversal:
# 1 4 7 
# 2 5 8 
# 3 6 9 

# 2. Diagonal traversal
def matrixTraversal3(arr):
    print('Diagonal Traversal:')
    for i in range(len(arr)):
        print(arr[i][i], end ="")

matrixTraversal3(matrix)
# Output:
# Diagonal Traversal:
# 159
print('')
# 2.1 Addition of Diagonal traversal
def matrixTraversal4(arr):
    result = 0
    for i in range(len(arr)):
        result = result + arr[i][i]
    return result 

print(matrixTraversal4(matrix))