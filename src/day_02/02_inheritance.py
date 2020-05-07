"""
Пример программы для работы с ООП

Сделать
- класс User от класса Person
- добавить поле для пароля
- добавить метод проверки пароля
"""


class Person:
    name: str
    surname: str
    age: int

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def info(self):
        print(f"{self.name} {self.surname}, {self.age}")

    def say_as(self, message):
        return f"<{self.name}> {message}"


class User(Person):
    password: str

    def check_password(self, user_password):
        return self.password == user_password


user = User("test", "test", 30)
user.password = 123123

print(user.check_password(321321))
print(user.check_password(123123))
