# https://www.acmicpc.net/problem/1546
_ = input()
n_list = list(map(int, input().split()))
M = max(n_list)
m_list = []
for one in n_list:
    m_list.append(one / M * 100)
print(sum(m_list) / len(m_list))
