"""
https://www.acmicpc.net/problem/1929
"""
import sys
input=sys.stdin.readline
M,N=map(int,input().split())
# 시간초과 발생, cnt>1 순간 이미 소수가 아니므로 탐색 중지
def check(n):
    cnt=0
    for i in range(1,int(n**(1/2))+1):
        if n%i==0:
            cnt+=1
            if cnt>1:
                return False
    return True
    
for i in range(M,N+1):
    if i==1: # 1은 소수가 아니므로 제외
        continue
    if check(i):
        print(i)