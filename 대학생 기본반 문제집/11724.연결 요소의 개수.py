"""
https://www.acmicpc.net/problem/11724
"""
from collections import deque
import sys # 시간초과 발생
input = sys.stdin.readline

def bfs(start, edges, visited): # bfs 정의
    q = deque([start])
    visited[start] = True
    while q: # q가 존재하지 않으면 탐색이 완료된 것으로 반복문 종료
        now = q.popleft()
        for e in edges[now]: # e와 연결된 node는 모두 탐색
            if not visited[e]:
                q.append(e) # 방문하지 않았던 곳이면 해당 node와 연결된 다른 node도 순회하기 위해 q에 append
                visited[e] = True

N,M = map(int, input().split())
edges = [[] for _ in range(N + 1)] # n+1개의 빈 list 정의 (node번호와 idx를 같게하기위해 N+1까지 반복)
for _ in range(M): # node와 연결된 node를 정리한 list
    node1, node2 = map(int, input().split())
    edges[node1].append(node2) 
    edges[node2].append(node1)
    # node1와 node2는 서로 연결되어 있음을 의미

result = 0
visited = [False] * (N + 1) # 방문 여부를 확인하는 list 생성
for i in range(1, N + 1):
    if not visited[i]: # 서로 연결되지 않은 node의 수를 찾는다.
        result += 1 # 연결되지 않았을 때 1씩 추가
        bfs(i, edges, visited)
print(result)