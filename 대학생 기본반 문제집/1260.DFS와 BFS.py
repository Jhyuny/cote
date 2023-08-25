"""
https://www.acmicpc.net/problem/1260
"""
from collections import deque
N,M,V=map(int,input().split())
graph=[[] for _ in range(N+1)]

for _ in range(M):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

def dfs(s):
    visited[s]=True
    print(s,end=" ")
    for i in graph[s]:
        if not visited[i]:
            dfs(i)

def bfs(s):
    queue=deque([s])
    visited[s]=True
    while queue:
        v=queue.popleft()
        print(v,end=" ")
        for i in graph[v]:
            if not visited[i]:
                visited[i]=True
                queue.append(i)

# dfs
visited = [False] * (N + 1)
dfs(V)

print()

# bfs
visited = [False] * (N + 1)
bfs(V)
