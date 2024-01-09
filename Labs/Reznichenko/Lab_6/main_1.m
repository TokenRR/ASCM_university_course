% Вхідні дані
supply = [21, 19, 15, 25];
demand = [15, 15, 15, 15, 20];
costs = [
  30, 24, 11, 12, 25;
  26, 4, 29, 20, 24;
  27, 14, 14, 10, 18;
  6, 14, 28, 8, 2
];

% Перетворення векторів та матриці в необхідні дані для GLPK
C = reshape(costs', 1, numel(costs))';
b = [supply, demand]';

m = length(supply);
n = length(demand);

A_eq = zeros(m + n, m * n);
b_eq = zeros(m + n, 1);

for i = 1:m
    A_eq(i, (i-1)*n + 1:i*n) = 1;
    b_eq(i) = b(i);
end

for j = 1:n
    A_eq(m+j, j:n:m*n) = 1;
    b_eq(m+j) = b(m+j);
end

lb = zeros(m * n, 1);
ub = inf(m * n, 1);

param.msglev = 1; % двофазний простий симплекс
ctype = repmat('S', 1, m + n);
vartype = repmat('C', 1, m * n);
sense = 1;
results = glpk(C, A_eq, b_eq, lb, ub, ctype, vartype, sense, param);
plan = reshape(results, n, m)';
oct_total_cost = dot(C, results);

% Виведення результатів
fprintf('\nРозв''язок транспортної задачі (без обмежень) на мові Octave\n');
fprintf('Оптимальний план перевезень:\n');
disp(plan);
fprintf('Мінімальна вартість перевезень: %f\n', oct_total_cost);

