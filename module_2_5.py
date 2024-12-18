def get_matrix(n, m, value):
    matrix = [[value]*m for  _ in range (n)]
    return matrix
matrices = []
for i in range(3):
    n = int(input ('n:'))
    m = int(input ('m:'))
    value = int(input ('value:'))

    matrix = get_matrix(n, m, value)
    matrices.append(matrix)
for i, matrix in enumerate(matrices):
    print(matrix)
