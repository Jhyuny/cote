"""
https://www.acmicpc.net/problem/2583
"""
from collections import deque

M, N, K = map(int, input().split())
graph = [[0]*N for _ in range(M)]


def bfs(graph,i, j):
    q = deque()
    q.append((i, j))
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    cnt = 1
    while q:
        y, x = q.popleft() # 좌표이므로
        for k in range(4):
            ny = y+dy[k]
            nx = x+dx[k]
            if (0 <= ny < M) and (0 <= nx < N) and graph[ny][nx] == 0:
                graph[ny][nx] = 1
                q.append((ny, nx))
                cnt += 1
    return cnt


for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] += 1

answer = []

for i in range(M):
    for j in range(N):
        if graph[i][j] == 0:
            graph[i][j] += 1
            answer.append(bfs(graph,i, j))

print(len(answer))
ans = ''
for i in sorted(answer):
    ans = ans + str(i)+' '
print(ans.rstrip())