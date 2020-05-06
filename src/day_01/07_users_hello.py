"""
Пример программы для работы с циклами

Данные
- список клиентов чата ['John', 'David', 'Kate', 'Alex']

Сделать
- написать цикл для приветствия каждого клиента
- сообщение имеет вид "Hello, ИМЯ"
"""
clients = ['John', 'David', 'Kate', 'Alex']

for user in clients:
    print(f"Привет, {user}")

clients.append("Artur")
