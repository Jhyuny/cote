"""
https://www.acmicpc.net/problem/4344
"""
N=int(input())
for _ in range(N):
    std=0
    l = list(map(int,input().split()))
    n=l[0]
    l=l[1:]
    avg = sum(l)/len(l)
    for num in l:
        if num>avg:
            std+=1
    print(round(std/n*100,3),'%')