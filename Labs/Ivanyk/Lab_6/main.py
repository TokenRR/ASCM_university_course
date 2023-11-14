from oct2py import octave
import numpy as np
from collections import Counter


def umova():
    with open('data.txt', 'r', encoding='utf-8') as file:
        lines = [line.strip() for line in file.readlines()]

    # Знайти рядки з мітками
    indices = {label: lines.index(label) for label in ['вектор a', 'вектор b', 'матриця С']}

    # Читання векторів та матриці
    a = np.fromstring(lines[indices['вектор a'] + 1], sep=',')
    b = np.fromstring(lines[indices['вектор b'] + 1], sep=',')
    C_start, C_end = indices['матриця С'] + 1, len(lines)
    C = np.genfromtxt(lines[C_start:C_end], delimiter=',')

    return a, b, C


def transport(supply, demand, costs):
    assert sum(supply) == sum(demand)

    s, d, C = np.copy(supply), np.copy(demand), np.copy(costs)
    n, m = C.shape
    X = np.zeros((n, m))
    indices = [(i, j) for i in range(n) for j in range(m)]
    xs = sorted(zip(indices, C.flatten()), key=lambda a_b: a_b[1])

    for (i, j), _ in xs:
        if d[j] != 0:
            remains = s[i] - d[j] if s[i] >= d[j] else 0
            grabbed = s[i] - remains
            X[i, j], s[i], d[j] = grabbed, remains, d[j] - grabbed

    while True:
        u = np.array([np.nan] * n)
        v = np.array([np.nan] * m)
        S = np.zeros((n, m))

        nonzero = list(zip(*np.where(X > 0)))
        u[nonzero[0][0]] = 0

        while any(np.isnan(u)) or any(np.isnan(v)):
            for i, j in nonzero:
                if np.isnan(u[i]) and not np.isnan(v[j]):
                    u[i] = C[i, j] - v[j]
                elif not np.isnan(u[i]) and np.isnan(v[j]):
                    v[j] = C[i, j] - u[i]

        S = C - u[:, None] - v
        s = np.min(S)

        if s >= 0:
            break

        start = tuple(np.argwhere(S == s)[0])
        T = np.copy(X)
        T[start] = 1

        while True:
            _xs, _ys = np.nonzero(T)
            xcount, ycount = Counter(_xs), Counter(_ys)

            for x in xcount.keys():
                if xcount[x] <= 1: T[x, :] = 0
            for y in ycount.keys():
                if ycount[y] <= 1: T[:, y] = 0

            if all(x > 1 for x in xcount.values()) and all(y > 1 for y in ycount.values()):
                break

        path = [start]
        fringe = set(tuple(p) for p in np.argwhere(T > 0))
        size = len(fringe)

        while len(path) < size:
            last = path[-1]
            fringe.remove(last)
            next_ = min(fringe, key=lambda x_y: abs(last[0]-x_y[0]) + abs(last[1]-x_y[1]))
            path.append(next_)

        neg, pos = path[1::2], path[::2]
        q = min(X[tuple(zip(*neg))])
        X[tuple(zip(*neg))] -= q
        X[tuple(zip(*pos))] += q

    return X, np.sum(X * C)

supply, demand, costs = umova()
# print(supply)
# print(demand)
# print(costs)
routes, total_cost = transport(supply, demand, costs)

print('\n\nРозв\'язок на мові Python\n')
print('Оптимальний план перевезень:')
print(routes)
print(f'Мінімальна вартість перевезень: {total_cost}')



C = costs.astype(int).flatten().tolist()
b = np.concatenate((supply, demand)).astype(int).tolist()

m = len(supply)
n = len(demand)

A_eq = octave.zeros(m + n, m * n)
b_eq = octave.zeros(m + n, 1)

for i in range(m):
    A_eq[i, i*n:(i+1)*n] = 1
    b_eq[i] = b[i]

for j in range(n):
    A_eq[m+j, j::n] = 1
    b_eq[m+j] = b[m+j]

lb = octave.zeros(m * n, 1)
ub = octave.inf(m * n, 1)

param = {'msglev': 1}  #  двофазний простий симплекс
ctype = 'S' * (m + n)
vartype = 'C' * (m * n)
sense = 1 
results = octave.glpk(C, A_eq, b_eq, lb, ub, ctype, vartype, sense, param)
plan = np.reshape(results, (n, m)).T
oct_total_cost = octave.dot(C, results)

print('\n\nРозв\'язок на мові Octave\n')
print('Оптимальний план перевезень:')
print(plan)
print(f'Мінімальна вартість перевезень: {oct_total_cost}')
