"""
https://www.acmicpc.net/problem/10819
"""
from itertools import permutations
N=int(input())
array=list(map(int,input().split()))
def f(l,N):
    y=0
    for i in range(N-1):
        y += abs(l[i]-l[i+1])
    return y
ans=0
for l in permutations(array):
    ans=max(ans,f(list(l),N))
print(ans)