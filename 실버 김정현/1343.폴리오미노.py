"""
https://www.acmicpc.net/problem/1343
"""
N = input()
ans = ''
cnt = 0
for i in list(N):
    if i == '.':
        if cnt == 2:
            ans += 'BB'
            cnt -= 2
        elif cnt == 1 or cnt == 3:
            break
        ans += '.'
    else:
        cnt += 1
    if cnt == 4:
        ans += 'AAAA'
        cnt = 0
if cnt == 2:
    ans += 'BB'
    cnt -= 2
elif cnt == 1 or cnt == 3:
    ans = -1
print(ans)