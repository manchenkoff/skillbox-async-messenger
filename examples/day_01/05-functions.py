"""
Функции и аргументы
"""


# Простая функция
def simple_action():
    print('Я обычная функция! Ничего интересного...')


simple_action()  # вызывает выполнение функции


# Функция с аргументами
def say_hello(name: str):
    print(f"Привет, {name}")


say_hello('John')
say_hello('Kate')


# Функция с возращаемым значением
def get_sum_of_two_nums(a, b):
    return a + b


function_result = get_sum_of_two_nums(10, 17)


# Функция с необязательными параметрами
def say_hello_default(name: str = 'незнакомец'):
    print(f"Привет, {name}")


say_hello_default('John')
say_hello_default()


# Функция с неограниченным количество аргументов
def show_list_elements(*args):
    for index, item in enumerate(args):
        print(f"Элемент #{index}: {item}")


show_list_elements(1, 2, 3, 4, 5, 6, 7, 8, 'Все!')
