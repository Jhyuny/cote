"""
https://www.acmicpc.net/problem/14888
"""
from collections import deque
from itertools import permutations
N = int(input())
nums = list(map(int,input().split()))
q = deque(nums)
op = list(map(int,input().split()))
ops = []
for i,num in enumerate(op):
    for _ in range(num):
        if i == 0:
            ops.append('+')
        if i == 1:
            ops.append('-')
        if i == 2:
            ops.append('x')
        if i == 3:
            ops.append('/')
a = q.popleft()
answer = []
for idx,p in enumerate(permutations(ops,len(ops))):
    ans = a
    for op,num in zip(p,q):
        if op == '+':
            ans += num
        if op == '-':
            ans -= num
        if op == 'x':
            ans *= num
        if op == '/':
            if num<0 or ans<0:
                ans = abs(ans)//abs(num)
                ans = -ans
            else:
                ans = ans//num
    answer.append(ans)
print(max(answer))
print(min(answer))
