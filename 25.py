"""
Имя проекта: Practicum-1
Номер версии: 1.0
Имя файла: Practicum-1 (№25) .py
Автор: 2020 © А.И.Бизяева, Челябинск
Лицензия использования: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 9.12.2020
Дата последней модификации: 9.12.2020
Описание: Решение задачи № 25
# версия Python: 3.8
"""
Дано вещественное число A. Вычислить f(A), если f(x) = x^2+4x+5, при 2x≤2; в противном случае f(x)= x^2+4x+5 
""
a=float(input("Ведите вещественное число"))
x=a
if x<=2:
    fx=x**2+4*x+5
    print("x<=2,f(a)=:",fx)
else:
    fx=1/x**2+4*x+5
    print("f(a)=:",fx)