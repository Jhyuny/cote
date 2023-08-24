"""
https://www.acmicpc.net/problem/1449
"""
N, L = map(int,input().split())
crack=sorted(list(map(int,input().split())))
tape=2000
cnt=1
for i in crack:
    tape=min(tape,i-0.5+L)
    if i<tape:
        continue
    else:
        tape=i-0.5+L
        cnt+=1
print(cnt)
