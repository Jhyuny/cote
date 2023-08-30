from collections import deque

N=int(input())
K=int(input())
cmp=[[] for _ in range(N+1)]
for _ in range(K):
    a,b=map(int,input().split())
    cmp[a].append(b)
    cmp[b].append(a)

visited=[[0] for _ in range(N+1)]
infect=deque([1])
visited[1]=1
cnt=0
while infect:
    c_num=infect.popleft()
    for i in cmp[c_num]:
        if visited[i]==1:
            pass
        else:
            infect.append(i)
            visited[i]=1
            cnt+=1

print(cnt)