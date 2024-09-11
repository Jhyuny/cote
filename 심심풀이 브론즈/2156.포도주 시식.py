"""
https://www.acmicpc.net/problem/2156
"""
N = int(input())
l = [int(input()) for _ in range(N)]
dp = [0]*len(l)

if N>2:
    dp[0] = l[0]
    dp[1] = l[0] + l[1]
    dp[2]=max(l[2] + l[0], l[2] + l[1], dp[1])

    for i in range(3,N):
        dp[i]=max(l[i]+dp[i-2], l[i]+l[i-1]+dp[i-3], dp[i-1])

    print(dp[-1])
elif N==1:
    print(l[0])
else:
    print(l[0]+l[1])