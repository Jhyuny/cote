"""
https://www.acmicpc.net/problem/1912
"""
N=int(input())
nums = list(map(int,input().split()))

dp = [0]*N
dp[0] = nums[0]

for i in range(1,N):
    # 여기까지 모두 더한 값이랑 현재 값을 비교, 현재까지 더한 값이 더 작으면 앞의 값을 사용할 이유가 없음
    # 현재값부터 dp[i]에 다시 저장
    dp[i] = max(nums[i],dp[i-1] + nums[i])

print(max(dp))