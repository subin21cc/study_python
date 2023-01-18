# https://www.acmicpc.net/problem/4344
C = int(input())
for _ in range(C):
    l = list(map(int, input().split()))

    ll = l[1:]
    average = sum(ll) / len(ll)
    count = 0
    for one in ll:
        if one > average:
            count += 1
    print('{0:.3f}%'.format(count / len(ll) * 100))
