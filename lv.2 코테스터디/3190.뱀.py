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
    nx,ny = head
    for _ in range(int(t)): # t초 동안 움직인다.
        nx += dydx[dir_idx][0]
        ny += dydx[dir_idx][1]
        print('현재 head :', head)
        print('이전 for문 끝난 body :',body)
        if [nx,ny] in body: #몸에 닿는 경우
            print('body!')
            break
        body.append([nx,ny])
        print('현재 head append body :',body)
        if nx>=N or nx<0 or ny<0 or ny>=N: #벽에 닿는 경우
            print('wall!')
            break
        if graph[nx][ny] == 0: # 꼬리도 전진
           tail[0] += dydx[dir_idx][0]
           tail[1] += dydx[dir_idx][1]
           body.popleft()
        print('현재:',body)
        if graph[nx][ny] == 1: # 꼬리는 가만히
            pass
        answer+=1
        head = [nx,ny]
    if dir == 'L': # 이동 끝나면 방향 틀기
        dir_idx += 1
        if dir_idx >= 4:
            dir_idx = dir_idx-4
    else:
        dir_idx -= 1
        if dir_idx < 0:
            dir_idx = dir_idx+4
    print('end',answer)