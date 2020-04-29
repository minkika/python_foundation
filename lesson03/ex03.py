"""
Реализовать функцию ​ my_func()​ , которая принимает три позиционных аргумента, и
возвращает сумму наибольших двух аргументов.
"""

def my_func(a, b, c):
    '''
    returns sum of two the most of three
    '''
    d = list(reversed(sorted([a, b, c])))
    return d[0] + d[1]

print(my_func(1, 3, 5))