"""
문제 바로가기 https://www.acmicpc.net/problem/1652
"""
N = int(input())
room = []
row, col = 0, 0
for i in range(N):
    line = input()
    room.append(line)
    
for line in room:
    cnt = 0
    for i in line:
        if i == '.':
            cnt += 1
        if i == 'X':
            if cnt >= 2:
                row += 1
            cnt = 0
    if cnt >= 2:
        row += 1
for idx in range(N):
    cnt = 0
    for line in room:
        if line[idx] == '.':
            cnt += 1
        if line[idx] == 'X':
            if cnt >= 2:
                col += 1
            cnt = 0
    if cnt >= 2:
        col += 1
print(row, col)

