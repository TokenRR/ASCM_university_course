from oct2py import octave


def run_octave():
    """Використання Octave для завантаження даних та розв'язання системи рівнянь
    """
    octave.eval("A = load('Labs\Ivanyk\Lab_1\Matrix_A.txt');")
    octave.eval("b = load('Labs\Ivanyk\Lab_1\Vector_b.txt');")
    octave.eval("x = A \\ b;")

    # Отримання результату з Octave
    solution = octave.pull('x')
    solution = solution.flatten()

    # Обчислення похибки
    octave.eval("accuracy = norm(A * x - b);")
    accuracy = octave.pull('accuracy')

    return [solution, accuracy]

if __name__ == '__main__':
    x, e = run_octave()
    print(f'Solution: {x}')
    print(f'Accuracy: {e}')