# https://www.acmicpc.net/problem/2562
n_max = 0
index = 0
for i in range(1,10):
    num = int(input())
    if num > n_max:
        n_max = num
        index = i

print(n_max)
print(index)