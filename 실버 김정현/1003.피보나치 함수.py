"""
https://www.acmicpc.net/problem/1003
"""
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return str(fibonacci(n - 1)) + str(fibonacci(n - 2))

N=int(input())
nums=[int(input()) for _ in range(N)]
for i in nums:
    cnt_1=cnt_0=0
    for j in list(str(fibonacci(i))):
        if j=='1':
            cnt_1+=1
        else:
            cnt_0+=1
    print(cnt_0, cnt_1)