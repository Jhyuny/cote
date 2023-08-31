"""
https://www.acmicpc.net/problem/1753
"""
from collections import deque
V,E=map(int,input().split())
s=int(input())
tree=[[0]*(V+1) for _ in range(V+1)]
for _ in range(E):
    u,v,w=map(int,input().split())
    if tree[u][v]!=0 and tree[u][v]<=w:
        pass
    else:
        tree[u][v]=w
def bfs(start,end):
    if start==end: return 0
    visited=[0] * (V+1)
    q=deque([(start,0)])
    while q:
        now,weight=q.popleft()
        for idx,i in enumerate(tree[now][1:], start=1): # i=[정점,가중치] -> 여기서 순서대로 진행하지 않고 가중치가 작은 것부터 탐색 시작
            if idx==end and i!=0:
                return weight+i
            if visited[idx]==0: # 방문한 적 없다면
                q.append([idx,weight+i]) # [방문,현재 가중치]
                visited[idx]=1
            else:
                pass
    return 'INF'

for i in range(1,V+1):
    print(bfs(s,i))