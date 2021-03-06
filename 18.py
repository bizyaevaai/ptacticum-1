"""
Имя проекта: practicum-1
Номер версии: 1.0
Имя файла: practicum-1(№18).py
Автор: 2020 © А.И.Бизяева, Челябинск
Лицензия использования: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 30/11/2020
Дата последней модификации: 30/11/2020
Описание: Решение задачи № 18
#версия Python:3.8
"""
Имеются две ёмкости: кубическая с ребром A, цилиндрическая с высотой H и радиусом основания R. Определить, можно ли заполнить жидкостью объёма M первую ёмкость, вторую, обе.
""
import math
A = int(input("Ребро кубической ёмкости:"))
H = int(input("Высота цилиндрической ёмкости:"))
R = int(input("Радиус основания цилиндрической ёмкости:"))
M = int(input("Введите объем жидкости:"))
SK = A ** 3
print(SK, "Объём куба")
SC = math.pi * R ** 2 * H
print(SC, "Объём цилиндра")
if SC + SK <= M:
    print("Жидкость поместится в оба сосуда")
if SC <= M:
    print("Жидкость поместится в цилиндр")
if SK <= M:
    print("Жидкость поместится в куб")
