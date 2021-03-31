"""
Имя проекта: Practicum-1
Номер версии: 1.0
Имя файла: Practicum-1 (№75) .py
Автор: 2020 © А.И.Бизяева, Челябинск
Лицензия использования: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 25.01.2021
Дата последней модификации: 25.01.2021
Описание: Решение задачи №75
# версия Python: 3.8
"""
Создать прямоугольную матрицу A, имеющую N строк и M столбцов со случайными элементами. Определить, сколько нулевых элементов содержится в верхних L строках матрицы и в левых К столбцах матрицы
""
import random

N = 5
M = 7

L = 3
K = 2


def get_row(column):
    col = []
    for i in range(0, column):
        col.append(random.randint(-9, 9))

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


A = get_matrix(N, M)
print("Исходная матрица:")
print_matrix(A)

l_zeros = 0
k_zeros = 0


i = 0
while i < len(A):
    j = 0

    while j < len(A[i]):
        if A[i][j] == 0:
            if i < L:
                l_zeros += 1

            if j < K:
                k_zeros += 1
        j += 1

    i += 1

print("В верхних %s строках содержится %s нулей" % (L, l_zeros))
print("В левых %s столбцах содержится %s нулей" % (K, k_zeros))
