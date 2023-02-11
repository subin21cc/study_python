# https://www.acmicpc.net/problem/2566
import sys
input = sys.stdin.readline
matrix = []

for _ in range(9):
    matrix.append(list(map(int, input().split())))

x = 0
y = 0
max = -1

for i in range(9):
    for j in range(9):
        if matrix[i] [j] > max:
            max = matrix[i] [j]
            x = i + 1
            y = j + 1

print(max)
print(x, y)