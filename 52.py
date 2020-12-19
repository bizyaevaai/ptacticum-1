"""
Имя проекта: Practicum-1
Номер версии: 1.0
Имя файла: Practicum-1 (№52) .py
Автор: 2020 © А.И.Бизяева, Челябинск
Лицензия использования: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 15.12.2020
Дата последней модификации: 15.12.2020
Описание: Решение задачи №52
# версия Python: 3.8
"""
 Заданы M строк символов, которые вводятся с клавиатуры. Из заданных строк, каждая из которых представляет одно слово, составить одну длинную строку, разделяя слова пробелами.
""
import random
M = random.randint(1,10)
arr = [random.randint(1,10) for i in range(M)]

for i in range(M):
    arr[i] = input()
print(arr)
b = arr[0]

for i in range(1 , M):
    b = str(b) + " " + arr[i]
print(b)
