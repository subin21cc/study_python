# https://www.acmicpc.net/problem/8958
C = int(input())
for _ in range(C):
    s = input()
    c = 0
    score = 0
    for i in s:
        if i == 'O':
            c += 1
            score += c
        else:
            c = 0

    print(score)