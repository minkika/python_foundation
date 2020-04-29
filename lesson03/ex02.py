"""
Реализовать функцию, принимающую несколько параметров, описывающих данные
пользователя: имя, фамилия, год рождения, город проживания, email, телефон. Функция
должна принимать параметры как именованные аргументы. Реализовать вывод данных о
пользователе одной строкой.
"""

def archive(name='User', lastName='None', bDateYear='None', city='unknown', email=None, mobile=None):
    return print(f'User named {name}, {lastName}, born in {bDateYear}, living in {city}, has email {email} and phone number {mobile}')

archive(name='Luba', lastName='Golubeva', bDateYear='1992', email='lubov@golubeva.su', mobile='9263230686')
