"""
https://www.acmicpc.net/problem/1654
"""
K,N=map(int,input().split())
nums=[int(input()) for _ in range(K)]
start,end=1,max(nums)
while start <= end:
    mid=(start+end)//2
    sum=0
    for num in nums:
        sum+=num//mid
    if sum>=N:
        start=mid+1
    else:
        end=mid-1
print(end)