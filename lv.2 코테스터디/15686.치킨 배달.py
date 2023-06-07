"""
https://www.acmicpc.net/problem/15686
"""
from itertools import combinations
N,M = list(map(int,input().split()))
city = [list(map(int, input().split())) for _ in range(N)]
chicken = []
home = []
ans = 1000000000000
for i in range(N):
    for j in range(N):
        if city[i][j] == 2:
            chicken.append([i,j])
        elif city[i][j] == 1:
            home.append([i,j])
for group in combinations(chicken,M):
    city_dir = 0
    for h in home:
        dir = 1000000000000
        for i in range(M):
            dir = min(dir,abs(h[0]-group[i][0]) + abs(h[1]-group[i][1]))
        city_dir += dir
    ans = min(ans,city_dir)
print(ans)
    