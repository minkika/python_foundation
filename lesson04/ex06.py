"""
Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию ​ count() и cycle() модуля ​ itertools​ . Обратите внимание, что
создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его
завершения. Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10
завершаем цикл. Во втором также необходимо предусмотреть условие, при котором
повторение элементов списка будет прекращено.
"""

from itertools import count, cycle, islice

from checks import user_input, check_limits


def iter_list(start, length):
    # creates a list of integers from start to stop using count()
    return [i for i in islice(count(start), length)]


def user_cycle(length, array):
    # creates a list of cycled array with given length
    return [i for i in islice(cycle(array), length)]

user_start = user_input('Input lower number for list: ', False)
user_stop = user_input('Input length for list: ', False)
user_start, user_stop = check_limits(user_start, user_stop)
final_list = iter_list(user_start, user_stop)

print(f'Your primary list is {final_list}')

user_length = user_input('Input length for iterator: ')

print(f'Your final list is {user_cycle(user_length, final_list)}')
