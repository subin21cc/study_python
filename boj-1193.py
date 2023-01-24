# https://www.acmicpc.net/problem/1193
x = int(input())
n = int((2*x - 7/4)**0.5 + 0.5)
first = int((n*n - n)/2 + 1)
r1 = n - x + first
r2 = x - first + 1

if n % 2 == 0:
    print('{}/{}'.format(r2, r1))
else:
    print('{}/{}'.format(r1, r2))
