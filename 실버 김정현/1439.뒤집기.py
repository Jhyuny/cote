"""
https://www.acmicpc.net/problem/1439
"""
S = list(input())
a = S[0]
ans = [a]
for i in S:
    if i == a:
        pass
    else:
        ans.append(i)
        a = i
print(min(ans.count('1'),ans.count('0')))
