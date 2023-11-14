import time
import os

import tkinter as tk
import tkinter.messagebox as messagebox
import numpy as np
from oct2py import octave


CL_GRAY = '#4F6D7A'
CL_Black = '#000000'
CL_WHITE = '#ffffff'


root = tk.Tk()  #  Створення головного вікна програми
root.title('')  #  Задання назви вікну
root.geometry('1050x350')  #  Задаємо розмір вікна
root.resizable(width=False, height=False)  #  Заборона зміни розмірів вікна
root.configure(bg=CL_WHITE)  #  Задаємо колір фону

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
    matrix_A = read_matrix('Labs\.Other\Students\Shapovalov\Lab_1\matrix.txt')
    vector_b = read_vector('Labs\.Other\Students\Shapovalov\Lab_1\\vector.txt')

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


def run_octave():
    """Використання Octave для завантаження даних та розв'язання системи рівнянь
    """
    octave.eval("A = load('Labs\.Other\Students\Shapovalov\Lab_1\matrix.txt');")
    octave.eval("b = load('Labs\.Other\Students\Shapovalov\Lab_1\\vector.txt');")
    octave.eval("x = A \\ b;")

    # Отримання результату з Octave
    solution = octave.pull('x')
    solution = solution.flatten()

    # Обчислення похибки
    octave.eval("accuracy = norm(A * x - b);")
    accuracy = octave.pull('accuracy')

    return [solution, accuracy]


def run1():
    os.system('cls')  #  Очищення консолі
    # - - - - - #
    try:
        start_python_time = time.time()
        matrix_A, vector_b, python_answer, python_accuracy = run_python()
        python_run_time = time.time() - start_python_time
        python_time_label.config(text=f'Час виконання: {round(python_run_time, 4)} сек')
        python_accuracy_label.config(text=f'Похибка: {"{:.3e}".format(python_accuracy)}')
        python_result_label.config(text=f'Результат: \n{python_answer}')
        print(python_answer)
    except:
        pass


def run2():
    os.system('cls')  #  Очищення консолі
    # - - - - - #
    
    start_octave_time = time.time()
    octave_answer, octave_accuracy = run_octave()
    octave_run_time = time.time() - start_octave_time
    octave_time_label.config(text=f'Час виконання: {round(octave_run_time, 2)} сек')
    octave_accuracy_label.config(text=f'Похибка: {"{:.3e}".format(octave_accuracy)}')
    octave_result_label.config(text=f'Результат: \n{octave_answer}')
    


python_name_label = tk.Label(root,
                        text='Python',
                        bg=CL_WHITE,
                        fg=CL_Black,
                        font=('Helvetica', 20),
                        ).place(x=150, y=100)

python_time_label = tk.Label(root,
                        text='Час виконання: ',
                        bg=CL_WHITE,
                        fg=CL_Black,
                        font=('Helvetica', 12),
                        )
python_time_label.place(x=150, y=150)

python_accuracy_label = tk.Label(root,
                        text='Похибка: ',
                        bg=CL_WHITE,
                        fg=CL_Black,
                        font=('Helvetica', 12),
                        )
python_accuracy_label.place(x=150, y=200)

python_result_label = tk.Label(root,
                        text='Результат: ',
                        bg=CL_WHITE,
                        fg=CL_Black,
                        font=('Helvetica', 12),
                        )
python_result_label.place(x=150, y=250)

# ----------------------------------------------- #

octave_name_label = tk.Label(root,
                        text='Octave',
                        bg=CL_WHITE,
                        fg=CL_Black,
                        font=('Helvetica', 20),
                        ).place(x=600, y=100)

octave_time_label = tk.Label(root,
                        text='Час виконання: ',
                        bg=CL_WHITE,
                        fg=CL_Black,
                        font=('Helvetica', 12),
                        )
octave_time_label.place(x=600, y=150)

octave_accuracy_label = tk.Label(root,
                        text='Похибка: ',
                        bg=CL_WHITE,
                        fg=CL_Black,
                        font=('Helvetica', 12),
                        )
octave_accuracy_label.place(x=600, y=200)

octave_result_label = tk.Label(root,
                        text='Результат: ',
                        bg=CL_WHITE,
                        fg=CL_Black,
                        font=('Helvetica', 12),
                        )
octave_result_label.place(x=600, y=250)

# ----------------------------------------------- #


button_run_python = tk.Button(root,
                       text='Run Python',
                       command=run1,
                       bg=CL_GRAY,
                       fg=CL_Black,
                       borderwidth=0,
                       font=('Helvetica', 20),
                       ).place(x=140, y=30)

button_run_octave = tk.Button(root,
                       text='Run Octave',
                       command=run2,
                       bg=CL_GRAY,
                       fg=CL_Black,
                       borderwidth=0,
                       font=('Helvetica', 20),
                       ).place(x=590, y=30)



if __name__ == '__main__':
    os.system('cls')  #  Очищення консолі
    root.mainloop()  #  Запуск головного циклу програми