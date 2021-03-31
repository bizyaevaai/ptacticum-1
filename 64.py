"""
Имя проекта: Practicum-1
Номер версии: 1.0
Имя файла: Practicum-1 (№64) .py
Автор: 2020 © А.И.Бизяева, Челябинск
Лицензия использования: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 05.01.2021
Дата последней модификации: 05.01.2021
Описание: Решение задачи №64
# версия Python: 3.8
"""
Суммировать вводимые числа, среди которых нет нулевых. При вводе нуля обеспечить вывод текущего значения суммы. При вводе числа 99999 закончить работу.
""
import re

list_numbers = []

sum = 0


while True:
    print("Введите число:", end=' ')
    string = re.sub(r'[^0-9\-]+', '', input())
    if len(string) == 0:
        print("В строке не обнаружено числа")
        continue

    number = int(string)
    list_numbers.append(number)

    if number == 99999:
        break
    elif number == 0:
        print("Сумма:", sum)
    else:
        sum += number

print("Сумма:", sum)
