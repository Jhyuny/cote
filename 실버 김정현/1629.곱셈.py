"""
https://www.acmicpc.net/problem/1629
"""

import sys

input = sys.stdin.readline

A, B, C = list(map(int, input().split()))
l = []
num = A % B
for i in range(B):
    num *= A
    remain = num % C
    if remain in l:
        break
    else:
        l.append(remain)

print(l[B % len(l)])
