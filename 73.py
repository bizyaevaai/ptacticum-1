
"""
Имя проекта: Practicum-1
Номер версии: 1.0
Имя файла: Practicum-1 (№73) .py
Автор: 2020 © А.И.Бизяева, Челябинск
Лицензия использования: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 20.01.2021
Дата последней модификации: 20.01.2021
Описание: Решение задачи №73
# версия Python: 3.8
"""
Создать прямоугольную матрицу A, имеющую N строк и M столбцов со случайными элементами. Найти сумму элементов всей матрицы. Определить, какую долю в этой сумме составляет сумма элементов каждой строки. Результат оформить в виде матрицы из N строк и M+1 столбцов.

""

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

sum = 0

i = 0
while i < len(A):
    j = 0

    while j < len(A[i]):
        sum += A[i][j]
        j += 1

    i += 1

i = 0

while i < len(A):
    j = 0

    sum_row = 0
    while j < len(A[i]):
        sum_row += A[i][j]
        j += 1

    A[i].append(sum_row/sum)

    i += 1

print("Сумма всех элементов:", sum)
print("Модифицированная матрица:")
print_matrix(A)
