# https://www.acmicpc.net/problem/2941
s = input()
alphabet_count = 0
c_alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
i = 0

while i < len(s):
    for one in c_alphabet:
        if s[i:i+len(one)] == one:
            i += len(one)-1
            break

    alphabet_count += 1
    i += 1

print(alphabet_count)