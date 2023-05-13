"""
https://www.acmicpc.net/problem/3649
"""
import sys

input = sys.stdin.readline
# combination 활용 -> 시간초과
# two pointer 사용

while True:
    try:
        hole = (int(input()))*10**7
        n = int(input())
        pieces = sorted([int(input()) for _ in range(n)])
        answers = {}
        left, right = 0, n-1
        while left < right:
            if pieces[left] + pieces[right] < hole:
                left += 1
            elif pieces[left] + pieces[right] > hole:
                right -= 1
            else:
                answers[pieces[right]-pieces[left]] = [pieces[left], pieces[right]]
                break
        if answers:
            print('yes', answers[max(answers.keys())][0], answers[max(answers.keys())][1])
        else:
            print('danger')
    except: # 입력 값이 없는 경우 예외처리하는 방법
        break