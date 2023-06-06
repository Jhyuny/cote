"""
https://www.acmicpc.net/problem/7576
"""
from collections import deque

M, N = list(map(int, input().split()))
graph = [list(map(int, input().split())) for _ in range(N)]
q = deque()


def bfs(i, j, graph):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q.append([i, j])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1
                    q.append([nx, ny])
    print(graph)


for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            bfs(i, j, graph)
ans = 0
for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit()
    ans = max(ans, max(i))
print(ans - 1)
