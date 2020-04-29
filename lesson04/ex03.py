"""
Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить
задание в одну строку.
"""

from checks import user_input, check_limits


def dividents_list(lower, upper):
    # creates list of dividents by 20 or 21
    return [i for i in range(lower, upper) if i % 20 == 0 or i % 21 == 0]


low = user_input('Input lower number: ', False)
high = user_input('Input upper number: ', False)
low, high = check_limits(low, high)
print(f'List of dividents by 20 and 21 between {low} and {high}: \n '
      f'{dividents_list(low, high)}' if len(dividents_list(low, high)) is not 0 else 'Nothing')
