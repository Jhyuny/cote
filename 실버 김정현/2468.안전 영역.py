"""
https://www.acmicpc.net/problem/2468
"""
from collections import deque

N = int(input())

area = []
visited = [[False]*N for _ in range(N)]

# read the map
for i in range(N):
    area.append(list(map(int,input().split())))

# find max value
m = 0
for i in range(N):
    m = max(m,max(area[i]))

def count_safety_area(graph,x,y):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    queue = deque()
    queue.append((x,y))
    visited[y][x] = True
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=N or ny<0 or ny>=N: # out of the area
                continue
            else: # update 
                if graph[ny][nx]==1 and visited[ny][nx]==False: # can move
                    queue.append((nx,ny))
                    visited[ny][nx] = True

def safety_area(graph, h): # return NxN list
    safety_area = []
    for y in graph:
        l = []
        for x in y:
            if x>h:
                l.append(1)
            else:
                l.append(0)
        safety_area.append(l)
    return safety_area


ans = []
for h in range(m):
    s_area = safety_area(area, h)
    # print(s_area)
    visited = [[False]*N for _ in range(N)]
    cnt = 0
    for y in range(N):
        for x in range(N):
            if s_area[y][x] == 1 and visited[y][x] == False:
                count_safety_area(s_area, x, y)
                cnt+=1
    ans.append(cnt)
    
print(max(ans))