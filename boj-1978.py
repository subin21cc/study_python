# https://www.acmicpc.net/problem/1978
N = int(input())
num = map(int, input().split())
prime_list = []

for i in num:
    a = 0
    if i == 1:
        continue

    for j in range(2,i):
        if i % j == 0:
            a += 1
    if a == 0:
        prime_list.append(i)

print(len(prime_list))
