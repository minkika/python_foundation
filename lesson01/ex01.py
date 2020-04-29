"""
Поработайте с переменными, создайте несколько, выведите на экран, запросите у
пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.
"""

codeInteger = 1
codeFloat = 2.11
codeStringWithSingleQuotes = 'Hi there!'
codeStringWithDoubleQuotes = "Hi there again!"
codeBoolean = False
codeList = [1, 3, 5, 9]
codeTuple = (9, 5, 3, 1)
codeDict = {'1': 1, '2': 2}

print("I've been created a few variables, look:")
print(f"Variable 1: {codeInteger}, it's type is {type(codeInteger)}")
print(f"Variable 2: {codeFloat}, it's type is {type(codeFloat)}")
print(f"Variable 3: {codeStringWithDoubleQuotes}, it's type is {type(codeStringWithDoubleQuotes)}")
print(f"Variable 4: {codeBoolean}, it's type is {type(codeBoolean)}")

codeBoolean = True

print('Changed variable 4 to', codeBoolean)

inputString = input('Create your own string variable: ')
print('You entered string "%s"' % inputString)

inputInteger = int(input("Create your own integer variable: "))
print('You entered integer: {}'.format(inputInteger))
