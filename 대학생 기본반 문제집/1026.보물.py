"""
https://www.acmicpc.net/problem/1026
"""
N = input()
A = sorted(list(map(int,input().split())),reverse=True)
B = sorted(list(map(int,input().split())))
answer = 0
for a,b in zip(A,B):
    answer += a*b
print(answer)