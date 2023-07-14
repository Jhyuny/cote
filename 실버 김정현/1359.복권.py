"""
https://www.acmicpc.net/problem/1359
"""
def fac(num):
    k = 1
    for i in range(1,num+1):
        k *= i
    return k
N,M,K = map(int,input().split())
ans = 0
for k in range(K,M+1):
    p = ((fac(M)/(fac(k)*fac(M-k)))*(fac(N-M)/(fac(M-k)*fac(N-2*M+k))))/(fac(N)/(fac(M)*fac(N-M)))
    ans = ans + p
print(ans)