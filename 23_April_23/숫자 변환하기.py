# from collections import deque
# def solution(x, y, n):
#     dis = [0 for _ in range(y+1)]
#     Q = deque()
#     Q.append(x)
#     if x == y:
#         return 0
#     while Q: #Q가 존재한다면
#         nx = Q.popleft()
#         for dir in range(3):
#             if dir == 0:
#                 cur_x = nx * 2
#             if dir == 1:
#                 cur_x = nx * 3
#             if dir == 2:
#                 cur_x = nx + n
#             if cur_x > y or dis[cur_x]:
#                 continue
#             if cur_x == y:
#                 return dis[nx] + 1
#             Q.append(cur_x)
#             dis[cur_x] = dis[nx] + 1
    
#     return -1
from collections import deque
def solution(x, y, n):
    ans = [0 for i in range(y+1)]
    Q = deque()
    Q.append(x)
    if x == y:
        return 0
    while Q:
        now_x = Q.popleft() 
        for i in range(3):
            if i == 0:
                new_x = now_x*2
            if i == 1:
                new_x = now_x*3
            if i == 2:
                new_x = now_x + n
            if new_x > y or ans[new_x]: #현재 x의 값이 y보다 크거나, 
                continue
            if new_x == y:
                return ans[now_x] + 1
            Q.append(new_x)
            ans[new_x] = ans[now_x] + 1       
    return -1

solution(10,40,5)