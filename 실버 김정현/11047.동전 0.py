"""
https://www.acmicpc.net/problem/11047
"""
import sys
input=sys.stdin.readline
N, K = map(int,input().split())
coins=[int(input()) for _ in range(N)]
cnt=0
idx=-1
while K!=0:
    coin=coins[idx]
    if coin>K:
        idx-=1
        continue
    else:
        K-=coin
        cnt+=1
print(cnt)

# pypy3 + sys.stdin.readline을 사용으로 시간초과 해결