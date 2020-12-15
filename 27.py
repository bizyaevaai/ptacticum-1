"""
Имя проекта: Practicum-1
Номер версии: 1.0
Имя файла: Practicum-1 (№27) .py
Автор: 2020 © А.И.Бизяева, Челябинск
Лицензия использования: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 10.12.2020
Дата последней модификации: 10.12.2020
Описание: Решение задачи № 27
# версия Python: 3.8
"""
Дано вещественное число A. Вычислить f(A), если f(x) = 0 при x ≤ 0; f(x) = x2 − x при 0 < x < 1, в противном случае f(x) = x2 − sin(πx2).
""
import math
A = float(input("Введите число А:"))
x = A
if x <= 0:
    fx = 0
    print("x <= 0; f(a) =:", fx)
elif 0 < x < 1:
    fx = math.pow(x, 2) - x
    print("0 < x < 1; f(a) =:", fx)
else:
    fx = math.pow(x, 2) - math.sin((math.pi * math.pow(x, 2)))
    print("x >= 1; f(a) =:", fx)
