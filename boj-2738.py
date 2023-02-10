# https://www.acmicpc.net/problem/2738
N, M = map(int, input().split())
a = []
for i in range(N):
    a.append(list(map(int, input().split())))

b = []
for i in range(N):
    b.append(list(map(int, input().split())))

procession = []

for i in range(N):
    procession.append([0]*M)

for i in range(N):
    for j in range(M):
        procession[i][j] = a[i][j] + b[i][j]

for i in range(N):
    print(*procession[i])