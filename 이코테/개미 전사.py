# 두 개의 경우로 나눠서 풀기
N = int(input())
l = list(map(int,input().split()))
# ai : i번째 식량창고까지의 최적의 해
DP = [0]*N

for i in range(N):
    if i == 0:
        DP[i] = l[i]
    elif i == 1:
        DP[i] = max(l[i-1],l[i])
    else:
        DP[i] = max(l[i-2]+l[i],l[i-1])
print(DP[N-1])
    