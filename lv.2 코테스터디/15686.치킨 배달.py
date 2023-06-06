"""
https://www.acmicpc.net/problem/15686
"""
from collections import deque
N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]
print(graph)
chicken = []
q = deque()
for i in range(N):
    for j in range(N):
        if graph[i][j] == 2:
            chicken.append([i,j])

def bfs(i,j):
    visited = [[0]*N for _ in range(N)]
    l = []
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    x,y = i,j
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<N and 0<=ny<N:
            if visited[nx][ny] == 1: # 
                q.append([nx,ny])
                visited[nx][ny] = visited[x][y]+1
            elif graph[nx][ny] == 0:
                q.append([nx,ny])