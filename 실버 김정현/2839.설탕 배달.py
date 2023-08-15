"""
https://www.acmicpc.net/problem/2839
"""
N=int(input())
if N%5 == 0:
    print(N//5)
else:
    box_5 = N//5
    while (N-box_5*5)%3 != 0:
        box_5 -= 1
        if box_5<0:
            break
    box_3 = (N-box_5*5)//3
    if box_5<0:
        print(-1)
    else:
        print(box_5+box_3)