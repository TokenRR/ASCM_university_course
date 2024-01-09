% Читаємо дані з файлу
fid = fopen('D:\\KPI\\ASKM\\Labs\\Reznichenko\\Lab_5\\umova.txt', 'r');
data = struct('Вартість', [], 'Матриця', [], 'Норми', []);
current_list = [];

while ~feof(fid)
    line = fgetl(fid);
    line = strtrim(line);

    if strncmp(line, '#', 1)
        current_list = strtrim(line(2:end));
    elseif ~isempty(current_list)
        values = sscanf(line, '%f');

        if strcmp(current_list, 'Матриця')
            data.(current_list) = [data.(current_list); values'];
        else
            data.(current_list) = [data.(current_list), values];
        end
    end
end

fclose(fid);

% Визначаємо необхідні змінні
c = data.('Вартість');
A = data.('Матриця');
b = data.('Норми');
lb = [0; 0; 0; 0];
ub = [];
vartype = 'CCCC';
ctype = 'UUU';
sense = 1;

% Викликаємо функцію glpk
[x, fval, status] = glpk(c, A, b, lb, ub, ctype, vartype, sense);

% Виводимо результати
if status == 5
    fprintf('Задачу не вдалося вирішити.\n');
else
    fprintf('\nРозв''язок на мові Octave\n');
    fprintf('Максимальний прибуток: %f\n', -fval);
    fprintf('Оптимальний план випуску продукції:\n');
    fprintf('P1 = %f\n', x(1));
    fprintf('P2 = %f\n', x(2));
    fprintf('P3 = %f\n', x(3));
    fprintf('P4 = %f\n', x(4));
end


