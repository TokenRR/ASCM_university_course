import numpy as np
from scipy.optimize import minimize


def optimize_my_function(initial_vector):
    if len(initial_vector) != 2:
        raise ValueError('Початковий вектор повинен мати розмірність 2')

    def objective_function(x):
        x1, x2 = x
        return 3*x1**3 - x1 + x2**3 - 3*x2**2 -1
    
    result = minimize(objective_function, initial_vector)

    return result.x, result.fun

real_optimal_value = -47/9  # Реальні значення взяті з умови

initial_vector = np.array([1, 1])  # Ваш початковий вектор
optimal_vector, optimal_value = optimize_my_function(initial_vector)
error = abs(optimal_value - real_optimal_value)  # Обчислити похибку для мінімального значення функції

print('\n\n\nРезниченко Є. С. Варіант 15 Лаб 4\n')
print('Точка мінімуму:', optimal_vector)
print('Мінімальне значення функції:', optimal_value)
print('Оцінка похибки:', error)
