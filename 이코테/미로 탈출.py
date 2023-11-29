from collections import deque

N,M = map(int,input().split())
graph = [list(input()) for _ in range(N)]
dis = [[0 for _ in range(M)] for _ in range(N)]

dis[0][0] = 1

q = deque()
q.append([0,0])

dx = [0,0,1,-1]
dy = [1,-1,0,0]
while q:
    y,x = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<M and 0<=ny<N:
            if graph[ny][nx] == '1':
                q.append([ny,nx])
                graph[ny][nx] = 0
                dis[ny][nx] = dis[y][x] + 1

print(dis[N-1][M-1])