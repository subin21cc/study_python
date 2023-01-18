# https://www.acmicpc.net/problem/5597
find_list = list(range(1,31))
for _ in range(28):
    num = int(input())
    find_list.remove(num)

print(find_list[0], find_list[1])