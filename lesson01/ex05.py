"""
Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким
финансовым результатом работает фирма (прибыль ​ — выручка больше издержек, или убыток
— издержки больше выручки). Выведите соответствующее сообщение. Если фирма
отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к
выручке). Далее запросите численность сотрудников фирмы и определите прибыль фирмы в
расчете на одного сотрудника.
"""

revenue = int(input('How is your revenue: '))
costs = int(input('What about costs: '))

if costs > revenue:
    print('It is a lesion')
elif costs == revenue:
    print('Your profit is zero')
else:
    profitability = (revenue - costs) / revenue
    strength = int(input(f'Profitability is {profitability:.2f}! What is strength of your company? '))
    print(f'Profit per person = {(revenue - costs) / strength:.2f}')
