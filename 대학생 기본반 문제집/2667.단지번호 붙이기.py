"""
https://www.acmicpc.net/submit/2667
"""
from collections import deque

N = int(input())
graph = [list(input()) for _ in range(N)]
ans = 0
answers = []


def bfs(i, j, graph):
    num = 1
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    x = i
    y = j
    q = deque()
    graph[i][j] = "0"  # 현재 위치 방문처리
    q.append([x, y])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == "1":
                q.append([nx, ny])
                num += 1
                graph[nx][ny] = "0"
    return num


for i in range(N):
    for j in range(N):
        if graph[i][j] == "1":
            answers.append(bfs(i, j, graph))
            ans += 1

print(ans)
for i in sorted(answers):  # 오름차순 출력
    print(i)
