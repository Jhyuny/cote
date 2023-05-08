"""
https://www.acmicpc.net/problem/3190
"""
from collections import deque
tail = [0,0]
head = [0,0]
body = deque()
dydx = [[0,1],[-1,0],[0,-1],[1,0]] # 오, 위, 좌, 하
dir_idx = 0 # L이면 idx +1, D면 -1 (4이상이면 -4, 음수면 +4) 
N = int(input())
graph = [[0]*N for _ in range(N)]

K = int(input())
for _ in range(K):
    a,b = map(int,input().split())
    graph[a-1][b-1] = 1

body.append([0,0])
print(body)
print(graph)
answer = 0
L = int(input())
for _ in range(L):
    t,dir = input().split()
    for _ in range(int(t)): # t초 동안 움직인다.
        head[0] += dydx[dir_idx][0]
        head[1] += dydx[dir_idx][1]
        print('head :', head)
        print('body :',body)
        if head in list(body)[0:-1]: #몸에 닿는 경우
            print('body!')
            break
        body.append(head)
        print('body :',body)
        if head[0] >= N or head[0]<0 or head[1]<0 or head[1] >= N: #벽에 닿는 경우
            print('wall!')
            break
        if graph[head[0]][head[1]] == 0: # 꼬리도 전진
           tail[0] += dydx[dir_idx][0]
           tail[1] += dydx[dir_idx][1]
           body.popleft()
        print(body)
        if graph[head[0]][head[1]] == 1: # 꼬리는 가만히
            pass
        answer+=1
    if dir == 'L': # 이동 끝나면 방향 틀기
        dir_idx += 1
        if dir_idx >= 4:
            dir_idx = dir_idx-4
    else:
        dir_idx -= 1
        if dir_idx < 0:
            dir_idx = dir_idx+4
print('end',answer)