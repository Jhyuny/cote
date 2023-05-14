"""
https://www.acmicpc.net/problem/10026
"""
from collections import deque

N = int(input())
graph = [list(input()) for _ in range(N)]
# 같은 리스트 객체를 가리키지 않도록 만들려면 아래와 같이 복사해서 만든다
# 이 부분은 다른 사람의 표현 참조
graph1 = [row[:] for row in graph]
graph2 = [row[:] for row in graph]

def bfs(i,j,map,color):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    q = deque()
    q.append([i,j])
    while q:
        x,y = q.pop()
        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]
            if 0<=nx<N and 0<=ny<N and map[nx][ny] in color: # graph이내 + 같은 색이면
                q.append([nx,ny])
                map[nx][ny] = 0 # 방문 처리

cnt1 = 0
cnt2 = 0
for i in range(N):
    for j in range(N):
        if graph1[i][j] == 'R':
            bfs(i,j,graph1,['R'])
            cnt1 += 1
        if graph1[i][j] == 'G':
            bfs(i,j,graph1,['G'])
            cnt1 += 1
        if graph1[i][j] == 'B':
            bfs(i,j,graph1,['B'])
            cnt1 += 1

for i in range(N):
    for j in range(N):
        if graph2[i][j] == 'R' or graph2[i][j] == 'G':
            cnt2 += 1
            bfs(i,j,graph2,['R','G'])
        if graph2[i][j] == 'B':
            bfs(i,j,graph2,['B'])
            cnt2 += 1

print(cnt1,cnt2)