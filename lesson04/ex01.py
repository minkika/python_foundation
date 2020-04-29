"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной
платы сотрудника. В расчете необходимо использовать формулу: (выработка в часах*ставка в
час) + премия. Для выполнения расчета для конкретных значений необходимо запускать
скрипт с параметрами.
"""

from sys import argv

from checks import check_input

script_name, hours, rate, bonus = argv


def calculate(hours, rate, bonus):
    """
    calculates salary after checking input or throws message 'Wrong input'

    arguments:
    hours - hours worked
    rate - $ per hour
    bonus - amount of added $
    """
    if (check_input(hours, rate, bonus)):
        hours, rate, bonus = check_input(hours, rate, bonus)
        print(hours * rate + bonus)
    else:
        print('Wrong input')


calculate(hours, rate, bonus)
