"""
https://www.acmicpc.net/problem/19236
"""
import sys
input = sys.stdin.readline
dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]
graph = []
shark = [0,0]
fishes = {}
for i in range(4):
    fish = input().rstrip().split(' ')
    for j,a in enumerate(range(0,len(fish),2)):
        fishes[fish[a]] = [fish[a+1],[i,j]]
fishes = dict(sorted(fishes.items(), key=lambda x: x[0]))
print(fishes) # key : number of fish, value['direction',[fish_x,fish_y]]

x,y = start = [0,0]
nx,ny = start
while 0<=nx<4 or 0<=ny<4:
    shark[0] = shark[0] + graph[x][y][0] # eating
    shark[1] = graph[x][y][1]
    
    # move_fish
    for a,b in fishes.items():
        fishes[a] = []
    # move_shark
    choose = []
    while 0<=nx<4 or 0<=ny<4:
        nx = x + dx[shark[1]]
        ny = y + dy[shark[1]]
        choose.append(graph[nx][ny][0])

print(shark[0])



