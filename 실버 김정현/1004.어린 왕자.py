"""
https://www.acmicpc.net/problem/1004
"""

def check(x,y,a,b,r):
    d = ((x-a)**2 + (y-b)**2)**(1/2)
    if d<r:
        return True
    else:
        return False

T = int(input())

for _ in range(T):
    cnt = 0
    x1, y1, x2, y2 = map(int,input().split())
    N = int(input())
    for _ in range(N):
        a,b,r = map(int,input().split())
        p1 = check(x1,y1,a,b,r)
        p2 = check(x2,y2,a,b,r)
        if p1==True and p2==True:
            pass
        if p1==False and p2==False:
            pass
        if (p1==True and p2==False) or (p1==False and p2==True):
            cnt+=1
            
    if x1==x2 and y1==y2:
        print(0)
    else:
        print(cnt)
