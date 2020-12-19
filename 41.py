"""
Имя проекта: Practicum-1
Номер версии: 1.0
Имя файла: Practicum-1 (№41) .py
Автор: 2020 © А.И.Бизяева, Челябинск
Лицензия использования: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 13.12.2020
Дата последней модификации: 13.12.2020
Описание: Решение задачи № 41
# версия Python: 3.8
"""
Дан одномерный массив числовых значений, насчитывающий N элементов. Определить, образуют ли элементы массива, расположенные перед первым отрицательным элементом, возрастающую последовательность.
""
import random

N = int(input("Количество элементов массива"))
A = [1,5,3,-4]

print(A)

a = 0
for i in range(N):
    if A[i] >= 0:
        break
    if A[i] < 0:
        for i in range(N):
            if A[i-1] < A[i]:
                a = 0
            else:
                a =1
                break
        A[i] = A[i] - 1
        
if (a == 0):
    print("Возрастающая")
    
else:
    print("Убывающая")