"""
Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь
ввёл число 3. Считаем 3 + 33 + 333 = 369
"""

char = int(input('Enter any num: '))

print(int(str(char)*3) + int(str(char)*2) + char)
