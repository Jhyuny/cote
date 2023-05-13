"""
https://www.acmicpc.net/problem/16235
"""
# (r,x)는 graph의 좌표를 직접적으로 의미
# 양분은 모든 칸에 5씩
# 봄 : 어린 나무부터 해당 칸의 양분 먹기, 나이만큼 못 먹으면 죽음, 그 후에 나이 +1
# 여름 : 죽은 나무 -> 양분, 나이//2만큼 추가
# 가을 : 나이 5이상 나무 번식, 주변 칸에 나무 추가, 벗어나면 X
# 겨울 : 양분 추가 
# K년이 지난 후 살아있는 나무 개수
# 각 칸에 대해 존재하는 나무의 나이를 list에 추가
# 5이상이 아닌 5의 배수에서 번식
# 천년테케 통과 못함.. -> 통과
# 시간초과 해결 
# ->1. 반복문 중복 최대한 감소, 2. deque()사용, 3.input = sys.stdin.readline사용, 4. pypy3로 제출

import sys
from collections import deque
input = sys.stdin.readline
N,M,K = map(int,input().split())
nutr = [[5]*N for _ in range(N)]
add_nutr = [list(map(int,input().rstrip().split())) for _ in range(N)]
graph = [[deque() for _ in range(N)] for _ in range(N)] # 그냥 한 행에 대해서 곱해주면 모든 행이 같아지므로 for문을 이용해서 독립적으로 생성해줘야함

for _ in range(M):
    x,y,age = map(int,input().rstrip().split())
    graph[x-1][y-1].append(age)

def year(graph,nutr):
    dx = [0,0,1,1,1,-1,-1,-1]
    dy = [1,-1,0,1,-1,0,1,-1]
    # spring, summer
    for i in range(N):
        for j in range(N):
            be_nutr = 0
            alive = deque()
            for age in graph[i][j]: # 양분 먹기
                if nutr[i][j]>=age:
                    nutr[i][j] = nutr[i][j] - age
                    alive.append(age+1) # 양분 먹은 나무는 나이+1
                else: # 양분 없어서 죽음
                    be_nutr += age//2
            nutr[i][j] += be_nutr # 죽은 나무 양분화
            graph[i][j] = alive # 나이 먹음
    # fall
    for i in range(N):
        for j in range(N):
            if graph[i][j]:
                for tree in graph[i][j]:
                    if tree%5==0: # 5이상이 아니라 5의 배수...;;
                        for k in range(8):
                            nx = i+dx[k]
                            ny = j+dy[k]
                            if 0<=nx<N and 0<=ny<N:
                                graph[nx][ny].appendleft(1)
            # winter
            nutr[i][j] += add_nutr[i][j]
    return graph, nutr

for _ in range(K):
    graph,nutr = year(graph,nutr)

answer = 0
for i in range(N):
    for j in range(N):
        answer += len(graph[i][j])
print(answer)
