# https://www.acmicpc.net/problem/2869
A, B, V = map(int, input().split())
x = int((V - B) / (A - B) - 0.00001) + 1
print(x)