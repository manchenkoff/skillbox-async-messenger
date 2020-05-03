"""
Объектно-ориентированного программирование, использование классов и объектов
"""


# Простой класс с переменными
class Person:
    first_name: str
    last_name: str
    age: int


person1 = Person()

person1.first_name = 'John'
person1.last_name = 'Doe'
person1.age = 43

print(person1.first_name)


# Простой класс с конструктором
class Person:
    first_name: str
    last_name: str
    age: int

    def __init__(self, first_name: str, last_name: str, age: int = 0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


person1 = Person('John', 'Doe', 43)

print(person1.first_name)


# Класс с методами
class Person:
    first_name: str
    last_name: str
    age: int

    def __init__(self, first_name: str, last_name: str, age: int = 0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def info(self):
        print(f"Объект класса Person: {self.first_name} {self.last_name}, age: {self.age}")


person1 = Person('John', 'Doe', 43)

person1.info()
