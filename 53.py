"""
Имя проекта: Practicum-1
Номер версии: 1.0
Имя файла: Practicum-1 (№53) .py
Автор: 2020 © А.И.Бизяева, Челябинск
Лицензия использования: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 15.12.2020
Дата последней модификации: 15.12.2020
Описание: Решение задачи № 53
# версия Python: 3.8
"""
Заданы M строк слов, которые вводятся с клавиатуры. Подсчитать количество гласных букв в каждой из заданных строк.
""
import re
M = 4
def get_count(str):
    vowel = 0
    consonant = 0
    str = re.sub(r'\d', '', str)
    str = re.sub(r'\W', '', str)
    i = 0
    while i < len(str):
        char = str[i]
        if char.lower() in ['a', 'e', 'i', 'o', 'u', 'y',
                            'а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']:
            vowel += 1
        else:
            consonant += 1

        i += 1
    return vowel, consonant
list_strings = []
for i in range(0, M):
    print("Введите строку:", end=' ')
    list_strings.append(input())

for str in list_strings:
    vowel, consonant = get_count(str)
    print("В строке %s %s гласных и %s согласных" % (str, vowel, consonant))
