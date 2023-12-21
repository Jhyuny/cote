"""
https://www.acmicpc.net/problem/11650
"""
N = int(input())
points = [list(map(int,input().split())) for _ in range(N)]
sorted_points = sorted(points, key=lambda x:[x[0],x[1]])

for i in sorted_points:
    print(i[0],i[1])