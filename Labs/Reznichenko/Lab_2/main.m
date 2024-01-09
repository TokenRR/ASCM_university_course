pkg load symbolic;  % Завантаження пакету symbolic

% Читання формули, первісної та меж інтегрування з файлу
try
    fid = fopen('D:\\KPI\\ASKM\\Labs\\Reznichenko\\Lab_2\\umova.txt', 'r');
    lower_limit = str2double(fgetl(fid));
    upper_limit = str2double(fgetl(fid));
    n = str2double(fgetl(fid));
    func_str = fgetl(fid);
    antiderivative_str = fgetl(fid);
    fclose(fid);
catch
    disp('ERROR: Помилка при читанні файлу');
end_try_catch


% Заміна символів у рядках
func_str = strrep(func_str, '.', '');
func_str = strrep(func_str, '**', '^');
antiderivative_str = strrep(antiderivative_str, '.', '');
antiderivative_str = strrep(antiderivative_str, '**', '^');

% Обчислення формули похідної
func_derivative = diff(sym(func_str));

% Обчислення значень функцій у цих точках
h = (upper_limit - lower_limit) / n;  %  Крок
x_values = lower_limit:h:upper_limit;  % Створюємо масив точок на інтервалі [a, b] з кроком h
func_values = arrayfun(@(x) eval(func_str), x_values);
func_derivative_values = arrayfun(@(x) eval(func_derivative), x_values);

% Обчислення різниці між значеннями функцій
difference = func_values - func_derivative_values;

% Виведення результатів
printf('\n\n')
disp('Диференціювання за допомогою Octave');
printf('%5s %20s %20s %20s\n', 'x', 'f(x)', '(F(x)'')', 'Різниця');
printf('%5.2f %20.15f %20.15f %20.15f\n', [x_values; func_values; func_derivative_values; abs(difference)]);

% Обчислюємо чисельне значення визначеного інтегралу для кожної точки
simpson = arrayfun(@(i) trapz(x_values(1:i), func_values(1:i)), 1:length(x_values));

% Обчислюємо чисельне значення визначеного інтегралу за допомогою методу Ньютона-Лейбніца
newton_leibniz = arrayfun(@(x) eval(strrep(antiderivative_str, 'x', num2str(x))), x_values) - eval(strrep(antiderivative_str, 'x', num2str(lower_limit)));

% Обчислюємо різницю між значеннями, отриманими двома методами
difference = abs(simpson - newton_leibniz);

% Виведення результатів
printf('\n\n')
disp('Інтегрування за допомогою Octave');
printf('%5s %25s %40s %25s\n', 'x', 'м.Сімпсона', 'м.Ньютона-Лейбніца', 'Різниця');
printf('%5.2f %20.15f %20.15f %20.15f\n', [x_values; simpson; newton_leibniz; difference]);

