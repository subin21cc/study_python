# https://www.acmicpc.net/problem/1157

def toUpper(s):
    result = ''
    for ch in s:
        if 'A' <= ch <= 'Z':
            result += ch
        else:
            result += chr(ord(ch)-ord('a')+ord('A'))
    return result


word = input()
a_list = [0]*26

for ch in toUpper(word):
    a_list[ord(ch)-ord('A')] += 1

if a_list.count(max(a_list)) >= 2:
    print('?')
else:
    print(chr(a_list.index(max(a_list))+ord('A')))

'''
print(toUpper('Mississipi'))

print(ord('a'), ord('z'))
print(ord('A'), ord('Z'))
print(chr(ord('n')-ord('a')+ord('A')))
'''