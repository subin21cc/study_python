# https://www.acmicpc.net/problem/2292
import math
N = int(input())
x2 = math.sqrt(1/3*(N-0.25)) + 0.5
# print(x2)
x = int(math.sqrt(1/3*(N-0.25)) + 0.5 - 0.00000001) + 1
print(x)

xx = 18257
nn = 3*xx*xx - 3*xx + 1
# print(nn)
