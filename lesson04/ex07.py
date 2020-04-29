"""
Реализовать генератор с помощью функции с ключевым словом ​ yield​ , создающим очередное
значение. При вызове функции должен создаваться объект-генератор. Функция должна
вызываться следующим образом: ​
for el in fact(n)​ . Функция отвечает за получение факториала
числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал
четырёх 4! = 1 * 2 * 3 * 4 = 24.
"""

from checks import user_input


def factorial(x):
    # counts factorial of n
    result = 1
    for i in range(1, x + 1):
        result *= i
        yield result


n = user_input('N! (1-15) ', limit=15)
for el in factorial(n):
    print(el)
