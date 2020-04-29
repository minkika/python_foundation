"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с
декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к
типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на
реальных данных.
"""

from datetime import date
from re import findall


class Date:

    def __init__(self, date_string):
        self.day, self.month, self.year = findall(r'\d+', date_string)

    @classmethod
    def date_string_to_nums(cls, string):
        return int(string)

    @staticmethod
    def date_validate(day, month, year):
        day, month, year = map(Date.date_string_to_nums, [day, month, year])
        if year % 4 == 0 and year % 100 != 0 and month == 2 and day == 29:
            return True
        else:
            try:
                date(year, month, day)
                return True
            except:
                return False


for i in ['01-01-1999', '15-13-2011', '29-02-2008', '31-04-2019', '09-09-2020', '29-02-2100', 'wtf?']:  # +-+-+-
    try:
        udate = Date(i)
        print(udate.date_validate(udate.day, udate.month, udate.year))
    except ValueError:
        print("Can't understand you")
