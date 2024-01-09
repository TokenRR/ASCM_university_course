import warnings
import os
import numpy as np
from scipy.optimize import linprog
warnings.filterwarnings("ignore", category=DeprecationWarning)


def umova():
    with open('umova.txt', 'r', encoding='utf-8') as file:
        lines = [line.strip() for line in file.readlines()]

    # Знайти рядки з мітками
    indices = {label: lines.index(label) for label in ['вектор a', 'вектор b', 'матриця С']}

    # Читання векторів та матриці
    a = np.fromstring(lines[indices['вектор a'] + 1], sep=',')
    b = np.fromstring(lines[indices['вектор b'] + 1], sep=',')
    C_start, C_end = indices['матриця С'] + 1, len(lines)
    C = np.genfromtxt(lines[C_start:C_end], delimiter=',')

    return a, b, C


supply, demand, costs = umova()
os.system('cls')
# print(supply)
# print(demand)
# print(costs)





"""
Транспортна задача без обмежень на Python
"""

C = costs.astype(int).flatten().tolist()
b = np.concatenate((supply, demand)).astype(int).tolist()

m = len(supply)
n = len(demand)

A_eq = np.zeros((m + n, m * n))
b_eq = np.zeros(m + n)

for i in range(m):
    A_eq[i, i * n:(i + 1) * n] = 1
    b_eq[i] = b[i]

for j in range(n):
    A_eq[m + j, j::n] = 1
    b_eq[m + j] = b[m + j]

bounds = [(0, None)] * (m * n)  # Вказуємо верхню межу для всіх змінних

param = {'disp': False}  # Вивід інформації про процес оптимізації
results = linprog(C, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='highs', options=param)
plan = np.reshape(results.x, (n, m)).T
total_cost = np.dot(C, results.x)

print('\nРозв\'язок транспорної задачі (без обмежень) на мові Python')
print('Оптимальний план перевезень:')
print(plan)
print(f'Мінімальна вартість перевезень: {total_cost}')






"""
Транспортна задача обмеженням на Python
"""

# Матриця витрат
costs = np.array([
    [5, 4, 20, 5, 14],
    [19, 20, 2, 4, 5],
    [9, 6, 8, 19, 1],
    [7, 15, 20, 6, 11]
])

# Об'єми виробництва та об'єми потреб
supplies = [60, 50, 40, 20]
demands = [10, 50, 40, 50, 20]

B = np.array([
    [5, 20, 14, 25, 13],
    [19, 22, 15, 4, 12],
    [6, 8, 15, 5, 10],
    [14, 7, 2, 23, 20]
])

# Перетворення задачі у вигляд лінійного програмування
num_supplies = len(supplies)
num_demands = len(demands)
flatten_costs = costs.flatten()

# Коефіцієнти цільової функції (вартість перевезень)
c = flatten_costs

# Коефіцієнти лівих частин обмежень (обсяги виробництва та споживання)
A_eq = np.zeros((num_supplies + num_demands, num_supplies * num_demands))
for i in range(num_supplies):
    for j in range(num_demands):
        A_eq[i, i * num_demands + j] = 1
        A_eq[num_supplies + j, i * num_demands + j] = 1

# Праві частини обмежень (суми обсягів)
b_eq = np.concatenate([supplies, demands])

# # Визначення меж для кількості продуктів (позитивні значення)
# bounds = [(0, None) for _ in range(num_supplies * num_demands)]


# Згенеруйте список кортежів меж для кожного x_ij на основі матриці обмежень B
bounds = [(0, None) for _ in range(num_supplies * num_demands)]

# Виклик функції linprog для знаходження оптимального розв'язку
result = linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='highs')

# Виведення результату
print('\n\n\nРозв\'язок транспорної задачі (з обмеженнями) на мові Python')
print('Оптимальний план перевезень:')
print(result.x.reshape((num_supplies, num_demands)))
print('Мінімальні витрати перевезень:', result.fun)
