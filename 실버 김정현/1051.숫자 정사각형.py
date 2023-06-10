"""
https://www.acmicpc.net/problem/1051
"""
N,M = map(int,input().split())
K = min(N,M)
ans = 1
graph = [list(map(int,list(input()))) for _ in range(N)]
for i in range(N):
    for j in range(M):
        for k in range(K):
            if i+k<N and j+k<M and graph[i][j]==graph[i+k][j]==graph[i][j+k]==graph[i+k][j+k]:
                ans = max(ans,(k+1)**2)
print(ans)