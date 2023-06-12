"""
https://www.acmicpc.net/problem/11399
"""
N = int(input())
times = sorted(list(map(int,input().split())))
cnt = N-1
ans = 0
for i in times:
    ans+=cnt*i
    cnt-=1
print(ans+sum(times))
