"""
Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются
элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний
сохранить на своем месте. Для заполнения списка элементов необходимо использовать
функцию input().
"""

import time

changeList = []
item = 1

print('To stop press enter without any input')

while item:
    item = input('Enter something: ')
    changeList.append(item)

changeList.pop()  # Delete the last (empty) input

print('Wait for shaking...')
time.sleep(3)

for ind, el in enumerate(changeList):
    if ind % 2 == 0 and ind < len(changeList) - 1:
        changeList[ind], changeList[ind + 1] = changeList[ind + 1], changeList[ind]
print(changeList)
