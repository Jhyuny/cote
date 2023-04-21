from collections import deque
def bfs(start,goal,maps):
    h = len(maps)
    w = len(maps[0])
    nxny = [[-1,0],[1,0],[0,-1],[0,1]]
    visited = [[-1]*w for _ in range(h)]
    visited[start[0]][start[1]] = 0 # start 0부터 시작
    queue = deque([start]) # queue정의
    print(len(queue))
    while len(queue)>0: # append되지 않으면 break
        print('start')
        x,y = queue.popleft()
        for nx,ny in nxny:
            move = visited[x][y]
            x += nx
            y += ny
            print(x,y,move)
            if x>=w or x<0: # x가 maps을 벗어나는 경우
                continue
            if y>=h or y<0: # y가 maps을 벗어나는 경우
                continue
            if visited[x][y] != -1: # 이미 방문
                continue
            if maps[x][y] == 'X':
                continue
            visited[x][y] == move + 1
            queue.append([x,y])
            print('>>>',queue)
    return visited[goal[0]][goal[1]] # 목표에 도달하지 못하면 -1을 반환함

                
def solution(maps):
    a = 0
    for i in maps: # len(maps)로 하면 a,b 따로 정의하지 않아도 됨
        b = 0
        for j in i:
            if j == 'S':
                S = [a,b]
            if j == 'E':
                E = [a,b]
            if j == 'L':
                L = [a,b]
            b += 1
        a += 1
    # S -> L
    if bfs(S,L,maps)<0:
        return -1
    # L -> E
    if bfs(L,E,maps)<0:
        return -1
    else:
        return bfs(S,L,maps)+bfs(L,E,maps)
    
solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"])