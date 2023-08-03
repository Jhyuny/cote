"""
https://www.acmicpc.net/problem/1024
"""
N, L = map(int,input().split())
while L<=100:
    sum = 0
    for i in range(L+1):
        sum += i
    K = L*((N-sum)//L) + sum
    if K == N and N-sum>=-L:
        ans = []
        for i in range(L):
            ans.append((N-sum)//L+i+1)
        print(*ans)
        break
    L += 1
if L>100:
    print(-1)