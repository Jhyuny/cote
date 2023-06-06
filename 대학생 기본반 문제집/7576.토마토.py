"""
https://www.acmicpc.net/problem/7576
"""
from collections import deque

M, N = list(map(int, input().split()))
graph = [list(map(int, input().split())) for _ in range(N)]
q = deque()


def bfs():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1
                    q.append([nx, ny])


for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            q.append([i,j]) # 토마토가 존재하는 좌표를 모두 넣고 한 번에 bfs진행
bfs()
ans = 0
for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit()
    ans = max(ans, max(i))
print(ans - 1)
