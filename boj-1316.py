# https://www.acmicpc.net/problem/1316
def is_group_word(s):
    flag = 0
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            if flag == 0:
                if s[i] != s[j]:
                    flag = 1
            else:


n = int(input())
group_word = 0

for _ in range(n):
    s = input()
    if is_group_word(s):
        group_word += 1

print(group_word)


