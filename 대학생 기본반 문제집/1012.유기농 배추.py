"""
https://www.acmicpc.net/problem/1012
"""
from collections import deque

# idx에 따라 상하좌우
dx = [0,0,-1,1] 
dy = [1,-1,0,0]

N = int(input())

def bfs(graph, a, b):
    queue = deque()
    queue.append((a,b)) # 현재 위치
    graph[a][b] = 0 # graph에서 방문처리

    while queue:
        x, y = queue.popleft()
        for i in range(4): # 4방향 모두 탐색
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or nx >=n or ny < 0 or ny >= m: # 범위 넘어서면 그냥 지나간다
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0 # 방문처리하고
                queue.append((nx, ny)) # 해당 위치 q에 append
    return

for i in range(N):
    cnt = 0
    n, m, k = map(int,input().split())
    graph = [[0]*m for _ in range(n)]

    for j in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1

    for a in range(n): # 1인 부분 만나면 연결된 부분 탐색(through bfs)
        for b in range(m):
            if graph[a][b] == 1:
                bfs(graph, a, b)
                cnt += 1
    print(cnt)