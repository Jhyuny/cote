N = int(input())
power = list(map(int,input().split()))

power.reverse()

dp = [1]*N

for i in range(1,N):
    for j in range(0,1):
        if power[j] < power[i]:
            dp[i] = max(dp[i],dp[j]+1)
print(N-max(dp))

# 8
# 15 11 4 13 8 7 9 8
# ans = 4
# print = 6 ???