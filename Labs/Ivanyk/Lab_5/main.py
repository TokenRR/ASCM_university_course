from scipy.optimize import linprog
from oct2py import octave


def umova():
    data = {'Список 1': [], 'Матриця 1': [], 'Список 2': []}
    current_list = None

    with open('data.txt', 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if line.startswith('#'):
                current_list = line[1:].strip()
            elif current_list:
                values = [float(x) for x in line.split()]
                if current_list == 'Матриця 1':
                    data[current_list].append(values)
                else:
                    data[current_list].extend(values)

    data['Матриця 1'] = [row for row in data['Матриця 1'] if row]

    return data['Список 1'], data['Матриця 1'], data['Список 2']

c, A, b = umova()


# Виклик функції лінійного програмування з методом 'highs' для максимізації прибутку
result = linprog(c, A_ub=A, b_ub=b, method='highs')

if result.success:
    print('\n\nРозв\'язок на мові Python\n')
    print('Максимальний прибуток:', -round(result.fun, 2))
    print("Оптимальний план випуску продукції:")
    print('P1 =', round(result.x[0], 2))
    print('P2 =', round(result.x[1], 2))
    print('P3 =', round(result.x[2], 2))
else:
    print('Задачу не вдалося вирішити.')



lb = [0, 0, 0]
ub = []
vartype = 'CCC'
ctype = 'UUU'
sense = 1

# Передаємо дані до Octave
OCTAVE_DATA = {'c': c, 'A': A, 'b': b, 'lb': lb, 'ub': ub, 'vartype': vartype, 'ctype': ctype, 'sense': sense}

for key, value in OCTAVE_DATA.items():
    octave.push(key, value)


# Викликаємо функцію glpk з Octave
octave.eval('[x, fval, status] = glpk(c, A, b, lb, ub, ctype, vartype, sense);')

# Отримуємо результати з Octave
x = octave.pull('x')
fval = octave.pull('fval')
status = octave.pull('status')

if status == 5:  # Статус 5 вказує на невирішену задачу
    print("Задачу не вдалося вирішити.")
else:
    print('\n\nРозв\'язок на мові Octave\n')
    print("Максимальний прибуток:", -fval)
    print("Оптимальний план випуску продукції:")
    print(f"P1 = {x[0][0]}")
    print(f"P2 = {x[1][0]}")
    print(f"P3 = {x[2][0]}")
