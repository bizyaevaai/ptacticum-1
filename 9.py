"""
Имя проекта: practicum-1
Номер версии: 1.0
Имя файла: practicum-1(№9).py
Автор: 2020 © А.И.Бизяева, Челябинск
Лицензия использования: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 19/11/2020
Дата последней модификации: 19/11/2020
Связанные файлы/пакеты:num 
Описание: Решение задачи № 9
#версия Python:3.8
"""
Дано натуральное число. Определить, будет ли это число: нечётным, кратным 7.
""
num=int(input("Введите число:\n"))
if num %2==1 and num %7==0:
    print("Число",num,"нечетное и кратно 7")
    
else:
    print("Число не соответствует условию")