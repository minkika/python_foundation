"""
Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить
подсчет количества строк, количества слов в каждой строке.
"""


def count_words(string):
    return len(string.split())


def count_lines(file):
    file.seek(0, 0)
    return len(file.readlines())


with open('ex02.txt', 'r') as f:
    for i, line in enumerate(f.readlines(), 1):
        print(f'Words in {i} line: {count_words(line)}')
    print(f'Lines in {f.name}: {count_lines(f)}')
