N,M = map(int,input().split())
coins = [int(input()) for _ in range(N)]

dp = [10001]*(M+1) # M+1개 설정, min이므로 최댓값 설정

dp[0]=0
for i in range(N):
    for j in range(coins[i], M+1):
        if dp[j-coins[i]] != 10001:
            dp[j] = min(dp[j],dp[j-coins[i]]+1) # 현재 지정된 dp랑 새로운 값이랑 비교

if dp[M] == 100001:
    print(-1)
else:
    print(dp[M])