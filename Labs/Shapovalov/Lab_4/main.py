import numpy as np
from scipy.optimize import fmin


def optimize_my_function(initial_vector):
    if len(initial_vector) != 2:
        raise ValueError('Початковий вектор повинен мати розмірність 2')

    def objective_function(x):
        x1, x2 = x
        return x1**2 + 16*x2**2
    
    optimal_vector = fmin(objective_function, initial_vector, disp=False)

    return optimal_vector, objective_function(optimal_vector)

real_optimal_value = 0  #  Реальні значення

initial_vector = np.array([2, 2])
optimal_vector, optimal_value = optimize_my_function(initial_vector)
error = abs(optimal_value - real_optimal_value)  #  Обчислити похибку для мінімального значення функції

print('\n\n\nШаповалов Г. Г. Варіант 28 Лаб 4\n')
print('Результати Python')
print('Оптимальний вектор:', optimal_vector)
print('Мінімальне значення функції:', optimal_value)
print('Оцінка похибки:', error)
