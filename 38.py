"""
Имя проекта: Practicum-1
Номер версии: 1.0
Имя файла: Practicum-1 (№38) .py
Автор: 2020 © А.И.Бизяева, Челябинск
Лицензия использования: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 12.12.2020
Дата последней модификации: 12.12.2020
Описание: Решение задачи № 38
# версия Python: 3.8
"""
Дан одномерный массив числовых значений, насчитывающий N элементов.Исключить из него M элементов, начиная с позиции K.
""
import numpy as np
import array
import random

N = int(input("Введите количество элементов массива "))
K = int(input("Позиция K "))
M = int(input("количество элементов для вычитания "))
A = [random.randint(0, 100) for i in range(0, N)]
print(A)

A.insert(K,M)
print(A)

A.delete(K,M)
