"""
Пример программы для работы с ООП

Данные класса
- имя
- фамилия
- возраст
"""


class Person:
    name: str
    surname: str
    age: int


user = Person()
user.name = "John"
user.surname = "Doe"
user.age = 30

print(user)
