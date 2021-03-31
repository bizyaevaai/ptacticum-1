"""
Имя проекта: Practicum-1
Номер версии: 1.0
Имя файла: Practicum-1 (№79) .py
Автор: 2020 © А.И.Бизяева, Челябинск
Лицензия использования: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 28.01.2021
Дата последней модификации: 28.01.2021
Описание: Решение задачи №79
# версия Python: 3.8
"""
Создать прямоугольную матрицу A, имеющую N строк и M столбцов со случайными элементами. Разделить элементы каждого столбца матрицы на элемент этого столбца с наибольшим значением.
""
import random
N = 4
M = 5
L = 2

def get_row(column):
    col = []
    for i in range(0, column):
        col.append(random.randint(0, 9))
    return col

def get_matrix(row, column):
    matrix = []
    for i in range(0, row):
        matrix.append(get_row(column))

    return matrix


def print_matrix(matrix):
    i = 0
    while i < len(matrix):
        j = 0
        row = matrix[i]
        while j < len(row):
            column = row[j]
            print(column, end=' ')
            j += 1

        print()
        i += 1


def get_column(matrix, index):
    column = []
    i = 0
    while i < len(matrix):
        column.append(matrix[i][index])
        i += 1

    return column

A = get_matrix(N, M)
print("Исходная матрица:")
print_matrix(A)

original_matrix = A.copy()
i = 0
while i < len(A):
    j = 0
    max_element = max(A[i])
    while j < len(A[i]):
        print(A[i][j], 'делим на ', max(get_column(A, j)))
        A[i][j] /= max(get_column(original_matrix, i))
        A[i][j] = round(A[i][j], 1)
        j += 1

    i += 1
print("Модифицированная матрица:")
print_matrix(A)
