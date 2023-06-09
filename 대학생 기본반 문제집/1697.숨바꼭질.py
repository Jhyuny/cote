"""
https://www.acmicpc.net/problem/1697
"""
from collections import deque

N, K = map(int,input().split())
queue = deque()
queue.append((N, 0))
visited = [False] * 100001
result = 0

while queue:
    num, count = queue.popleft()
    if num == K:
        print(count)
        break

    if 0 <= 2 * num <= 100000 and visited[2 * num] == False:
        queue.append((2 * num, count + 1))
        visited[2 * num] = True
    if 0 <= num + 1 <= 100000 and visited[num + 1] == False:
        queue.append((num + 1, count + 1))
        visited[num+1] = True
    if 0 <= num - 1 <= 100000 and visited[num-1] == False:
        queue.append((num - 1, count + 1))
        visited[num-1] = True