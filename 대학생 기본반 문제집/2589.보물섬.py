"""
https://www.acmicpc.net/problem/2589
"""
from collections import deque
h,w = map(int,input().split())
map = [list(input()) for _ in range(h)]

def bfs(i,j):
    # 하, 상, 우, 좌
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    visited = [[-1]*w for _ in range(h)]
    t = 0
    q = deque()
    q.append([i,j]) # 출발 지점
    visited[i][j] = 0 
    while q:
        y,x = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<w and 0<=ny<h and map[ny][nx] == 'L' and visited[ny][nx] == -1:
                visited[ny][nx] = visited[y][x] + 1
                t = max(t,visited[ny][nx])
                q.append([ny,nx])
    return t

ans = 0
for i in range(h):
    for j in range(w):
        if map[i][j] == 'L':
            time= bfs(i,j)
            ans = max(ans,time)

print(ans)
                