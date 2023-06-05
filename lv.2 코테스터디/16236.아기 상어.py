"""
https://www.acmicpc.net/problem/16236
"""
from collections import deque

N = int(input())
map = [list(map(int, input().split())) for _ in range(N)]


def bfs(shark_size, n, m):
    l = []  # 움직인 거리수, 물고기의 좌표 저장
    visited = [[0] * N for _ in range(N)]
    q = deque([(n, m)])  # 괄호 빼먹지 않기
    dx = [0, 0, 1, -1]  # right, left, down, up
    dy = [1, -1, 0, 0]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:  # 움직일 수 있는 경우 정의
                if map[nx][ny] < shark_size and map[nx][ny] != 0:  # 물고기가 상어보다 작을 때
                    l.append([visited[x][y], nx, ny])
                    visited[nx][ny] = visited[x][y] + 1
                elif map[nx][ny] == shark_size:  # 물고기랑 상어의 크기가 같을 때
                    visited[nx][ny] = visited[x][y] + 1
                    q.append([nx, ny])
                elif map[nx][ny] == 0:  # 물고기가 존재하지 않을 때
                    visited[nx][ny] = visited[x][y] + 1
                    q.append([nx, ny])
    return sorted(l, key=lambda x: (x[0], x[1], x[2]))  # 제일 가까운 것, 가장 위쪽, 가장 왼쪽 순서로 정렬


for i in range(N):
    for j in range(N):
        if map[i][j] == 9:
            shark = [i, j]
i, j = shark
shark_size = 2
cnt = 0
time = 0
while True:
    map[i][j] = shark_size
    move = deque(bfs(shark_size, i, j))
    if not move:
        break
    step, x, y = move.popleft()  # eat
    time += step + 1
    cnt += 1  # count
    if cnt == shark_size:
        shark_size += 1
        cnt = 0
    map[i][j] = 0
    i, j = x, y
print(time)
