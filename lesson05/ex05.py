"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

from random import randint

numbers = [randint(0, 100) for i in range(10)]
with open('ex05.txt', 'w') as f:
    f.write(' '.join(list(map(str, numbers))))
print(sum(numbers))
