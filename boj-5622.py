# https://www.acmicpc.net/problem/5622
word = input()
time = 0
for ch in word:
    if ch == 'A' or ch == 'B' or ch == 'C':
        time += 3
    elif ch == 'D' or ch == 'E' or ch == 'F':
        time += 4
    elif ch == 'G' or ch == 'H' or ch == 'I':
        time += 5
    elif ch == 'J' or ch == 'K' or ch == 'L':
        time += 6
    elif ch == 'M' or ch == 'N' or ch == 'O':
        time += 7
    elif ch == 'P' or ch == 'Q' or ch == 'R' or ch == 'S':
        time += 8
    elif ch == 'T' or ch == 'U' or ch == 'V':
        time += 9
    else:
        time += 10


print(time)