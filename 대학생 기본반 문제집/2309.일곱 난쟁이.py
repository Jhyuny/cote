"""
https://www.acmicpc.net/problem/2309
"""
import itertools
heights = [input() for _ in range(9)]
for i in itertools.combinations(heights,7):
    i = list(map(int,i))
    i.sort()
    if sum(list(i)) == 100:
        for j in i:
            print(j)
        break