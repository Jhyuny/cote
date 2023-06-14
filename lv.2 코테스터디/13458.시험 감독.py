"""
https://www.acmicpc.net/problem/13458
"""
N = int(input())
l = list(map(int,input().split()))
B,C = list(map(int,input().split()))
l2 = [i-B for i in l]
ans = 0
for i in l2:
    if i>0:
        if i%C == 0:
            ans += i//C
        else:
            ans += i//C + 1
print(ans+N)