"""
Имя проекта: Practicum-1
Номер версии: 1.0
Имя файла: Practicum-1 (№63) .py
Автор: 2020 © А.И.Бизяева, Челябинск
Лицензия использования: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 05.01.2021
Дата последней модификации: 05.01.2021
Описание: Решение задачи №63
# версия Python: 3.8
"""
Даны число P и число H. Определить сумму чисел меньше P, произведение чисел больше H и количество чисел в диапазоне значений P и H. При вводе числа равного P или H, закончить работу.
""
import re

P = 2
H = 10

list_numbers = []

sum = 0
multiply = 1
count = 0


while True:
    print("Введите число:", end=' ')
    string = re.sub(r'[^0-9\-]+', '', input())
    if len(string) == 0:
        print("В строке не обнаружено числа")
        continue

    number = int(string)
    list_numbers.append(number)

    if number < P:
        sum += number
    elif number > H:
        multiply *= number

    if P < H:
        if P < number < H:
            count += 1
    else:
        if H < number < P:
            count += 1

    last_namber = list_numbers[len(list_numbers) - 1]
    if last_namber == P or last_namber == H:
        break


print("Сумма:", sum)
print("Произведение:", multiply)
print("Количество чисел в диапазоне значений P и H:", count)
