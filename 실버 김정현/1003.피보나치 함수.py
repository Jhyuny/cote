"""
https://www.acmicpc.net/problem/1003
"""

def fibonacci(n):
    for i in range(n+1):
        if i>1:
            l.append([l[i-2][0]+l[i-1][0], l[i-2][1]+l[i-1][1], i])
    return

T = int(input())
for _ in range(T):
    n = int(input())
    zero = [1,0,0]
    one = [0,1,1]
    l=[zero,one]

    fibonacci(n)
    print(l[n][0],l[n][1])