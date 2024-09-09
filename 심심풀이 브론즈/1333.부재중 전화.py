"""
https://www.acmicpc.net/problem/1333
"""

N, L, D = map(int,input().split())

total = (N*L) + (5*(N-1))
dp = [False]*(total+1)

# set dp
for i in range(1,N+1):
    now = i*L + 5*(i-1)
    for j in range(now, now+5):
        if j>=len(dp):
            break
        dp[j] = True

ans = False
for i in range(D, total, D):
    if dp[i]:
        ans = True
        print(i)
        break

if ans == False:
    print(((total//D)+1)*D)