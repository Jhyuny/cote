"""
https://www.acmicpc.net/problem/1049
"""
N, M = map(int,input().split())
prices = []
for _ in range(M):
    a,b = list(map(int,input().split()))
    if N%6 == 0:
        prices.append(a*(N//6))
    else:
        prices.append(a*(N//6+1))
    prices.append(b*N)

print(min(prices))