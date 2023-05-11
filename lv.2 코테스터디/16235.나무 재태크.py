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
import sys
input = sys.stdin.readline
N,M,K = map(int,input().split(' '))
nutr = [[5]*N for _ in range(N)]
add_nutr = [list(map(int,input().rstrip().split(' '))) for _ in range(N)]
graph = [[[]]*N for _ in range(N)] # 그냥 한 행에 대해서 곱해주면 모든 행이 같아지므로 for문으로 독립적으로 생성해줘야함
print(graph)
for _ in range(M):
    x,y,age = map(int,input().rstrip().split(' '))
    graph[x][y].append(age)
    graph[x][y].sort()

def year(graph,nutr):
    dx = [0,0,0,1,1,1,-1,-1,-1]
    dy = [0,1,-1,0,1,-1,0,1,-1]
    # spring, summer
    for i in range(N):
        for j in range(N):
            be_nutr = 0
            for age in graph[i][j][::]:
                if nutr[i][j]>=age:
                    nutr[i][j] == nutr[i][j]-age
                else:
                    graph[i][j].remove(age) # 양분 없어서 죽음
                    be_nutr += age//2
            nutr[i][j] += be_nutr # 죽은 나무 양분화
            graph[i][j] = list(map(lambda x: x+1,graph[i][j])) # 나이 먹음
    # fall
    for i in range(N):
        for j in range(N):
            if graph[i][j] and max(graph[i][j]) >= 5:
                x,y = i,j
                for k in range(8):
                    nx = x+dx[k]
                    ny = y+dy[k]
                    if 0<=nx<N and 0<=ny<N:
                        graph[nx][ny].append(1)
                        graph[nx][ny].sort()
    # winter
    new_nutr = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_nutr[i][j] = nutr[i][j] + add_nutr[i][j]
    return graph,new_nutr

for _ in range(K):
    graph,nutr = year(graph,nutr)

answer = 0
for i in range(N):
    for j in range(N):
        answer += len(graph[i][j])
print(answer)