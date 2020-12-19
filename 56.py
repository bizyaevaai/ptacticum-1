"""
Имя проекта: Practicum-1
Номер версии: 1.0
Имя файла: Practicum-1 (№56) .py
Автор: 2020 © А.И.Бизяева, Челябинск
Лицензия использования: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 15.12.2020
Дата последней модификации: 15.12.2020
Описание: Решение задачи № 56
# версия Python: 3.8
"""
 Заданы M строк символов, которые вводятся с клавиатуры. Напечатать все центральные буквы строк нечетной длины.
""
import math
M = 3

list_strings = []
for i in range(0, M):
    print("Введите строку:", end=' ')
    list_strings.append(input())

for string in list_strings:
    strlen = len(string)

    if strlen % 2 != 0:
        print(string[math.ceil(strlen/2) - 1])
