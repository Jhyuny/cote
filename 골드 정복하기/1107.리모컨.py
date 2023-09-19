"""
https://www.acmicpc.net/problem/1107
"""
# test_case 7번 해결
channel = 100
N = input()
M = int(input())
if M != 0:
    broken = set(map(int, input().split()))
else:
    broken = set([])
nums = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
buttons = list(nums - broken)
ans = []

for num in N:
    if int(num) in buttons:
        ans.append(0)
    else:
        ans.append(min(map(lambda x: abs(x - int(num)), buttons)))

answer = 0
for idx, i in enumerate(ans):
    answer += i * 10 ** (len(ans) - idx - 1)
print(min(answer + len(N), abs(int(N) - channel)))
