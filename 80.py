"""
Имя проекта: Practicum-1
Номер версии: 1.0
Имя файла: Practicum-1 (№80) .py
Автор: 2020 © А.И.Бизяева, Челябинск
Лицензия использования: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 29.01.2021
Дата последней модификации: 29.01.2021
Описание: Решение задачи №80
# версия Python: 3.8
"""
 Создать прямоугольную матрицу A, имеющую N строк и M столбцов со случайными элементами. Разделить элементы матрицы на элемент матрицы с наибольшим значением.
""
import random

N = 7
M = 9
L = 2

def get_row(column):
    col = []
    for i in range(0, column):
        col.append(random.randint(0, 99))

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

max_element = False

i = 0
while i < len(A):
    j = 0

    while j < len(A[i]):
        if max_element is False or max_element < A[i][j]:
            max_element = A[i][j]
        j += 1

    i += 1

i = 0
while i < len(A):
    j = 0
    while j < len(A[i]):
        A[i][j] /= max_element
        A[i][j] = round(A[i][j], 1)
        j += 1

    i += 1

print("Максимальный элемент:", max_element)
print("Модифицированная матрица:")
print(matrix(A))
