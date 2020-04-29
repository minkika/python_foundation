"""
Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""

inputNumber = int(input('Give me a huge number: '))

maxChar = 0
while inputNumber > 0:
    buf = inputNumber % 10
    if buf >= maxChar:
        maxChar = buf
    inputNumber //= 10
print(maxChar)
