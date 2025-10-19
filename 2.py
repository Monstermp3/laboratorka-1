def Main():
#Zadanie 1.1
    def greet(name):
        return f'Привет, {name}'

    name = input('Введите своё имя пользователя: ')
    if name == ' ':
        print('Ошибка, введите корректные данные ')
        return
    print(greet(name))
#Zadanie 1.2
    def square(number):
        return number ** 2
    number = input('Введите своё число: ')
    try:
        x = float(number)
        print('Квадрат числа: ', square(x))
    except ValueError:
        print('Число некорректное')
#Zadanie 1.3
    def describe_person(name, age=30):
        print(f'Ваше имя: {name}, Ваш возраст: {age}')
    name = input('Введите ваше имя')
    age1 = input('Введите ваш возраст: ')
    if age1 == '':
        describe_person(name)
    else:
        try:
            age = int(age1)
            describe_person(name, age)
        except ValueError:
            print('Введите корректные значения')


Main()

#Zadanie 2.1
from math import sqrt
number = int(input('Введите простое число: '))
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(sqrt(number) + 1)):
        if number % i == 0:
            return False
        return True
if is_prime(number) == True:
    print('Число простое')
else:
    print('Число не простое')
