from octave_ import run_octave
from python_ import run_python


import time
import os
import tkinter as tk


CL_BLUE = '#084C61'
CL_RED = '#DB504A'
CL_YELLOW = '#E3B505'
CL_GRAY = '#4F6D7A'
CL_OCEAN = '#56A3A6'
CL_GREEN = '#79B473'
CL_PURPLE = '#414073'
CL_BLACK = '#000000'


root = tk.Tk()  #  Створення головного вікна програми
root.title('Іваник')  #  Задання назви вікну
root.geometry('1000x600')  #  Задаємо розмір вікна
root.resizable(width=False, height=False)  #  Заборона зміни розмірів вікна
root.configure(bg=CL_GRAY)  #  Задаємо колір фону


def run():
    os.system('cls')  #  Очищення консолі
    try:
        start_python_time = time.time()
        matrix_A, vector_b, python_answer, python_accuracy = run_python()
        python_run_time = time.time() - start_python_time
        python_time_label.config(text=f'Час виконання: {round(python_run_time, 4)} сек')
        python_accuracy_label.config(text=f'Похибка: {"{:.3e}".format(python_accuracy)}')
        python_result_label.config(text=f'Результат: \n{python_answer}')

        start_octave_time = time.time()
        octave_answer, octave_accuracy = run_octave()
        octave_run_time = time.time() - start_octave_time
        octave_time_label.config(text=f'Час виконання: {round(octave_run_time, 2)} сек')
        octave_accuracy_label.config(text=f'Похибка: {"{:.3e}".format(octave_accuracy)}')
        octave_result_label.config(text=f'Результат: \n{octave_answer}')
        print(python_answer)
        print(octave_answer)
    except:
        pass

python_name_label = tk.Label(root,
                        text='Python',
                        bg=CL_BLACK,
                        fg=CL_GRAY,
                        font=('Helvetica', 20),
                        ).place(x=150, y=30)

python_time_label = tk.Label(root,
                        text='Час виконання: ',
                        bg=CL_BLACK,
                        fg=CL_GRAY,
                        font=('Helvetica', 12),
                        )
python_time_label.place(x=100, y=80)

python_accuracy_label = tk.Label(root,
                        text='Похибка: ',
                        bg=CL_BLACK,
                        fg=CL_GRAY,
                        font=('Helvetica', 12),
                        )
python_accuracy_label.place(x=100, y=110)

python_result_label = tk.Label(root,
                        text='Результат: ',
                        bg=CL_BLACK,
                        fg=CL_GRAY,
                        font=('Helvetica', 12),
                        )
python_result_label.place(x=100, y=140)

# ----------------------------------------------- #

octave_name_label = tk.Label(root,
                        text='Octave',
                        bg=CL_BLACK,
                        fg=CL_GRAY,
                        font=('Helvetica', 20),
                        ).place(x=540, y=30)

octave_time_label = tk.Label(root,
                        text='Час виконання: ',
                        bg=CL_BLACK,
                        fg=CL_GRAY,
                        font=('Helvetica', 12),
                        )
octave_time_label.place(x=490, y=80)

octave_accuracy_label = tk.Label(root,
                        text='Похибка: ',
                        bg=CL_BLACK,
                        fg=CL_GRAY,
                        font=('Helvetica', 12),
                        )
octave_accuracy_label.place(x=490, y=110)

octave_result_label = tk.Label(root,
                        text='Результат: ',
                        bg=CL_BLACK,
                        fg=CL_GRAY,
                        font=('Helvetica', 12),
                        )
octave_result_label.place(x=490, y=140)


# ----------------------------------------------- #

button_run = tk.Button(root,
                       text='Run',
                       command=run,
                       bg=CL_BLACK,
                       fg=CL_YELLOW,
                       borderwidth=0,
                       font=('Helvetica', 20),
                       ).place(x=360, y=30)
