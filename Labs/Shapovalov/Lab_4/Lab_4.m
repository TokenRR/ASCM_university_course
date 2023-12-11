% Реальні значення
real_optimal_value = 0;

% Початковий вектор
initial_vector = [2, 2];

function [optimal_vector, optimal_value, error] = optimize_with_octave(initial_vector, real_optimal_value)
    if numel(initial_vector) ~= 2
        error('Початковий вектор повинен мати розмірність 2');
    end

    % Визначаємо функцію у форматі Octave
    eval("function y = objective_function(x) y = (x(1)^2 + 16*x(2)^2); end");

    % Використовуємо функцію fminunc для оптимізації
    options = optimset('fminunc');
    options.Display = 'off';
    [optimal_vector, optimal_value] = fminunc(@objective_function, initial_vector, options);

    % Обчислюємо похибку для мінімального значення функції
    error = abs(optimal_value - real_optimal_value);

    % Виводимо результати з більшою точністю та у науковому форматі
    fprintf('\nРезультати Octave\n');
    disp(['Оптимальний вектор: [' num2str(optimal_vector(1),'%.5e') ', ' num2str(optimal_vector(2),'%.5e') ']']);
    disp(['Мінімальне значення функції: ' num2str(optimal_value,'%.5e')]);
    disp(['Оцінка похибки: ' num2str(error,'%.5e')]);
end

% Виклик функції оптимізації
[optimal_vector, optimal_value, error] = optimize_with_octave(initial_vector, real_optimal_value);

