"""
Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое
слово с новой строки. Строки необходимо пронумеровать. Если в слово длинное, выводить
только первые 10 букв в слове.
"""

userInput = input('Input the string splitted by spaces: ').split(' ')

for i, e in enumerate(userInput, 1):
    print(f'{i}. {e[:10]}')