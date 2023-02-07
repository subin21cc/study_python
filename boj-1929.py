# https://www.acmicpc.net/problem/1929
M, N = map(int, input().split())

for i in range(M, N+1):
    if i > 1:
        prime = True
        max = int(i ** 0.5)

        for j in range(2,max+1):
            if i % j == 0:
                prime = False
                break

        if prime:
            print(i)