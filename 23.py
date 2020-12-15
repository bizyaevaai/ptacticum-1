"""
Имя проекта: Practicum-1
Номер версии: 1.0
Имя файла: Practicum-1 (№23) .py
Автор: 2020 © А.И.Бизяева, Челябинск
Лицензия использования: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 10.12.2020
Дата последней модификации: 10.12.2020
Описание: Решение задачи № 23
# версия Python: 3.8
"""
Даны двещественные числа X и Y . Вычислить Z. Z = √(X x Y) при X > Y, Z = ln(X + Y ) в противном случае.
""
import math
x = float(input("Введите вещественное число x:"))
y = float(input("Введите вещественное число y:"))
if x > > y:
    z = math.sqrt(x * y)
    print(z)
else:
    z = math.log(x + y, math.e)
    print(z)
