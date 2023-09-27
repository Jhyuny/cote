"""
https://www.acmicpc.net/problem/1717
"""
n,m = map(int,input().split())
l=[i for i in range(n+1)]

def find(x):
    if l[x] != x:
        l[x] = find(l[x]) # l[x]==x일 때가지 타고 올라감
    return l[x]

def union(x,y):
    x=find(x)
    y=find(y)
    if x<y:
        l[y]=x
    else:
        l[x]=y

for _ in range(m):
    op,a,b=map(int,input().split())
    if op==0:
        union(a,b)
    else:
        if find(a)==find(b):
            print('YES')
        else:
            print('NO')