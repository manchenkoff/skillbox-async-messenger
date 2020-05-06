"""
Пример программы для работы со списками

Данные
- есть список из 6 чисел [4, 8, 15, 16, 23, 42]

Сделать
- добавить число 108 в конец списка
- удалить число 15
- вывести длину списка
- вывести сумму всех значений
- вывести последний элемент
- вывести срез элементов с 2 по 4
"""
numbers = [4, 8, 15, 16, 23, 42]
print(numbers)

numbers.append(108)
print(numbers)

numbers.remove(15)
print(numbers)

print(len(numbers))

print(sum(numbers))

print(numbers[-1])

print(numbers[2:4])
print(numbers[2:4:2])
