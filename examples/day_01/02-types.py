"""
Основные типы данных
"""

# Числа
number_integer = 10
number_float = 10.5

result_integer = 10 * 2
result_float = 5 / 2

sum_example = 10
sum_example = sum_example + 5  # = 15
sum_example += 5  # краткая запись примера выше, аналогично с *=, /=, -= и тд

convert_to_integer = int(10.4)  # = 10
convert_to_float = float(7)  # = 7.0

simple_integer = 10000  # стандартная запись большого числа
simple_integer_readable = 10_000  # более читаемая запись большого числа

# Строки
first_name = 'John'
last_name = "Doe"  # можно использовать и ' и " для обозначения строк, предпочтительно "

full_name_simple = first_name + ' ' + last_name  # конкатенация строки (сложение)

full_name_format = f"{first_name} {last_name}"  # конкатенация строки (современный вариант)

letter = first_name[0]  # = J

first_name_slice = first_name[0:1]  # срез с 0 по 1 индексы (порядковый номер символа)

first_name_stepped_slice = first_name[0:4:2]  # срез с 0 по 4 индексы с шагом в 2

first_name_reverse = first_name[::-1]  # nhoJ

# Списки
numbers = [4, 8, 15, 16, 23, 42]

random_data = [1, "text", ['Moscow', 2019], 20.5, numbers]

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

numbers.append(108)  # добавить элемент в конец списка

numbers.pop()  # извлечь последний элемент списка

numbers.pop(1)  # извлечь элемент по индексу

numbers.remove(15)  # удалить значение из списка

numbers.count(23)  # посчитать кол-во повторений элемента в списке

len(numbers)  # посчитать длину списка

numbers.sort()  # сортировка списка

numbers.insert(4, 'new_value')  # вставить 'new_value' на 4 индекс

numbers.reverse()  # инверсия списка (обратный порядок)

# Булево значение
is_active = True
is_disabled = False

simple_check_gt = 10 > 5  # = True
simple_check_lt = 5 < 4  # = False

convert_boolean_number = bool(10)  # True
convert_boolean_string = bool('Simple string')  # True
convert_boolean_negative = bool(-20)  # True
convert_boolean_zero = bool(0)  # False

# Словари
person = {'first_name': 'John', 'age': 53}

person_construct = dict(first_name='John', age=53)

john_name_key = person['first_name']
john_name_getter = person.get('first_name')  # вернет False, если такого ключа нет

person.keys()  # вернет названия полей
person.values()  # вернет значения полей
person.items()  # вернет пары ключ-значение
