"""
https://www.acmicpc.net/problem/1094
"""
X = int(input())
sticks = []
sticks.append(64)
while sum(sticks) != X:
    if sum(sticks)>X:
        # 절반 버리기
        a = sticks.pop()
        b = a/2
        sticks.append(b)
        if sum(sticks)<X:
            sticks.append(b)
print(len(sticks))
