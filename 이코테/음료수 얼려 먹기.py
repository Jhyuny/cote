from collections import deque

N, M = list(map(int,input().split()))
graph = [list(input()) for _ in range(N)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(graph,a,b):
    q = deque()
    q.append([b,a])
    while q:
        y,x = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<M and 0<=ny<N: # 범위 내에 있고
                if graph[ny][nx]=='0':
                    graph[ny][nx]='1'
                    q.append([ny,nx])

cnt = 0
for a in range(M):
    for b in range(N):
        if graph[b][a]=='0':
            bfs(graph,a,b)
            cnt += 1
print(cnt)