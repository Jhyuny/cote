"""
https://swexpertacademy.com/main/solvingProblem/solvingProblem.do
"""
from collections import Counter
T=int(input())
for _ in range(T):
    N=input()
    l=input().split()
    count_l=dict(Counter(l))
    # sorting dict in values()
    ans=dict(sorted(count_l.items(),reverse=True,key=lambda x: x[1]))
    print(f'#{N} {list(ans.keys())[0]}')