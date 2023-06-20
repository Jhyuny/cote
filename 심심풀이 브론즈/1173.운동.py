"""
https://www.acmicpc.net/problem/1173
"""
N, m, M, T, R = map(int,input().split())
ex = 0 # 운동
t = 0 # 시간
now = m
while ex < N:
    if m+T > M:
        break
    if now + T <= M:
        now += T
        ex += 1
    else:
        now = max(now-R, m)
    t += 1
print(t if ex == N else -1)

