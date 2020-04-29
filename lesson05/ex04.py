"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно
данные. При этом английские числительные должны заменяться на русские. Новый блок строк
должен записываться в новый текстовый файл.
"""

translator_dictionary = {'one': 'en', 'two': 'to', 'three': 'tre', 'four': 'fire', 'five': 'fem'}  # danish

with open('ex04_to.txt', 'w') as to_file:
    for line in open('ex04_fr.txt', 'r'):
        splitted_line = line.split()
        to_file.write(line.replace(splitted_line[0], translator_dictionary[splitted_line[0]]))
