"""
https://www.acmicpc.net/problem/13549
"""
from collections import deque

N,K=map(int,input().split())
visited=[-1]*100001
visited[N]=0
q=deque()
q.append(N)

while q:
    pos=q.popleft()
    if pos==K:
        print(visited[pos])
        break
    if 0 <= pos-1 < 100001 and visited[pos-1] == -1:
        visited[pos-1] = visited[pos] + 1
        q.append(pos-1)
    if 0 < pos*2 < 100001 and visited[pos*2] == -1:
        visited[pos*2] = visited[pos] # 이동횟수 추가x
        q.appendleft(pos*2) # +1,-1보다 더 많은 움직임을 행하므로 최단시간을 구하려면
    if 0 <= pos+1 < 100001 and visited[pos+1] == -1:
        visited[pos+1] = visited[pos] + 1
        q.append(pos+1)
# 문제에서 주어진 조건 범위를 다 잡아서 푸는 것이 중요한 것 같다.
