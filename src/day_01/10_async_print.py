"""
Пример программы для работы с асинхронностью

Данные
- пользователь вводит число X

Сделать
- асинхронную функцию, которая запустится X раз
- функция должна считать от 0 до числа X
- между выводом чисел должны быть паузы по 0,5 сек
"""
import asyncio


def print_counter(x):
    for number in range(x):
        print(number)


def start(x):
    for number in range(x):
        print_counter(x)


user_count = int(input("Количество функций >> "))
start(user_count)
