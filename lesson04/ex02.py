"""
Представлен список чисел. Необходимо вывести элементы исходного списка, значения
которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
"""

from checks import auto_list, user_input


def bigger_prev(array):
    # elements of array that bigger than previous -> list
    return [array[i] for i in range(1, len(array)) if array[i] > array[i - 1]]


array = auto_list(user_input('Enter length of array: '))
print(array, bigger_prev(array), sep='\n')
