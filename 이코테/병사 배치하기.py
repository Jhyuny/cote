N = int(input())
power = list(map(int,input().split()))
dp = [0]*N
dp[0]=1
a = power[0]
cnt = 1
ans = 0 # 열외 병사
for i in range(1,N):
    if a<=power[i]:
        dp[i] = 1
        cnt = 1
        ans += 1
    else:
        cnt += 1
        dp[i] = cnt
    a = power[i]
print(dp)
print(ans)
# 8
# 15 11 4 13 8 7 9 8
# ans = 4