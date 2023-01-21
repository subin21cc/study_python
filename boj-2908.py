# https://www.acmicpc.net/problem/2908
a, b = input().split()
A = a[::-1]
B = b[::-1]
if int(A) > int(B):
    print(A)
else:
    print(B)