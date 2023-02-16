# https://www.acmicpc.net/problem/2563
import sys
paper = [[0] * 100 for _ in range(100)]
T = int(sys.stdin.readline())
width = 0

for i in range(T):
    X, Y = map(int, sys.stdin.readline().split())
    Y = 99 - Y
    for j in range(Y - 10, Y):
        for z in range(X, X + 10):
            paper[j][z] = 1

for i in range(100):
    width += paper[i].count(1)

print(width)

