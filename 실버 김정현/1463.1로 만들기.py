"""
https://www.acmicpc.net/problem/1463
"""
## BFS
from collections import deque
N = int(input())
q = deque()
visited=[0]*(N+1)
q.append(N)
while q:
    n=q.popleft()
    if n==1:
        break
    if n%3==0 and visited[n//3]==0:
        q.append(n//3)
        visited[n//3]=visited[n]+1
    if n%2==0 and visited[n//2]==0:
        q.append(n//2)
        visited[n//2]=visited[n]+1
    if visited[n-1]==0:
        q.append(n-1)
        visited[n-1]=visited[n]+1
print(visited[1])

## DP-BottomUp
N=int(input())
d=[0]*(N+1)
for i in range(2,N+1):
    d[i]=d[i-1]+1 # d[i]에서 1을 빼면 d[i-1]이기때문
    if i%2==0:
        d[i]=min(d[i],d[i//2]+1) # 2로 나눈 것과 1을 뺀 것중 무엇이 더 작은지
    if i%3==0:
        d[i]=min(d[i],d[i//3]+1)
print(d[N])

