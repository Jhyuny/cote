"""
https://www.acmicpc.net/problem/1247
"""
import sys

input = sys.stdin.readline  # sys.stdin.readline 사용 안해서 시간초과
for _ in range(3):
    N = int(input())
    S = 0
    for _ in range(N):
        S += int(input())
    if S == 0:
        print("0")
    elif S > 0:
        print("+")
    else:
        print("-")
