"""
https://www.acmicpc.net/problem/2751
"""
import sys
input = sys.stdin.readline
N = int(input())
l = []
for _ in range(N):
    num = int(input())
    l.append(num)
for i in sorted(l):
    print(i)