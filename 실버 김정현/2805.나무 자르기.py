"""
https://www.acmicpc.net/problem/2805
"""
# 1 ≤ N ≤ 1,000,000, 1 ≤ M ≤ 2,000,000,000
# 단순 탐색의 경우 시간 초과가 발생할듯 -> 이분 탐색으로 풀이
tree, needs = list(map(int,input().split()))
trees = list(map(int,input().split()))
l,r = [1,max(trees)]
mid = (r+l)//2
while True:
    length = 0 # 벌목된 나무의 총합
    for tree in trees:
        if tree>mid:
            length+=(tree-mid)
    if length<needs:
        l,r=[l,mid-1]
    else:
        l,r=[mid+1,r]
    if l>r:
        break 
    mid = (r+l)//2
print(r) 