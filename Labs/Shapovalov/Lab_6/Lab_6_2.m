% Матриця витрат
costs = [
    18, 14, 6, 8, 7;
    8, 19, 9, 16, 17;
    18, 10, 14, 7, 19;
    1, 6, 10, 5, 13
];

% Об'єми виробництва та об'єми потреб
supplies = [72, 29, 68, 26];
demands = [65, 24, 50, 30, 26];

B = [
    12, 20, 30, 20, 10;
    20, 4, 3, 2, 8;
    13, 10, 30, 10, 15;
    23, 5, 6, 4, 6
];

% Перетворення задачі у вигляд лінійного програмування
num_supplies = length(supplies);
num_demands = length(demands);
flatten_costs = reshape(costs', 1, []);

% Коефіцієнти цільової функції (вартість перевезень)
c = flatten_costs;

% Коефіцієнти лівих частин обмежень (обсяги виробництва та споживання)
A_eq = zeros(num_supplies + num_demands, num_supplies * num_demands);
for i = 1:num_supplies
    for j = 1:num_demands
        A_eq(i, (i - 1) * num_demands + j) = 1;
        A_eq(num_supplies + j, (i - 1) * num_demands + j) = 1;
    end
end

% Праві частини обмежень (суми обсягів)
b_eq = [supplies, demands];

% Згенеруйте вектор меж для кожного x_ij на основі матриці обмежень B
bounds = zeros(num_supplies * num_demands, 2);
for i = 1:num_supplies * num_demands
    bounds(i, :) = [0, Inf];
end

% Виклик функції glpk для знаходження оптимального розв'язку
result = glpk(c, A_eq, b_eq, bounds(:, 1), bounds(:, 2));

% Перетворення результату назад у форму costs
result = reshape(result, num_demands, num_supplies)';

% Виведення результату
disp('Розв''язок транспортної задачі (з обмеженнями) на мові Octave');
disp('Оптимальний план перевезень:');
disp(result);
disp(['Мінімальні витрати перевезень: ', num2str(sum(sum(result .* costs)))]);

