from collections import deque
xhqsl = {}
for num, _ in enumerate(range(4),1):
    xhqsl[num] = list(input())
N = int(input())

def rotate_xhqsl(dir,l):
    l = deque(l)
    if dir == 1: # clockwise
        a = l.popleft()
        l.append(a)
    else: # counter-clockwise
        a = l.pop()
        l.appendleft(a)
    return l

for _ in range(N):
    num, dir = list(map(int,input().split()))
    if dir == 1:
        r_dir = -1
    else:
        r_dir = 1
    if num == 1: # 톱니 1번
        if xhqsl[1][7] != xhqsl[2][3]: # 회전할 조건
            xhqsl[2] = rotate_xhqsl(r_dir,xhqsl[2]) # 반대 방향으로 회전
        xhqsl[1] = rotate_xhqsl(dir,xhqsl[1])
    if num == 2: # 톱니 2번
        if xhqsl[1][7] != xhqsl[2][3]: # 1번 고려
            xhqsl[1] = rotate_xhqsl(r_dir,xhqsl[1])
        if xhqsl[2][7] != xhqsl[3][3]: # 3번 고려
            xhqsl[3] = rotate_xhqsl(r_dir,xhqsl[3])
        xhqsl[2] = rotate_xhqsl(dir,xhqsl[2])
    if num == 3: # 톱니 3번
        if xhqsl[2][7] != xhqsl[3][3]: # 2번 고려
            xhqsl[2] = rotate_xhqsl(r_dir,xhqsl[2])
        if xhqsl[3][7] != xhqsl[4][3]: # 4번 고려
            xhqsl[4] = rotate_xhqsl(r_dir,xhqsl[4])
        xhqsl[3] = rotate_xhqsl(dir,xhqsl[3])
    else: # 톱니 4번
        if xhqsl[3][7] != xhqsl[4][3]: # 회전할 조건
            xhqsl[3] = rotate_xhqsl(r_dir,xhqsl[3]) # 반대 방향으로 회전
        xhqsl[4] = rotate_xhqsl(dir,xhqsl[4])

answer = 0
for num,l in enumerate(xhqsl.values()):
    print(l)
    if l[0] == '1':
        print(l[0])
        answer += 2**num

print(answer)
