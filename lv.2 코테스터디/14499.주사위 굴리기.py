import sys
input = sys.stdin.readline
# (r,c) : r이 늘어나면 아래로, c가 늘어나면 오른쪽으로
N,M,x,y,K = map(int,input().split())
graph = [list(map(int,(input().split(' ')))) for _ in range(N)]
orders = list(map(int,input().split(' ')))
dice = [0]*6 # [0,0,0,0,0,0] = [up, down, left, right, front, back]
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

for move in orders:
    nx = x + dx[move]
    ny = y + dy[move]
    if nx < 0 or nx >= N or ny <0 or ny >= M: # graph 벗어나면 continue
        continue

    up, down, left, right, front, back = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    # 주사위가 굴러가면 그 때의 position index가 달라진다
    if move == 4:
        dice[0], dice[4], dice[1], dice[5] = front, down, back, up 
    elif move == 3:
        dice[0], dice[4], dice[1], dice[5] = back, up, front, down
    elif move == 2:
        dice[3], dice[4], dice[2], dice[5] = front, left, back, right
    else:
        dice[3], dice[4], dice[2], dice[5] = back, right, front, left

    if graph[nx][ny] == 0:
        graph[nx][ny] = dice[5]
    else:
        dice[5] = graph[nx][ny]
        graph[nx][ny] = 0
    x, y = nx, ny
    print(dice[4])
