import numpy as np
import tkinter.messagebox as messagebox


def run_python():
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
            messagebox.showerror('ERROR', f'Помилка: Файл `{filename}` не знайдено.')
        except ValueError:
            messagebox.showerror('ERROR', f'Помилка: Матриця в файлі `{filename}` містить неправильні значення.')
        except Exception as e:
            messagebox.showerror('ERROR', f'Помилка: Виникла невідома помилка при зчитуванні матриці: {str(e)}')

    def read_vector(filename):
        """Функція для зчитування вектора з файлу
        """
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()
                vector = [float(line.strip()) for line in lines]
                return np.array(vector)
        except FileNotFoundError:
            messagebox.showerror('ERROR', f'Помилка: Файл `{filename}` не знайдено.')
        except ValueError:
            messagebox.showerror('ERROR', f'Помилка: Вектор в файлі `{filename}` містить неправильні значення.')
        except Exception as e:
            messagebox.showerror('ERROR', f'Помилка: Виникла невідома помилка при зчитуванні вектора: {str(e)}')
    
    
    # Зчитування матриці A та вектора b з файлів
    matrix_A = read_matrix('Labs\Lab_1\Matrix_A.txt')
    vector_b = read_vector('Labs\Lab_1\Vector_b.txt')

    if len(vector_b) != len(matrix_A):
        messagebox.showerror('ERROR', f'Помилка: Вектор b не відповідає розмірності матриці А.')

    # Розв'язання СЛАР Ax = b
    try:
        solution = np.linalg.solve(matrix_A, vector_b)

        # Обчислення похибки
        accuracy = np.mean((vector_b - np.dot(matrix_A, solution)) ** 2)
        # print(accuracy)
        # accuracy = np.max(np.abs(vector_b - np.dot(matrix_A, solution)))
        # print(accuracy)
        return [matrix_A, vector_b, solution, accuracy]
    except:
        pass


if __name__ == '__main__':
    a, b, x, e = run_python()
    print(f'Matrix:\n{a}')
    print(f'Vector: {b}')
    print(f'Solution: {x}')
    print(f'Accuracy: {e}')