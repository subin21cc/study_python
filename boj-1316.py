# https://www.acmicpc.net/problem/1316
def is_group_word(s):
    for i in range(len(s)):
        flag = 0
        for j in range(i+1, len(s)):
            if flag == 0:
                if s[i] != s[j]:
                    flag = 1
            else:
                if s[i] == s[j]:
                    return False
    return True


n = int(input())
group_word_count = 0

for _ in range(n):
    s = input()
    if is_group_word(s):
        group_word_count += 1

print(group_word_count)


