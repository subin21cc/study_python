# https://www.acmicpc.net/problem/1978
N = int(input())
prime_count = 0

for _ in range(N):
    n = int(input())
    for i in range(2, n):
        if n % i != 0:
            prime_count += 1