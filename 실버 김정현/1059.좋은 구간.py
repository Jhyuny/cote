"""
https://www.acmicpc.net/problem/1059
"""
from itertools import combinations
N = int(input())
S = sorted(map(int,input().split()))

k = int(input())
min = 0
max = 0
ans = 0
if k in S:
    ans = -1
else:
    for i in S:
        if i < k: # i 가 k보다 작다면
            min = i
        elif i > k and max == 0:
            max = i 
min = min+1
max = max-1
if ans == -1:
    print(0)
else:
    print((k-min)*(max-k+1) + (max-k))