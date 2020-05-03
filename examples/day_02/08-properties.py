"""
ООП - Свойства и атрибуты объектов/классов
"""


# Класс с вычисляемыми свойствами
class Person:
    first_name: str
    last_name: str

    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


person = Person('John', 'Doe')

print(person.full_name)  # свойство вычисляется при обращении

person.last_name = 'Изменено'

print(person.full_name)
