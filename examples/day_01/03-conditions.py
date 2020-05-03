"""
Условные конструкции
"""

# Простое условие
a = 0

if a > 0:
    print("A is greater than 0")

# Полное условие
b = 10

if b > 0:
    print("B is greater than 0")
else:
    print("B isn't greater than 0")

# Проверка наличия в списке
persons = ["Jim", "John", "Adam", "Peter"]

search_person = "Jack"

if search_person in persons:
    print(f"{search_person} was found in person list")
else:
    print("No results")

# Тернарное условие
a = 10
b = 20

maximum = a if a > b else b  # возьмет наибольшее значение
