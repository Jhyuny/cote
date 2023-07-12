"""
https://www.acmicpc.net/problem/1213
"""
from collections import deque
N = sorted(list(input()), reverse=True)
seted_N = sorted(list(set(N)), reverse=True)
ans = deque()
cnt1 = 0
cnt2 = 0
m = 0
for i in seted_N:
    if len(N)%2 != 0: # 홀수개의 문자
        if N.count(i)%2 != 0:
            m = i
            cnt1 += 1
    else:
        if N.count(i)%2 != 0:
            cnt2 += 1
            break
if len(N)%2 != 0 and cnt1 != 1:
    ans = "I'm Sorry Hansoo"
elif len(N)%2 == 0 and  cnt2 != 0:
    ans = "I'm Sorry Hansoo"
else:
    if m in N:
        ans.append(m)
        N.remove(m)
    for idx,i in enumerate(N):
        if idx%2 == 0:
            ans.append(i)
        else:
            ans.appendleft(i)
    ans = ''.join(ans)
print(ans)