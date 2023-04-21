from collections import deque

def bfs(now_x,now_y,maps,visited):
    val = [int(maps[now_x][now_y])]
    dxdy = [[-1,0],[1,0],[0,-1],[0,1]]
    now = deque([(now_x,now_y)])
    
    while now:
        now_y,now_x = now.popleft()
        for i in range(4): #상하좌우 검사
            nx = now_x + dxdy[i][0]
            ny = now_y + dxdy[i][1]
            
            if 0 <= nx < len(maps[0]) and 0 <= ny < len(maps) and maps[ny][nx] != 'X' and not visited[ny][nx]: #not visited > visited가 False인 경우
                visited[ny][nx] = True
                val.append(int(maps[ny][nx]))
                now.append((ny,nx))
    return sum(val)
                
def solution(maps):
    answer = []
    h = len(maps)
    w = len(maps[0])
    visited = [[False]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if not visited[i][j] and maps[i][j] != 'X': 
                visited[i][j] = True
                answer.append(bfs(i,j,maps,visited))
            else:
                visited[i][j] = True
    if answer != []:
        return sorted(answer)
    else:
        return [-1]
    
solution(["X591X","X1X5X","X231X", "1XXX1"])