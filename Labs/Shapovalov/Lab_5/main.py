from scipy.optimize import linprog


def umova():
    data = {'Прибуток': [], 'Матриця': [], 'Запаси': []}
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

    return data['Прибуток'], data['Матриця'], data['Запаси']

c, A, b = umova()


# Виклик функції лінійного програмування з методом 'highs' для максимізації прибутку
result = linprog(c, A_ub=A, b_ub=b, method='highs')

print('\n\n\nШаповалов Г. Г. Варіант 15 Лаб 5\n')
if result.success:
    print('\nРозв\'язок на мові Python')
    print('Максимальний прибуток:', -round(result.fun, 2))
    print("Оптимальний план випуску продукції:")
    print('P1 =', round(result.x[0], 2))
    print('P2 =', round(result.x[1], 2))
    print('P3 =', round(result.x[2], 2))
else:
    print('Задачу не вдалося вирішити.')
