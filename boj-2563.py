# https://www.acmicpc.net/problem/2563
n = int(input())
full_width = n * 100
overlap = 0

for _ in range(n):
    a, b = map(int, input().split())
