"""
https://www.acmicpc.net/problem/1417
"""
N = int(input())
dasom = int(input())
if N == 1:
    cand = [0]
else:    
    cand = [ int(input()) for i in range(N-1)]
ans = 0
while dasom <= max(cand):
    m = max(cand)
    dasom += 1
    new_m = m -1
    cand.remove(m)
    cand.append(new_m)
    ans += 1
print(ans)