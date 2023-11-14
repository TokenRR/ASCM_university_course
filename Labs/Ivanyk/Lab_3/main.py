from oct2py import Oct2Py
import pandas as pd
import matplotlib.pyplot as plt


def equation_func(x, y, z):
    return x * (2.71828 ** x) - 2 * z - 2 * y

def runge_kutta(x0, y0, z0, h, x_target, equation_func):
    x = x0
    y = y0
    z = z0

    results = [('x', 'f(x)', 'f\'(x)')]

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
y0 = 0
z0 = 0
h = 0.1
x_target = 1.5

results = runge_kutta(x0, y0, z0, h, x_target+h, equation_func)

# Створюємо датафрейм з результатами
df_python = pd.DataFrame(results[1:], columns=results[0]).set_index('x')

print('\n\nРозв\'язок Python:\n')
print(df_python)


# Запускаємо Octave
oc = Oct2Py()

# Визначаємо функцію рівняння
oc.eval("""
function result = equation_func(x, y, z)
    result = x * exp(x) - 2 * z - 2 * y;
end
""")

# Визначаємо функцію для методу Рунге-Кутта
oc.eval("""
function results = runge_kutta_octave(x0, y0, z0, h, x_target)
    x = x0;
    y = y0;
    z = z0;

    results = zeros(1, 3);

    while x <= x_target
        results = [results; [x, z, y]];

        k1y = h * z;
        k1z = h * equation_func(x, y, z);

        k2y = h * (z + 0.5 * k1z);
        k2z = h * equation_func(x + 0.5 * h, y + 0.5 * k1y, z + 0.5 * k1z);

        k3y = h * (z + 0.5 * k2z);
        k3z = h * equation_func(x + 0.5 * h, y + 0.5 * k2y, z + 0.5 * k2z);

        k4y = h * (z + k3z);
        k4z = h * equation_func(x + h, y + k3y, z + k3z);

        y = y + (1/6) * (k1y + 2 * k2y + 2 * k3y + k4y);
        z = z + (1/6) * (k1z + 2 * k2z + 2 * k3z + k4z);
        x = x + h;
    end
end
""")


# Визначаємо початкові значення
x0 = -0.1;
y0 = 0;
z0 = 0;
h = 0.1;
x_target = 1.5;

# Викликаємо функцію методу Рунге-Кутта
results_octave = oc.runge_kutta_octave(x0, y0, z0, h, x_target+h)

# Створюємо датафрейм з результатами
df_octave = pd.DataFrame(results_octave[2:, :], columns=["x", "f(x)", "f\'(x)"]).set_index('x')

print('\n\nРозв\'язок Octave:\n')
print(df_octave)


# Створюємо графік для результатів Python
plt.figure(figsize=(10, 6))
plt.plot(df_python.index, df_python['f(x)'], label='f  (x)', color='blue')
plt.plot(df_python.index, df_python['f\'(x)'], label='f \'(x)', color='orange')
plt.title('Результати Python')
plt.legend()
plt.grid(c='#E7E8D2')
plt.show()

# Створюємо графік для результатів Octave
plt.figure(figsize=(10, 6))
plt.plot(df_octave.index, df_octave['f(x)'], label='f  (x)', color='blue')
plt.plot(df_octave.index, df_octave['f\'(x)'], label='f \'(x)', color='orange')
plt.title('Результати Octave')
plt.legend()
plt.grid(c='#E7E8D2')
plt.show()

