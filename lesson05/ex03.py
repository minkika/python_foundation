"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и
величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее
20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода
сотрудников.
"""


def file_to_dict(file, dictionary):
    with open(file, 'r') as file:
        for line in file.readlines():
            name, salary = line.split()
            dictionary[name] = float(salary.replace('\n', ''))
    return dictionary


def employees_filtrered_by_salary(dictionary, upper_limit):
    for key, value in dictionary.items():
        if value < upper_limit:
            print(key)


salaries = {}

employees_filtrered_by_salary(file_to_dict('ex03.txt', salaries), 20000)
print(f'Average is {sum(salaries.values()) / len(salaries):.2f}')
