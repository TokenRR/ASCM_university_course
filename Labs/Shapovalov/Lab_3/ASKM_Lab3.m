# Початкові значення
x0 = 0.0;
y0 = 2.5;
z0 = 1.5;
h = 0.1;
x_target = 0.9;

# Функція рівняння
function result = equation_func(x, y, z)
    result = 1 + exp(x) - y - z;
endfunction

# Метод Рунге-Кутта
function results = runge_kutta(x0, y0, z0, h, x_target)
    x = x0;
    y = y0;
    z = z0;
    results = [];

    while x < x_target
        results = [results; [x, y, z]];

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
    endwhile
    results = [results; [x, y, z]]; # Додаємо останній крок
endfunction

# Виклик методу Рунге-Кутта
results = runge_kutta(x0, y0, z0, h, x_target);

# Вивід результатів у форматі таблиці
fprintf('\nРозв''язок Octave:\n\n');
fprintf('      x     y''(x)      y(x)\n');
fprintf('---------------------------\n');
for i = 1:size(results, 1)
    fprintf('%6.4f   %8.6f   %8.6f\n', results(i, 1), results(i, 3), results(i, 2));
end

# Створення графіку
figure;
plot(results(:, 1), results(:, 3), 'g-', 'LineWidth', 2, 'DisplayName', 'y(x)');
hold on;
plot(results(:, 1), results(:, 2), 'r-', 'LineWidth', 2, 'DisplayName', 'y''(x)');
title('Результати Octave');
legend('Location', 'SouthWest', 'FontSize', 20);
grid on;
hold off;

