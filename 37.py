"""
Имя проекта: Practicum-1
Номер версии: 1.0
Имя файла: Practicum-1 (№37) .py
Автор: 2020 © А.И.Бизяева, Челябинск
Лицензия использования: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 12.12.2020
Дата последней модификации: 12.12.2020
Описание: Решение задачи № 37
# версия Python: 3.8
"""
Дан одномерный массив числовых значений, насчитывающий N элементов. Сумму элементов массива и количество положительных элементов поставить на первое и второе место.
""
import numpy as np
import array
import random

N = int(input("Введите количество элементов массива "))
A = [random.randint(-20, 20) for i in range(0, N)]

print(A)

B = 0
cym = np.sum(A)
C = np.size(A)
for i in range(N):
    if A[i] >= 0:
        B += A[i]
(A.insert(0, B))
(A.insert(1, C))

print(A)
