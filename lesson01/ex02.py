"""
Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и
выведите в формате чч:мм:сс. Используйте форматирование строк.
"""

inputNumber = int(input('Write seconds: '))
hours = inputNumber // 3600
minutes = (inputNumber - hours * 3600) // 60
seconds = inputNumber - minutes * 60 - hours * 3600

print(f"{hours}:{minutes:02d}:{seconds:02d}")
