"""
문제 바로가기 https://www.acmicpc.net/problem/2621
"""
from collections import Counter

def check_continuous(l):
    sorted(l)
    a = int(l[0])
    for i in l[1:]:
        if a+1 == i:
            a = i
            continue
        else:
            return 0
    return 1

colors = []
nums = []
result = []
for _ in range(5):
    N = input()
    color,num = N.split()
    colors.append(color)
    nums.append(int(num))
count_colors = Counter(colors)
count_nums = Counter(nums)
n_colors = len(count_colors)
n_nums = len(count_nums)
#1 카드 5장이 모두 같은 색이면서 숫자가 연속적일 때
if len(count_colors) == 1 and check_continuous(nums) == 1:
    result.append(900 + sum(nums))
#2 카드 5장 중 4장의 숫자가 같을 때
if 4 in count_nums.values():
    for key, value in count_nums.items():
        if value == 4:
            result.append(800 + int(key))
            break
#3 카드 5장 중 3장의 숫자가 같고 나머지 2장도 숫자가 같을 때
if 3 in count_nums.values() and 2 in count_nums.values():
    for key, value in count_nums.items():
        if value == 3:
            a = 10 * int(key)
        if value == 2:
            b = int(key)
    result.append(700 + a + b)
#4 5장의 카드 색깔이 모두 같을 때
if len(count_colors) == 1:
    result.append(600 + max(nums))
#5 카드 5장의 숫자가 연속적일 때
if check_continuous(nums) == 1:
    result.append(500 + max(nums))
#6 카드 5장 중 3장의 숫자가 같을 때
if 3 in count_nums.values():
    for key, value in count_nums.items():
        if value == 3:
            result.append(400+int(key))
#7 카드 5장 중 2장의 숫자가 같고 또 다른 2장의 숫자가 같을 때 
if 2 in count_nums.values() and len(count_nums) == 3 and 1 in count_nums.values():
    l = []
    for key, value in count_nums.items():
        if value == 2:
            l.append(int(key))
    result.append(10*max(l)+min(l)+300)
#8 카드 5장 중 2장의 숫자가 같을 때
if 2 in count_nums.values():
    for key, value in count_nums.items():
        if value == 2:
            result.append(200 + int(key))
#9
else:
    result.append(100 + max(nums))
print(max(result))



