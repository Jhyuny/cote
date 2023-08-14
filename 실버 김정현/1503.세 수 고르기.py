"""
https://www.acmicpc.net/problem/1503
"""
N,S = map(int,input().split())
if S == 0:
    print(0)
else:
    nums = list(map(int,input().split()))
    ans = 1001
    for x in range(1001):
        print(x)
        if x in nums:
            continue
        for y in range(1001):
            if y in nums:
                continue
            for z in range(1001):
                if z in nums:
                    continue
                ans = min(ans,abs(N-x*y*z))
    print(ans)