"""
https://www.acmicpc.net/problem/1920
"""
import sys

input = sys.stdin.readline
N = int(input())
nums = set(map(int, input().split()))
M = input()
check = map(int, input().split())
for i in check:
    print(1) if i in nums else print(0)
