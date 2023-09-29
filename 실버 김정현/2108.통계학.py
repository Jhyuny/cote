"""
https://www.acmicpc.net/problem/2108
"""
from collections import Counter
N=int(input())
nums=[int(input()) for _ in range(N)]
nums=sorted(nums)
# 산술평균
print(round(sum(nums)/len(nums)))
# 중앙값
print(nums[(len(nums)-1)//2])
# 최빈값
counter = dict(Counter(nums))
max_count = max(counter.values())
mode = [num for num, count in counter.items() if count == max_count]
mode.sort()
if len(mode) > 1:
    print(mode[1])
else:
    print(mode[0])
# 범위
print(max(nums)-min(nums))