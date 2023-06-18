"""
https://www.acmicpc.net/problem/1181
"""
N = int(input())
l = []
for _ in range(N):
    word = input()
    if [len(word),word] not in l:
        l.append([len(word),word])

l.sort(key = lambda x:(x[0], x[1]))

for i in l:
    print(i[1])
