"""
https://www.acmicpc.net/problem/1764
"""
N, M = map(int,input().split(' '))
L = [input() for _ in range(N)]
S = [input() for _ in range(M)]
answer = list(set(L)&set(S))
print(len(answer))
for i in sorted(answer):
    print(i)