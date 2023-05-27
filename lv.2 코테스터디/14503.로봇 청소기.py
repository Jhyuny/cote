"""
https://www.acmicpc.net/problem/14503
"""
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]

def bfs(i, j, d):
    cnt = 0
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    queue = deque()
    queue.append((i, j)) # 로봇 위치
    visited[i][j] = 1 # 시작 위치 방문처리 잊지 않기.
    cnt += 1 # 시작 위치 청소

    while queue:
        x, y = queue.popleft()
        cango = 0

        for _ in range(4):
            d = (d + 3) % 4
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < n and 0 <= ny < m and not graph[nx][ny]: 
                if not visited[nx][ny]:
                    visited[nx][ny] = 1  
                    queue.append((nx, ny))
                    cnt += 1
                    cango = 1
                    break

        if cango == 0: # 네 방향 모두 이동할 수 없다면
            if graph[x - dx[d]][y - dy[d]] != 1: # 벽이 아니라면
                queue.append((x - dx[d], y - dy[d])) # 후진
            else: # 벽이면
                print(cnt) # 정지
                break
bfs(r,c,d)