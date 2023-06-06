"""
https://www.acmicpc.net/problem/1247
"""
l = []
for _ in range(3):
    N = int(input())
    S = 0
    for _ in range(N):
        S += int(input())
    if S == 0:
        l.append("0")
    elif S > 0:
        l.append("+")
    else:
        l.append("-")
for i in l:
    print(i)
