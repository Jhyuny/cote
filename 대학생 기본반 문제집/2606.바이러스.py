"""
https://www.acmicpc.net/problem/2606
"""
from collections import deque
import sys
input = sys.stdin.readline
N = int(input()) # 컴퓨터 수 (= node 수)
M = int(input()) # 간선 수
link = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
# print(visited)
q = deque()
for i in range(M):
    u,v = map(int,input().split())
    link[u].append(v)
    link[v].append(u)

visited[1] == True
q.append(1)
while q:
    idx = q.popleft()
    for i in link[idx]:
        if visited[i]:
            continue
        else:
            visited[i] = True
            q.append(i)
print(visited.count(True)-1)