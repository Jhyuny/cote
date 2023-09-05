"""
https://www.acmicpc.net/problem/1920
"""
import sys

input = sys.stdin.readline
N = int(input())
nums = sorted(map(int, input().split()))
M = input()
check = map(int, input().split())
for i in check:
    l, r = 0, N - 1  # 이분탐색 초기 설정값
    find = False

    # 이분탐색 시작
    while l <= r:  # l이 r과 커지면 정지
        mid = (l + r) // 2
        if i == nums[mid]:
            find = True
            print(1)
            break
        elif i > nums[mid]:
            l = mid + 1
        else:
            r = mid - 1
    if not find:
        print(0)
