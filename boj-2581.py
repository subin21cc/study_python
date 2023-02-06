# https://www.acmicpc.net/problem/2581
def is_prime(n):
    if n > 1:
        for i in range(2,n):
            if n % i == 0:
                return False
        return True
    else:
        return False
    

M = int(input())
N = int(input())
prime_list = []

for i in range(M,N+1):
    if is_prime(i):
        prime_list.append(i)

if len(prime_list) > 0:
    print(sum(prime_list))
    print(min(prime_list))
else:
    print(-1)