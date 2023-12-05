"""
https://www.acmicpc.net/problem/11053
"""
N = int(input())
l = list(map(int,input().split()))
dp = [1]*N
for i in range(1,N):
    compe=[]
    for j in range(i):
        if l[i]>l[j]: # True라면
            dp[i]=max(dp[i],dp[j]+1)
print(max(dp))