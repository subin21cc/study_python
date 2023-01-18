# https://www.acmicpc.net/problem/3052
remain_list = []
for _ in range(10):
    num = int(input())
    remain = num % 42
    if remain not in remain_list:
        remain_list.append(remain)

print(len(remain_list))
