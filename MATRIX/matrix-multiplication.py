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

def multiMatrix(A,B):
    result = [[0 for j in range(len(A[0]))] for i in range(len(A))]
    # result = 0
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(A)):
                result[i][j] += A[i][k] * B[j][k]
    return result

print(multiMatrix(A,B))
