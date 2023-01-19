# https://www.acmicpc.net/problem/10809

n_list = [-1] * 26
S = input()
for i in range(len(S)):
    if n_list[ord(S[i]) - ord('a')] == -1:
        n_list[ord(S[i]) - ord('a')] = i

for one in n_list:
    print(one, end=' ')

'''
n_list[ord('b')-ord('a')] = 0
print(n_list)

print(ord('a'))
print(ord('b'))
print(ord('z'))
'''
