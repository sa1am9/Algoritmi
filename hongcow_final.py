inf = 1000000000
n = int(input())
data = [[0 for i in range(n)] for j in range(n)]


for i in range(0, n):                           # считывание информации и формирование матрицы А
    for j in range(0, i+1):
        if i != j:
            input_string = input().split()
            for k in range(0, i):
                tmp = input_string[k]
                if tmp == 'x':
                    data[i][k] = inf
                else:
                    data[i][k] = int(tmp)
                data[k][i]=data[i][k]
            break

edges = dict()

for i in range(n):
    for j in range(n):
        if data[i][j] == 0 or data[i][j] == inf:
            pass
        else:
            edges[(i, j)] = data[i][j]


F = [[inf] * n for i in range(n)]             # матрица самых коротких расстояний от стартовой вершины до всех остальных вершин, которые состоят из k
F[0][0] = 0
for k in range(1, n):                       # алгоритм Беллмана-Форда
    for i in range(n):
         F[k][i] = F[k - 1][i]
         for j in range(n):
             try:
                 if F[k - 1][j] + edges[j, i] < F[k][i]:
                     F[k][i] = F[k - 1][j] + edges[j, i]
             except KeyError:
                 pass

ans = 0
for i in range(0, n):
    ans = max(F[n-1][i], ans)               # так как процессы параллельно идут - выбираем максимальное время, которое гарантированно охватит все вершины
print(ans)
