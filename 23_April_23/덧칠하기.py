#시간초과
# from collections import deque
# def solution(n, m, section):
#     section = deque(section)
#     cnt = 0
#     while True:
#         if section[0] + m > n + 1:
#             last = n + 1
#         else:
#             last = section[0] + m
#         for i in range(section[0],last):
#             if i in section:
#                 section.popleft()
#         cnt += 1
#         if len(section) == 0:
#             return cnt

def solution(n, m, section):
    answer = 1
    paint = section[0] + m - 1
    for i in section[:]:
        if i <= paint:
            section.remove(i)
        else:
            answer += 1
            paint = section[0] + m -1
            section.remove(i)
    return answer
            


        
