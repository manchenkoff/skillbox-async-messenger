"""
ООП - Наследование и перегрузка классов
"""


# Пример базового класса
class Human:
    def walk(self):
        print("Я иду...")

    def sleep(self):
        print("Я сплю...")


person = Human()
person.walk()


# Пример класса-наследника
class SuperHuman(Human):
    def fly(self):
        print("Я лечу...")


person = SuperHuman()
person.walk()
person.fly()


# Пример перегрузки родительского класса
class SuperHuman(Human):
    def fly(self):
        print("Я лечу...")

    def walk(self):
        super().walk()
        print("Но как сверх-человек!")


person = SuperHuman()
person.walk()
person.fly()


# Пример перегрузки стандартных операций (str - для print, repr - для print в списках)
class PrintableHuman:
    name: str

    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f"Объект класса Human: {self.name}"


person = PrintableHuman('John Doe')
print(person)
