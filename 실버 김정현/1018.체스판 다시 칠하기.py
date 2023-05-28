"""
https://www.acmicpc.net/problem/1018
"""
N, M = map(int,input().split())
board = [input() for _ in range(N)]
answer = []

for i in range(N-7): # moving window in horizontal dir
    for j in range(M-7): # moving window in vertical dir
        ans1 = 0 # chess[0][0] == 'B'일 때
        ans2 = 0 # chess[0][0] == 'W'일 때
        for a in range(i,i+8):
            for b in range(j,j+8):
                if (a+b)%2 == 0:
                    if board[a][b] != 'B':
                        ans1 += 1
                    if board[a][b] != 'W':
                        ans2 += 1
                else:
                    if board[a][b] != 'W':
                        ans1 += 1
                    if board[a][b] != 'B':
                        ans2 += 1
        answer.append(min(ans1,ans2))

print(min(answer))
                       
