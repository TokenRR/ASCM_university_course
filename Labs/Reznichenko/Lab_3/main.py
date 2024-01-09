import pandas as pd
import matplotlib.pyplot as plt


def equation_func(x, y, z):
    return x**2 - x + 2 - y


def runge_kutta(x0, y0, z0, h, x_target, equation_func):
    x = x0
    y = y0
    z = z0

    results = [('x', 'y\'(x)', 'y(x)')]

    while x <= x_target:
        results.append((x, z, y))

        k1y = h * z
        k1z = h * equation_func(x, y, z)

        k2y = h * (z + 0.5 * k1z)
        k2z = h * equation_func(x + 0.5 * h, y + 0.5 * k1y, z + 0.5 * k1z)

        k3y = h * (z + 0.5 * k2z)
        k3z = h * equation_func(x + 0.5 * h, y + 0.5 * k2y, z + 0.5 * k2z)

        k4y = h * (z + k3z)
        k4z = h * equation_func(x + h, y + k3y, z + k3z)

        y = y + (1/6) * (k1y + 2 * k2y + 2 * k3y + k4y)
        z = z + (1/6) * (k1z + 2 * k2z + 2 * k3z + k4z)
        x = x + h

    return results


x0 = 0
y0 = 1
z0 = 0
h = 0.1
x_target = 1.0

results = runge_kutta(x0, y0, z0, h, x_target, equation_func)

# Створюємо датафрейм з результатами
df_python = pd.DataFrame(results[1:], columns=results[0])

print('\n\n\nРезниченко Є. С. Варіант 15 Лаб 3\n')
print('\nРозв\'язок Python:\n')
print(df_python)

# Створюємо графік для результатів Python
plt.figure(figsize=(10, 6))
plt.plot(df_python.index/10, df_python['y(x)'], label='y  (x)', color='orange')
plt.plot(df_python.index/10, df_python['y\'(x)'], label='y \'(x)', color='blue')
plt.title('Результати Python', color='red')
plt.grid(color='grey')
plt.legend()
plt.show()
