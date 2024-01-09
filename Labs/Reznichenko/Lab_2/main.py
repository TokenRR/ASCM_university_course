import time
import numpy as np
import pandas as pd
import sympy as sp
from scipy.integrate import simps


def get_func():
    '''Читання формули, первісної та меж інтегрування з файлу
    '''
    with open('D:\KPI\ASKM\Labs\Reznichenko\Lab_2\\umova.txt', 'r') as f:
        lines = f.readlines()
        lower_limit = float(lines[0].strip())
        upper_limit = float(lines[1].strip())
        n = float(lines[2].strip())
        func = lines[3].strip()
        antiderivative = lines[4].strip()
    return [lower_limit, upper_limit, n, func, antiderivative]


def dif():
    start_timer = time.time()
    lower_limit, upper_limit, n, func_str, antiderivative_str = get_func()

    try:
        func_str = func_str.replace('.', '')
        func_str = func_str.replace('^', '**')
        antiderivative_str = antiderivative_str.replace('.', '')
        antiderivative_str = antiderivative_str.replace('^', '**')

        x = sp.symbols('x')
        func = sp.sympify(func_str)  #  Функція
        antiderivative = sp.sympify(antiderivative_str)  #  Первісна

        antiderivative = sp.diff(antiderivative, x)  # Обчислення формули похідної 

        h = (upper_limit - lower_limit) / n  #  Крок 
        x_values = np.arange(lower_limit, upper_limit+h, h)  # Створюємо масив точок на інтервалі [a, b] з кроком h

        # Обчислення значень функцій у цих точках
        func_values = [func.subs(x, val).evalf() for val in x_values]
        antiderivative_values = [antiderivative.subs(x, val).evalf() for val in x_values]

        # Обчислення різниці між значеннями функцій
        difference = np.array(func_values) - np.array(antiderivative_values)

        diff_py = pd.DataFrame({
            'f(x)': func_values,
            '(F(x)\')': antiderivative_values,
            'Різниця': np.abs(difference)
        }, index=x_values)

        print('\n\nДиференціювання за допомогою Python\n')
        print(f'Час виконання {round(time.time() - start_timer, 4)} сек\n')
        print(diff_py)
    except:
        print('SYNTAX ERROR')


def integr():
    start_timer = time.time()
    lower_limit, upper_limit, n, func_str, antiderivative_str = get_func()

    try:
        func_str = func_str.replace('.', '')
        func_str = func_str.replace('^', '**')
        antiderivative_str = antiderivative_str.replace('.', '')
        antiderivative_str = antiderivative_str.replace('^', '**')

        x = sp.symbols('x')
        func = sp.sympify(func_str)  #  Функція
        antiderivative = sp.sympify(antiderivative_str)  #  Первісна

        int_func = sp.integrate(func, x)  #  Інтеграл від функції

        h = (upper_limit - lower_limit) / n  #  Крок 
        x_values = np.arange(lower_limit, upper_limit+h, h)  # Створюємо масив точок на інтервалі [a, b] з кроком h

        # Перетворюємо функцію та первісну у викликаємі функції
        func = sp.lambdify(x, func)
        antiderivative = sp.lambdify(x, antiderivative)

        y_values = [func(point) for point in x_values]  #  Створюємо масив значень функції для кожної точки

        # Обчислюємо чисельне значення визначеного інтегралу для кожної точки
        simpson = [simps(y_values[:i+1], x_values[:i+1], dx=h) for i in range(len(x_values))]

        # Обчислюємо чисельне значення визначеного інтегралу за допомогою методу Ньютона-Лейбніца
        newton_leibniz = [antiderivative(point) - antiderivative(lower_limit) for point in x_values]

        # Обчислюємо різницю між значеннями, отриманими двома методами
        difference = [abs(simpson[i] - newton_leibniz[i]) for i in range(len(x_values))]

        int_py = pd.DataFrame({
            'м.Сімпсона': simpson,
            'м.Ньютона-Лейбніца': newton_leibniz,
            'Різниця': difference
        }, index=x_values)

        print('\n\nІнтегрування за допомогою Python\n')
        print(f'Час виконання {round(time.time() - start_timer, 4)} сек\n')
        print(int_py)
    except:
        print('SYNTAX ERROR')


if __name__ == '__main__':
    lower_limit, upper_limit, _, func, _ = get_func()
    if lower_limit > upper_limit:
        print('lower_limit > upper_limit')

    dif()

    integr()
