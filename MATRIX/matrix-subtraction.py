A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

B = [
    [10, 11, 12],
    [13, 14, 15],
    [16, 17, 18]
]

def subMatrix(A,B):
    result = [[0 for j in range(len(A[0]))] for i in range(len(A))]
    for i in range(len(A)):
        for j in range(len(A[0])):
            result[i][j] = (A[i][j] - B[i][j])
    return result
print(subMatrix(B,A))

