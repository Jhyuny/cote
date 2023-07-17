"""
https://www.acmicpc.net/problem/1292
"""
A, B = map(int,input().split())
def findnum(num):
    a = 1
    while num > a:
        num = num -a
        a += 1
    return a,num
a,na = findnum(A)
b,nb = findnum(B)
if A == B:
    ans = a
elif a == b:
    ans = b*nb
else:
    ans = a*(a-na+1) + b*(nb)
    for i in range(a+1,b):
        ans = ans + i*i
print(ans)