"""
Реализовать формирование списка, используя функцию ​ range() и возможности генератора. В
список должны войти четные числа от 100 до 1000 (включая границы). Необходимо получить
результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию ​ reduce()​ .
"""

from functools import reduce

from checks import user_input, check_limits


def huge_multiply(lower, higher):
    # multiplies all odd numbers in limit
    return reduce((lambda x, y: x * y), [i for i in range(lower, higher + 1) if i % 2 == 0])


user_lower = user_input('Insert lower limit: ', False)
user_upper = user_input('Insert higher limit: ', False)
user_lower, user_upper = check_limits(user_lower, user_upper)
print('Multiplication is ', huge_multiply(user_lower, user_upper))
