"""
https://www.acmicpc.net/problem/1700
"""

import sys

input = sys.stdin.readline
N, K = map(int, input().split())
products = list(map(int, input().split()))
multi = [0] * N
ans = 0
change = maximum = 0

while products:
    product = products[0]
    if product in multi:
        products.remove(product)
        continue
    elif 0 in multi:
        multi[multi.index(0)] = product
        products.remove(product)
    else:
        for tool in multi:
            if tool not in products:
                change = tool
                break
            elif products.index(tool) > maximum:
                maximum = products.index(tool)
                change = tool
        multi[multi.index(change)] = product
        products.remove(product)
        maximum = 0
        ans += 1
print(ans)