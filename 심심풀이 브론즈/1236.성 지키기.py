"""
https://www.acmicpc.net/problem/1236
"""
N, M = map(int,input().split())
graph = [list(input()) for _ in range(N)]

x = []
y = []

for i in range(N):
    for j in range(M):
        if graph[i][j] == 'X':
            x.append(i)
            y.append(j)

print(max(N-len(set(x)),M-len(set(y))))