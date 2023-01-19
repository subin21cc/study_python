# https://www.acmicpc.net/problem/1065
def is_han_number(n):
    if n < 100:
        return True
    s = str(n)
    for i in range(len(s) - 2):
        if int(s[i + 1]) - int(s[i]) != int(s[i + 2]) - int(s[i + 1]):
            return False
    return True


'''
print(is_han_number(100))
print(is_han_number(99))
print(is_han_number(123))
print(is_han_number(12345))
print(is_han_number(12346))

'''
N = int(input())
count = 0
for i in range(1, N + 1):
    if is_han_number(i):
        count += 1

print(count)
# '''
