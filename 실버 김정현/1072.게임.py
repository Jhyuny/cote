"""
https://www.acmicpc.net/problem/1072
"""
X, Y = map(int,input().split())
Z = int((Y/X)*100)
# X의 주어진 범위가 1000000000이므로 O(N)으론 시간초과 -> 이분탐색을 이용해서 푼다
# x, y, z = X, Y, Z
# ans = 0
# if Z == 100 or Z == 99:
#         ans = -1
# else:
#     while z==Z:
#         ans += 1
#         y += X
#         x += X

#         z = int((y/x)*100)
# print(ans)