"""
Пример программы для работы с ООП

Сделать
- добавить метод для вывода сообщений с префиксом имени
- добавить метод для вывода информации об объекте
- добавить конструктор класса для формирования полей
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


user = Person("John", "Doe", 30)
user1 = Person("Artur", "Doe", 30)

# print(user.name, user.surname)
user.info()
user1.info()

print(user.say_as("Hello!"))
