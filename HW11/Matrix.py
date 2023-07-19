class Matrix:
    """
    Class for matrix objects. Each matrix can only containt integer values.
    A matrix object can be added to or multiplied by another matrix object
    following the basic math rules for matrices.
    """
    def __init__(self, matrix: list[list[int]]):
        first_line_length = len(matrix[0])
        for line in matrix:
            if len(line) != first_line_length:
                raise ValueError('В матрице не может быть строк разной длины')
            for num in line:
                if not isinstance(num, int):
                    raise ValueError('Матрица может принимать только целые числа')
        else:
            self.matrix = matrix
            self.number_of_rows = len(matrix)
            self.number_of_columns = first_line_length

    def __str__(self):
        max_len = 1
        for row in range(self.number_of_rows):
            for column in range(self.number_of_columns):
                length = len(str(self.matrix[row][column]))
                if length > max_len:
                    max_len = length
        return '\n'.join([''.join(['{num: {len}}'.format(num=item, len=max_len + 1) for item in row]) for row in self.matrix])

    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError(f"Объект класса 'Matrix' нельзя складывать с объектом класса '{other.__class__.__name__}'")
        if self.number_of_rows != other.number_of_rows or self.number_of_columns != other.number_of_columns:
            raise ValueError(f"Нельзя складывать матрицы разной размерности. Вы пытаетесь сложить матрицу размера "
                             f"{self.number_of_rows} х {self.number_of_columns} с матрицей размера "
                             f"{other.number_of_rows} x {other.number_of_columns}")
        result = []
        for row in range(self.number_of_rows):
            r = []
            for column in range(self.number_of_columns):
                r.append(self.matrix[row][column] + other.matrix[row][column])
            result.append(r)
        return Matrix(result)

    def __eq__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError(f"Объект класса 'Matrix' нельзя сравнивать с объектом класса '{other.__class__.__name__}'")
        if self.number_of_rows != other.number_of_rows or self.number_of_columns != other.number_of_columns:
            return False
        for row in range(self.number_of_rows):
            for column in range(self.number_of_columns):
                if self.matrix[row][column] != other.matrix[row][column]:
                    return False
        return True

    def __mul__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError(f"Объект класса 'Matrix' нельзя умножать на объект класса '{other.__class__.__name__}'")
        if self.number_of_columns == other.number_of_rows:
            result = [[0 for _ in range(other.number_of_columns)] for _ in range(self.number_of_rows)]
            for res_row in range(self.number_of_rows):
                for res_column in range(other.number_of_columns):
                    r = 0
                    for num in range(self.number_of_columns):
                        r += self.matrix[res_row][num] * other.matrix[num][res_column]
                    result[res_row][res_column] = r
            return Matrix(result)
        else:
            raise ValueError(f"Нельзя умножать матрицы такой размерности. Вы пытаетесь умножить матрицу размера "
                             f"{self.number_of_rows} х {self.number_of_columns} на матрицу размера "
                             f"{other.number_of_rows} x {other.number_of_columns}")


m = Matrix([[1, 2, 3], [3, 2, 1]])
n = Matrix([[2, 4, 111], [1, 1, 1]])
p = Matrix([[1, 2, 3], [3, 2, 1]])

k = Matrix([[1, 2, 0], [3, 1, -1]])
l = Matrix([[1], [2], [3]])

print(m + n)
print(m == n)
print(m == p)
print(k * l)
