"""
https://www.acmicpc.net/problem/1011
"""
from collections import deque
T=int(input())
for _ in range(T):
    x,y = map(int,input().split())
    point=0
    dx=[-1,0,1]
    cnt=[-1]*(y+1)
    q=deque()
    q.append(0)
    while q:
        pos=q.popleft()
        if pos==y: # arrive
            print(cnt[y])
            break
        
        for i in range(3):
            if 0<=pos+dx[i]<=y and cnt[pos+dx[i]]==-1:
                npoint=pos+dx[i]
                cnt[npoint]=cnt[pos]+1
                q.append(npoint) # x update
