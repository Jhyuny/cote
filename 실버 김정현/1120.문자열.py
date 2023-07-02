"""
https://www.acmicpc.net/problem/1120
"""
A,B = map(str,input().split())
ans = 52
for i in range(0,len(B)-len(A)+1):
    cnt = 0
    for a,b in zip(A,B[i:i+len(A)]):
        if a!=b:
            cnt += 1
    ans = min(ans,cnt)
print(ans)