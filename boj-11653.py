# https://www.acmicpc.net/problem/11653
N = int(input())

while N != 1:
    for i in range(2, N+1):
        if N % i == 0:
            print(i)
            N = N // i
            break


'''
for i in range(2, N):
    for j in range(2, N):
        if N % i == 0:
            print(i)
            N = N / i
i는 2부터 N
N을 i로 나눠서 나머지가 0이 되면 i를 프린트하고
나눈 N(N / i)을 다시 i부터 나눠서 나머지가 0이 되면 i를 프린트,
N / i == 1 이 되면 멈춤
'''