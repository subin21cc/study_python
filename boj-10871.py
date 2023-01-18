# https://www.acmicpc.net/problem/10871
N, X = map(int, input().split())
A = list(map(int, input().split()))

for one in A:
    if one < X:
        print(one, end=' ')