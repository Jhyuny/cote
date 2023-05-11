"""
https://www.acmicpc.net/problem/19236
"""
import sys
input = sys.stdin.readline
dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]
shark = [0,0]
fishes = {}
for i in range(4):
    fish = input().rstrip().split(' ')
    for j,a in enumerate(range(0,len(fish),2)):
        fishes[fish[a]] = [int(fish[a+1]),[i,j]]
fishes = dict(sorted(fishes.items(), key=lambda x: x[0]))
print(fishes) # key : number of fish, value['direction',[fish_x,fish_y]]
locations = fishes.values()
x,y = start = [0,0]
nx,ny = start
while 0<=nx<4 or 0<=ny<4:
    for idx,location in enumerate(locations):
        if [x,y] in location:
            """need to fill out"""
            pass
    shark[0] = shark[0] + graph[x][y][0] # eating
    shark[1] = graph[x][y][1]
    # move_fish
    for a,info in fishes.items(): # (n_fish, ['direction',[fish_x,fish_y]])
        fx,fy = info[1]
        while True:
            nfx = fx+dx[info[0]]
            nfy = fy+dy[info[0]]
            if [nfx,nfy] != [x,y] or 0<=nfx<4 or 0<=nfy<4: # can move
                fx,fy = nfx,nfy
                fishes[a]=[info[0],[fx,fy]]
            else: # cannot move -> change direction
                info[0] = info[0]+1
                if info[0]>9:
                    info[0] = info[0]-9
    print('finish moving :', fishes)

    # move_shark
    choose = []
    while 0<=nx<4 or 0<=ny<4:
        nx = x + dx[shark[1]]
        ny = y + dy[shark[1]]
        choose.append(graph[nx][ny][0])
    x = nx
    y = ny
print(shark[0])



