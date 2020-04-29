"""
Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года
относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.
"""

seasons = {
    'winter': (12, 1, 2),
    'spring': (3, 4, 5),
    'summer': (6, 7, 8),
    'fall': (9, 10, 11)
}

month = 0

while month not in range(1, 13):
    month = int(input('Input the number of month: '))

for key in seasons.keys():
    if month in seasons[key]:
        print(f'This month is {key} month')
