"""
Пример программы для работы с функциями

Сделать
- функцию hello, которая выводит текст приветствия клиенту
"""


def user_hello(user):
    print(f"Привет, {user}")


clients = ['John', 'David', 'Kate', 'Alex']

for user in clients:
    user_hello(user)

new_user = "Artur"

clients.append(new_user)
user_hello(new_user)
