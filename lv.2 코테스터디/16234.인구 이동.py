"""
https://www.acmicpc.net/problem/16234
"""
from collections import deque
q = deque()
N, L, R = list(map(int,input().split()))
graph = [list(map(int,input().split())) for _ in range(N)]

def bfs(i,j):
    union=[] # 연합국 모임
    dx,dy = [0,0,1,-1], [1,-1,0,0]
    q.append([i,j])
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N and visited[nx][ny] == 0:
                if L<=abs(graph[nx][ny]-graph[x][y])<=R:
                    union.append([nx,ny]) # 조건 만족 시, 연합에 추가
                    q.append([nx,ny]) # 현재 나라에서 또 다른 나라 탐색
                    visited[nx][ny] = 1 # 방문처리
    return union

cnt = 0
while True:
    check = 0
    visited = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                union = bfs(i,j)
                # 인구 이동
                if union:
                    total = 0
                    for country in union:
                        x,y = country
                        total += graph[x][y]
                    num = total//len(union)
                    for country in union:
                        x,y = country
                        graph[x][y] = num
                    check += 1
    if check == 0:
        break
    cnt += 1

print(cnt)

            
    