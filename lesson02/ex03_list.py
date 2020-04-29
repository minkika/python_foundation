"""
Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года
относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.
"""

months = [(12, 3, 6, 9), (1, 4, 7, 10), (2, 5, 8, 11), ('winter', 'spring', 'summer', 'fall')]
monthsSeasons = list(zip(*months))
search = 0

while search not in range(1, 13):
    search = int(input('Enter a number of month: '))

for i, el in enumerate(monthsSeasons):
    if search in monthsSeasons[i]:
        print(f'The {search} month belongs to {monthsSeasons[i][3]}')
