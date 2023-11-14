from oct2py import octave
import numpy as np
from scipy.optimize import fmin



def optimize_my_function(initial_vector):
    if len(initial_vector) != 2:
        raise ValueError('Початковий вектор повинен мати розмірність 2')

    def objective_function(x):
        x1, x2 = x
        return 10 * (x1 - np.sin(x2))**2 + 0.1 * x2**2

    optimal_vector = fmin(objective_function, initial_vector, disp=False)

    return optimal_vector, objective_function(optimal_vector)

real_optimal_value = 0  #  Реальні значення

initial_vector = np.array([-1, -1])
optimal_vector, optimal_value = optimize_my_function(initial_vector)
error = abs(optimal_value - real_optimal_value)  #  Обчислити похибку для мінімального значення функції

print('Результати Python')
print('Оптимальний вектор:', optimal_vector)
print('Мінімальне значення функції:', optimal_value)
print('Оцінка похибки:', error)



def optimize_with_octave(initial_vector):
    if len(initial_vector) != 2:
        raise ValueError('Початковий вектор повинен мати розмірність 2')

    # Визначаємо функцію у форматі Octave
    octave.eval("function y = objective_function(x) y = 10 * (x(1) - sin(x(2)) )^2 + 0.1 * x(2)^2; end")

    # Передаємо початковий вектор до Octave
    x0 = initial_vector.tolist()
    octave.push('initial_vector', x0)

    # Використовуємо функцію fminunc для оптимізації
    octave.eval("options = optimset('fminunc');")
    octave.eval("options.Display = 'off';")
    octave.eval("[optimal_vector, optimal_value] = fminunc(@objective_function, initial_vector, options);")

    # Отримуємо результати оптимізації
    optimal_vector = octave.pull('optimal_vector')
    optimal_value = octave.pull('optimal_value')

    return optimal_vector, optimal_value

real_optimal_value = 0  #  Реальні значення

initial_vector = np.array([-1, -1])
optimal_vector, optimal_value = optimize_with_octave(initial_vector)
error = abs(optimal_value - real_optimal_value)  #  Обчислити похибку для мінімального значення функції

print('Результати Octave')
print('Оптимальний вектор:', optimal_vector)
print('Мінімальне значення функції:', optimal_value)
print('Оцінка похибки:', error)
