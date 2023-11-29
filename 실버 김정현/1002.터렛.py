"""
https://www.acmicpc.net/problem/1002
"""
T = int(input())
for _ in range(T):
    x1,y1,r1,x2,y2,r2 = list(map(int,input().split()))
    d = ((x1-x2)**2 + (y1-y2)**2)**(1/2)
    if d == 0: # 중점이 같을 때
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        if  d > r1+r2 or d < abs(r1-r2): # 두 원이 만나지 않음
            print(0)
        elif d == r1+r2 or d==abs(r1-r2): # 두 원이 접함
            print(1)
        else: # 두 원이 두 점에서 만남
            print(2)