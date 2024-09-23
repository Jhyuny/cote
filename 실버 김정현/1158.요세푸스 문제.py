"""
https://www.acmicpc.net/problem/1158
"""
N, K = map(int,input().split())

nums = [str(i) for i in range(1,N+1)]
ans = []
a = 0
for i in range(N):
    a += (K-1)
    if a>=len(nums):
        a=a%len(nums)
    ans.append(nums[a])
    nums.pop(a)

print(f"<{', '.join(ans)}>")
