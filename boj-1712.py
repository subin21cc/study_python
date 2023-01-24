# https://www.acmicpc.net/problem/1712
# A:고정비용, B:가변비용, C:가격
A, B, C = map(int, input().split())
if B >= C:
    print(-1)
else:
    n = A // (C - B) + 1
    print(n)

'''
    while True:
        total_income = C * n
        total_cost = A + B * n
        if total_income > total_cost:
            print(n)
            break
        n += 1
'''
