"""
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV134DPqAA8CFAYh
"""
for num in range(10):
    N=int(input())
    buildings=list(map(int,input().split()))
    ans=0
    for i in range(2,len(buildings)-2):
        if buildings[i]>max(buildings[i-2],buildings[i-1],buildings[i+1],buildings[i+2]):
            ans+=buildings[i]-max(buildings[i-2],buildings[i-1],buildings[i+1],buildings[i+2])
    print(f'#{num+1} {ans}')