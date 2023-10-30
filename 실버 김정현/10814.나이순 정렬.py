"""
https://www.acmicpc.net/problem/10814
"""
N=int(input())
users=[input().split() for _ in range(N)]
users=sorted(users,key=lambda x: int(x[0]))

for i in users:
    print(i[0],i[1])        