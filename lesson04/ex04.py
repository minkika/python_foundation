"""
Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию. Элементы вывести в
порядке их следования в исходном списке. Для выполнения задания обязательно
использовать генератор.
Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]
"""

from checks import auto_list, user_input


def uniques_list(array):
    # deletes not unique elements from list
    return [i for i in array if array.count(i) == 1]


length = user_input('Input length of array: ')
array = auto_list(length, 0, 10)
print('Primary array: ', array, 'Uniqued array: ', uniques_list(array), sep='\n')
