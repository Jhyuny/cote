"""
https://www.acmicpc.net/problem/1032
"""
N = int(input())
A = input()
ans = A
for _ in range(N-1):
    B = input()
    new = ''
    for a,b in zip(ans,B):
        if a == b:
            new += a
        else:
            new += '?'
    ans = new
print(ans)
