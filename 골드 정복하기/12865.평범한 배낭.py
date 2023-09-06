"""
https://www.acmicpc.net/problem/12865
"""
import sys
input=sys.stdin.readline
N,K=map(int,input().split()) # K는 최대 무게, N은 물건 개수
weights=[0]*(N+1)
values=[0]*(N+1)

for i in range(1,N+1):
    weights[i], values[i] = map(int,input().split())

dp=[[0]*(K+1) for _ in range(N+1)]

for i in range(1,N+1):
    for w in range(1,K+1):
        if weights[i]>w: # i번째 물건의 무게가 w보다 크면 더 이상 배낭에 넣을 수 없으므로
            dp[i][w]=dp[i-1][w]
        else:
            dp[i][w]=max(dp[i-1][w],dp[i-1][w-weights[i]]+values[i]) # 물건을 배낭에 넣는다
print(dp[N][K]) # N번째 물건까지 고려했을 때 배낭 용량이 K일 때의 최대 가치