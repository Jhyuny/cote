"""
https://www.acmicpc.net/problem/1037
"""
# 유클리드 호제법을 이용해서 lcm 구현
# 모든 약수를 제시하므로 단순 최소공배수로 구현 불가    
N = int(input())
nums = list(map(int,input().split()))

print(min(nums)*max(nums))
