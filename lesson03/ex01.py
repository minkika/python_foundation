"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их
деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на
ноль.
"""


def divide(a, b):
    '''
    divides first by second

    a = divident
    b = divider
    returns quo
    '''
    try:
        return int(a) / int(b)
    except ZeroDivisionError:
        return 'You can divide by zero, but not in my shift'
    except ValueError:
        return 'I have been broken by your input!!!'


a = input('a: ')
b = input('b: ')

print(divide(a, b))
