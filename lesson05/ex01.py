"""
Создать программно файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
"""

ufile = input('Enter the file name: ')
with open(f'{ufile}.txt', 'w') as file:
    while True:
        new_line = input('Input something: ')
        if new_line == '':
            break
        file.write(new_line + '\n')
print('Done')
