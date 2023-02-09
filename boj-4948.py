# https://www.acmicpc.net/problem/4948
numberdict = {}
while True:
    num = int(input())
    if num == 0:
        break
    cnt = 0
    for i in range(num + 1, 2 * num + 1):
        if str(i) in numberdict:
            if numberdict[str(i)] == True:
                cnt += 1
            else:
                continue

        else:
            for j in range(2, int(i ** 0.5) + 1):
                if i % j == 0:
                    numberdict[str(i)] = False
                    break
            else:
                cnt += 1
                numberdict[str(i)] = True
    print(cnt)
    cnt = 0