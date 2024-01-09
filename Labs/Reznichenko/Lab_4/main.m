% Реальні значення
real_optimal_value = -47/9;

% Початковий вектор
initial_vector = [1, 1];

function [optimal_vector, optimal_value, error] = optimize_with_octave(initial_vector, real_optimal_value)
    if numel(initial_vector) ~= 2
        error('Початковий вектор повинен мати розмірність 2');
    end

    % Визначаємо функцію у форматі Octave
    eval("function y = objective_function(x) y = 3*x(1)^3 - x(1) + x(2)^3 - 3*x(2)^2 -1; end");

    % Використовуємо функцію fminunc для оптимізації
    options = optimset('fminunc');
    options.Display = 'off';
    [optimal_vector, optimal_value] = fminunc(@objective_function, initial_vector, options);

    % Обчислюємо похибку для мінімального значення функції
    error = abs(optimal_value - real_optimal_value);

    % Виводимо результати з більшою точністю та у науковому форматі
    fprintf('\nРезниченко Є. С. Варіант 15 Лаб 4\n');
    disp(['Точка мінімуму: [' num2str(optimal_vector(1),'%.5f') ', ' num2str(optimal_vector(2),'%.5f') ']']);
    disp(['Мінімальне значення функції: ' num2str(optimal_value,'%.8f')]);
    disp(['Оцінка похибки: ' num2str(error,'%.8e')]);
end

% Виклик функції оптимізації
[optimal_vector, optimal_value, error] = optimize_with_octave(initial_vector, real_optimal_value);

