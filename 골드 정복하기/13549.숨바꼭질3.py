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
# visited[something] == -1을 갱신 조건으로 설정하면 간선 간 가중치가 다르기때문에 오차가 생길 수 있다.
# 위의 문제에서 pos에 대한 연산 순서에 따라 정답과 오답이 갈린다
# 따라서 갱신 조건을 '역대 최단거리보다 가까우면'으로 설정해야한다
