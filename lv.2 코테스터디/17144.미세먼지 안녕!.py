"""
https://www.acmicpc.net/problem/17144
"""
R, C, T = list(map(int, input().split()))
graph = [list(map(int, input().split())) for _ in range(R)]


def diff():
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]

    tmp_graph = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if graph[i][j] != 0 and graph[i][j] != -1:
                tmp = 0
                for k in range(4):
                    nx = dx[k] + i
                    ny = dy[k] + j
                    if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] != -1:
                        tmp_graph[nx][ny] += graph[i][j] // 5
                        tmp += graph[i][j] // 5
                graph[i][j] -= tmp

    for i in range(R):
        for j in range(C):
            graph[i][j] += tmp_graph[i][j]  # 1초에 한 번씩 이동하므로 따로 구한 뒤 더한다.


def air_up():
    # 방향 오른쪽, 위쪽, 왼쪽, 아래쪽, 오른쪽으로 설정
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0
    x, y = up, 1
    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == up and y == 0:
            break
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            direct += 1
            continue
        graph[x][y], before = before, graph[x][y]
        x = nx
        y = ny


def air_down():
    # 방향 오른쪽, 아래쪽, 왼쪽, 위쪽, 오른쪽으로 설정
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0
    x, y = down, 1
    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == down and y == 0:
            break
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            direct += 1
            continue
        graph[x][y], before = before, graph[x][y]
        x = nx
        y = ny


for _ in range(T + 1):  # T초동안 반복
    for i in range(R):
        for j in range(C):
            if graph[i][j] == -1:
                up = i
                down = i + 1
    diff()
    air_up()
    air_down()

ans = 0
for i in range(R):
    ans += sum(graph[i])
print(ans)
