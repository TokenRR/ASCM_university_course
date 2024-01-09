import time
import os

import numpy as np


def read_matrix(filename):
    """Функція для зчитування матриці з файлу
    """
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            matrix = []
            for line in lines:
                row = [float(x) for x in line.strip().split()]
                matrix.append(row)
            return np.array(matrix)
    except FileNotFoundError:
        print('ERROR', f'Помилка: Файл `{filename}` не знайдено.')
    except ValueError:
        print('ERROR', f'Помилка: Матриця в файлі `{filename}` містить неправильні значення.')
    except Exception as e:
        print('ERROR', f'Помилка: Виникла невідома помилка при зчитуванні матриці: {str(e)}')


def read_vector(filename):
    """Функція для зчитування вектора з файлу
    """
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            vector = [float(line.strip()) for line in lines]
            return np.array(vector)
    except FileNotFoundError:
        print('ERROR', f'Помилка: Файл `{filename}` не знайдено.')
    except ValueError:
        print('ERROR', f'Помилка: Вектор в файлі `{filename}` містить неправильні значення.')
    except Exception as e:
        print('ERROR', f'Помилка: Виникла невідома помилка при зчитуванні вектора: {str(e)}')
    

if __name__ == '__main__':
    os.system('cls')  #  Очищення консолі
    start_python_time = time.time()

    # Зчитування матриці A та вектора b з файлів
    matrix_A = read_matrix('D:\KPI\ASKM\Labs\Reznichenko\Lab_1\matrix.txt')
    vector_b = read_vector('D:\KPI\ASKM\Labs\Reznichenko\Lab_1\\vector.txt')

    if len(vector_b) != len(matrix_A):
        print('ERROR', f'Помилка: Вектор b не відповідає розмірності матриці А.')

    if len(vector_b) >= 10 or len(matrix_A) >= 10:
        print(f'Введіть матрицю меншої розмірності')

    # Розв'язання СЛАР Ax = b
    try:
        solution = np.linalg.solve(matrix_A, vector_b)

        # Обчислення похибки
        accuracy = np.mean((vector_b - np.dot(matrix_A, solution)) ** 2)
        python_run_time = time.time() - start_python_time
        print()
        print(f'Час виконання: {round(python_run_time, 4)} сек')
        print(f'Похибка: {"{:.3e}".format(accuracy)}')
        print(f'Результат: \n{solution}')
    except:
        pass
