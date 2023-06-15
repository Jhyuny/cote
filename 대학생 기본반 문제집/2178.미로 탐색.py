"""
https://www.acmicpc.net/problem/2178
"""
from collections import deque
N,M = list(map(int,input().split()))
graph = [list(input()) for _ in range(N)]
q = deque()

def bfs():
    q.append([0,0,1])
    dx,dy=[0,0,1,-1],[1,-1,0,0]
    while q:
        x,y,cnt=q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            ncnt = cnt + 1
            if 0<=nx<N and 0<=ny<M and graph[nx][ny] == '1':
                if nx == N-1 and ny == M-1:
                    return print(ncnt)
                q.append([nx,ny,ncnt])
                graph[nx][ny] = '0'

bfs()