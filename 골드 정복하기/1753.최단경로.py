"""
https://www.acmicpc.net/problem/1753
"""
import sys
import heapq

input=sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        weight,now=heapq.heappop(q)
        if distance[now]<weight:
            continue
        for i in tree[now]:
            cost=weight+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

V,E=map(int,input().split())
s=int(input())
tree=[[] for _ in range(V+1)]
distance = [INF] * (V+1) #최단 거리 테이블

for _ in range(E):
    u,v,w=map(int,input().split())
    tree[u].append((v,w))

dijkstra(s)

for i in range(1,V+1):
    if distance[i]==INF:
        print("INF")
    else:
        print(distance[i])