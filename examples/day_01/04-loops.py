"""
Циклические конструкции
"""

# Цикл while
step = 0
max_steps = 5

while step < max_steps:
    print(f"I'm working on ... {max_steps - step} remaining")
    step += 1

# Цикл for in
persons = ['Jim', 'Adam', 'Kate', 'Peter']

for person in persons:
    print(f"Hello, {person}")
