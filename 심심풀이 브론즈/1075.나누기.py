"""
https://www.acmicpc.net/problem/1075
"""
N = int(input())
K = int(input())
min_N = (N//100)*100
if min_N%K == 0:
    print(str(min_N)[-2:])
else:
    n = min_N//K
    print(str(K*(n+1))[-2:])