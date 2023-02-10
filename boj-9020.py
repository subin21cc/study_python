# https://www.acmicpc.net/problem/9020
def find_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

prime_list1 = []
for i in range(2, 10000):
    if find_prime(i):
        prime_list1.append(i)

T = int(input())

for _ in range(T):
    prime_list2 = list(prime_list1)
    a = int(input())
    if a % 2 == 1 or a <= 3 or a > 10000:
        continue
    prime_list2.append(a//2)
    prime_list2.sort()
    b = prime_list2.index(a//2)

    for i in range(b, -1, -1):
        if a-prime_list2[i] in prime_list1:
            if a-prime_list2[i] > prime_list2[i]:
                print(prime_list2[i], a-prime_list2[i])
                break
            else:
                print(a-prime_list2[i], prime_list2[i])
                break