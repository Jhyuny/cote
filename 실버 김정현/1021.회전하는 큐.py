"""
https://www.acmicpc.net/problem/1021
"""
from collections import deque
L,N = map(int,input().split())
nums = list(map(int,input().split()))
q = deque([i for i in range(1,L+1)])
cnt = 0
for num in nums:
    if num == q[0]:
        q.popleft()
        continue
    if q.index(num)<=len(q)/2:
        while num != q[0]:
            a = q.popleft()
            q.append(a)
            cnt+=1
        q.popleft()
    else:
        while num != q[0]:
            a = q.pop()
            q.appendleft(a)
            cnt+=1
        q.popleft()
print(cnt)