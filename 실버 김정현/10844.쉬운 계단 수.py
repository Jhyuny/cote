"""
https://www.acmicpc.net/problem/10844
"""
N = int(input())

l = 10**(N-1)
r = 10**N

def check(l):
    for i in range(1,len(l)):
        if abs(l[i-1]-l[i]) == 1:
            pass
        else:
            return 0
    return 1

cnt = 0

for i in range(l,r):
    num = list(map(int,list(str(i))))
    if check(num):
        cnt +=1

print(cnt%1000000000)