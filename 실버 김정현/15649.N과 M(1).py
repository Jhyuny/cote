"""
https://www.acmicpc.net/problem/15649
"""

# M,N<=8 : 반복문 허용
N, M = map(int,input().split())

for i in range(N):
    l = []
    for j in range(N):
        if j in l:
            while j not in l:
                j+=1
            l.append(j)
        else:
            l.append(j)
        if len(l) == M:
            print(l,sep=" ")
            break
        
    