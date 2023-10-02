"""
https://www.acmicpc.net/problem/10816
"""
from collections import Counter
N=int(input())
nums=input().split()
count = Counter(nums)
M=int(input())
cnts=input().split()
for i in cnts:
    print(count[i], end=' ')
# Counter는 KeyError대신 0을 반환한다
# Counter에 대해 elements()를 적용할 수 있다
# print(list(count.elements()))
# ['6', '3', '2', '10', '10', '10', '-10', '-10', '7', '3']