% Матриця витрат
costs = [
    5, 4, 20, 5, 14;
    19, 20, 2, 4, 5;
    9, 6, 8, 19, 1;
    7, 15, 20, 6, 11
];

% Об'єми виробництва та об'єми потреб
supplies = [60, 50, 40, 20];
demands = [10, 50, 40, 50, 20];

B = [
    5, 20, 14, 25, 13;
    19, 22, 15, 4, 12;
    6, 8, 15, 5, 10;
    14, 7, 2, 23, 20
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

