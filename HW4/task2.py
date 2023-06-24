# Напишите функцию для транспонирования матрицы

matr = [[1, 2], [3, 4], [5, 6]]


def transpose_matrix(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]


print(transpose_matrix(matr))
