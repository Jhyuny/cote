"""
https://www.acmicpc.net/problem/5430
"""
# https://ideone.com/5zZesN - 반례 납득 안됨...
import sys
input=sys.stdin.readline

T=int(input().strip())
def rvs(l):
    reverse_l=[]
    for i in l[::-1]:
        reverse_l.append(int(i))
    return reverse_l

def dlt(l):
    return l[1:]

ans=[]
for _ in range(T):
    p=input().strip()
    n=int(input())
    nums=list(map(int,input()[1:-2].split(',')))

    for i in p:
        if i=='R':
            nums=rvs(nums)
        if i=='D':
            nums=dlt(nums)
    if len(nums)==0:
        ans.append('error')
    else:
        ans.append(nums)
for i in ans:
    print(i)