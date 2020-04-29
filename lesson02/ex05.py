"""
Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор
натуральных чисел. У пользователя необходимо запрашивать новый элемент рейтинга. Если
в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же
значением должен разместиться после них.

Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: ​ 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
"""

rating = [15, 13, 11, 9, 7, 5, 3, 1]
print('To exit press "q"')
while True:
    newEl = input('Give me your score: ')
    if newEl == 'q':
        break
    else:
        try:
            newEl = int(newEl)
            if newEl > 0:
                for i, e in enumerate(rating):
                    if newEl > e:
                        rating.insert(i, newEl)
                        break
                    elif i == len(rating) - 1:
                        rating.append(newEl)
                        break
            else:
                print('Input must be a positive number')
        except:
            print('Input must be a number')
    print(rating)
print('Exit.')
