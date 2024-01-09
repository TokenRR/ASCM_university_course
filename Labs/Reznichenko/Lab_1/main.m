% Зчитування матриці A та вектора b з файлів
try
    tic;  % Початок вимірювання часу
    matrix_A = dlmread('D:\\KPI\\ASKM\\Labs\\Reznichenko\\Lab_1\\matrix.txt');
    vector_b = dlmread('D:\\KPI\\ASKM\\Labs\\Reznichenko\\Lab_1\\vector.txt');
catch
    disp('ERROR: Помилка при зчитуванні матриці або вектора');
end_try_catch

if length(vector_b) != size(matrix_A, 1)
    disp('ERROR: Помилка: Вектор b не відповідає розмірності матриці А.');
end

if length(vector_b) >= 10 || size(matrix_A, 1) >= 10
    disp('Введіть матрицю меншої розмірності');
end

% Розв'язання СЛАР Ax = b
try
    solution = matrix_A \ vector_b;

    % Обчислення похибки
    accuracy = mean((vector_b - matrix_A * solution) .^ 2);
    execution_time = toc;  % Кінець вимірювання часу
    disp(['Час виконання: ', num2str(execution_time), ' сек']);
    disp(['Похибка: ', num2str(accuracy, '%.3e')]);
    disp(['Результат: ', mat2str(solution)]);
catch
    disp('ERROR: Помилка при розв`язанні СЛАР');
end_try_catch

