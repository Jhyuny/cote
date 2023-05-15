"""
https://www.acmicpc.net/problem/14501
"""
N = int(input())
L = [list(map(int,input().split())) for _ in range(N)]
dp = [0]*N

for i in range(N):
    if i + L[i][0] <= N:
        dp[i] = L[i][1]
        for j in range(i):
            if j + L[j][0] <= i:
                dp[i] = max(dp[i], dp[j]+L[i][1])

print(max(dp))

