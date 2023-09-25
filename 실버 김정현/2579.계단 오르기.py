"""
https://www.acmicpc.net/problem/2579
"""
N=int(input()) # 300이하의 자연수
stair=[0]*301
for i in range(N):
    stair[i]=int(input())
dp=[0]*301

dp[0]=stair[0]
dp[1]=stair[0]+stair[1]
dp[2]=max(stair[0]+stair[2], stair[1]+stair[2])
for i in range(3,N): # N이 3보다 작으면 for loop pass
    dp[i]=max(dp[i-3]+stair[i-1]+stair[i], dp[i-2]+stair[i])
print(dp[N-1])