"""
https://www.acmicpc.net/problem/1987
"""
R,C=map(int,input().split())
board=[list(input().rstrip()) for _ in range(R)]
visited = [False]*26 # 알파벳 수 26
# 상하좌우
dx=[-1,1,0,0]
dy=[0,0,-1,1]

max_distance=0

def dfs(x,y,distance):
    global max_distance
    max_distance=max(max_distance, distance)
    visited[ord(board[x][y])-ord('A')]=True
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        # 이동할 수 있는 경우라면
        if 0<=nx<R and 0<=ny<C and not visited[ord(board[nx][ny])-ord('A')]:
            dfs(nx,ny,distance+1) # 그 위치에서 다시 dfs탐색 시작

    visited[ord(board[x][y]) - ord('A')] = False # 이동할 수 없다면 해당 위치 방문 취소

dfs(0,0,1)
print(max_distance)