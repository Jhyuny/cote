"""
https://www.acmicpc.net/problem/1316
"""
N = int(input())
cnt = N
for _ in range(N):
    word = input()
    l = []
    for idx in range(len(word)):
        if idx == len(word) - 1:
            if word[idx] in l:
                cnt -= 1
        elif word[idx] == word[idx + 1]:
            pass
        else:
            if word[idx] not in l:
                l.append(word[idx])
            else:
                cnt -= 1
                break
print(cnt)
