"""
https://www.acmicpc.net/problem/14890
"""


def check(l, L):
    l = list(map(int, l))
    ret = 0
    cnt = 1
    before = l[0]
    for i in l[1:]:
        # print("before:", before)
        # print("i:", i)
        # print("cnt:", cnt)
        if i == before:
            cnt += 1
        else:
            if i == before + 1 and cnt >= L:  # 경사로 놓고 한 칸 올라가기
                before = i
                cnt = 1  # cnt 초기화
            # 경사로 두고 내려가는 경우도 구현할 것
            else:
                return False
    return True


N, L = map(int, input().split())
graph = [input().split() for _ in range(N)]
ans = 0
# horizontal road check
for l in graph:
    if check(l, L) or check(l[::-1], L):
        ans += 1
        print("add!")
# vertical road check
for i in range(N):
    l = []
    for j in range(N):
        l.append(graph[j][i])
    if check(l, L) or check(l[::-1], L):
        ans += 1
        print("add!")
print(ans)

# check([1, 1, 1, 2, 2, 3], 2)
