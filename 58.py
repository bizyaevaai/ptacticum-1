"""
Имя проекта: Practicum-1
Номер версии: 1.0
Имя файла: Practicum-1 (№58) .py
Автор: 2020 © А.И.Бизяева, Челябинск
Лицензия использования: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 15.12.2020
Дата последней модификации: 15.12.2020
Описание: Решение задачи №58
# версия Python: 3.8
"""
Задана строка символов, в которой встречается символ «.». Поставить после каждого такого символа системное время ПК.
""
from datetime import datetime
M = 3

list_strings = []
for i in range(0, M):
    print("Введите строку:", end=' ')
    list_strings.append(input())

now = str(datetime.now())

for string in list_strings:
    print(string.replace('.', '.' + now))
