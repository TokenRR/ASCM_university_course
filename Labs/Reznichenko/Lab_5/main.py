from scipy.optimize import linprog


def umova():
    data = {'Вартість': [], 'Матриця': [], 'Норми': []}
    current_list = None

    with open('umova.txt', 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if line.startswith('#'):
                current_list = line[1:].strip()
            elif current_list:
                values = [float(x) for x in line.split()]
                if current_list == 'Матриця':
                    data[current_list].append(values)
                else:
                    data[current_list].extend(values)

    data['Матриця'] = [row for row in data['Матриця'] if row]

    return data['Вартість'], data['Матриця'], data['Норми']

c, A, b = umova()


# Виклик функції лінійного програмування з методом 'highs' для максимізації прибутку
result = linprog(c, A_ub=A, b_ub=b, method='highs')

print('\n\n\nРезниченко Є. С. Варіант 6 Лаб 5\n')
if result.success:
    print('Максимальна кількість поживних речовин:', -round(result.fun, 3))
    print("Оптимальний план раціону харчування:")
    print('P1 =', round(result.x[0], 3))
    print('P2 =', round(result.x[1], 3))
    print('P3 =', round(result.x[2], 3))
    print('P4 =', round(result.x[3], 3))
else:
    print('Задачу не вдалося вирішити.')
