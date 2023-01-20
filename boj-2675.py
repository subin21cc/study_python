# https://www.acmicpc.net/problem/2675
t = int(input())
for _ in range(t):
    n, s = input().split()
    for ch in s:
        for _ in range(int(n)):
            print(ch, end='')
    print()

